from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.core.security import decode_access_token
from app.core.ws_manager import manager
from app.crud.user import get_user
from app.db.session import get_session

router = APIRouter()


@router.websocket("/ws/documents/{document_id}")
async def websocket_document(websocket: WebSocket, document_id: str, token: str) -> None:
    """WebSocket для совместного редактирования документа."""

    # 1. Авторизация
    payload = decode_access_token(token)
    if not payload or not payload.get("sub"):
        await websocket.close(code=4001, reason="Invalid token")
        return

    user_id = payload.get("sub")
    if user_id is None:
        await websocket.close(code=4001, reason="Invalid token")
        return

    # Явно преобразуем в строку
    user_id_str: str = str(user_id)

    # 2. Проверяем, существует ли пользователь в БД
    async for db in get_session():
        user = await get_user(db, user_id_str)
        if not user:
            await websocket.close(code=4001, reason="User not found")
            return
        break

    # 3. Подключаем пользователя к комнате через менеджер
    await manager.connect(document_id, websocket)
    print(f"✅ User {user_id_str} joined room {document_id}")

    try:
        # 4. Читаем бинарные сообщения от клиента (Yjs шлет bytes)
        while True:
            data = await websocket.receive_bytes()

            # 5. Рассылаем всем остальным в этой комнате
            await manager.broadcast(document_id, data, exclude=websocket)

    except WebSocketDisconnect:
        # 6. Чистим за собой при отключении
        manager.disconnect(document_id, websocket)
        print(f"❌ User {user_id_str} left room {document_id}")
