from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.core.security import decode_access_token
from app.core.ws_manager import manager

router = APIRouter()


@router.websocket("/ws/documents/{document_id}")
async def websocket_document(
    websocket: WebSocket, document_id: str, token: str
) -> None:  # Добавляем тип возврата
    """WebSocket для совместного редактирования документа."""

    # 1. Авторизация (как и раньше)
    payload = decode_access_token(token)
    if not payload or not payload.get("sub"):
        await websocket.close(code=4001, reason="Invalid token")
        return

    user_id = payload.get("sub")

    # 2. Подключаем пользователя к комнате через менеджер
    await manager.connect(document_id, websocket)
    print(f"✅ User {user_id} joined room {document_id}")

    try:
        # 3. Читаем бинарные сообщения от клиента (Yjs шлет bytes)
        while True:
            data = await websocket.receive_bytes()

            # 4. Рассылаем всем остальным в этой комнате
            await manager.broadcast(document_id, data, exclude=websocket)

    except WebSocketDisconnect:
        # 5. Чистим за собой при отключении
        manager.disconnect(document_id, websocket)
        print(f"❌ User {user_id} left room {document_id}")
