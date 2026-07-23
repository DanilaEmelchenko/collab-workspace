from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

# В будущем здесь будет логика Yjs и "комнат" (документов)


@router.websocket("/ws/documents/{document_id}")
async def websocket_document(websocket: WebSocket, document_id: str, token: str) -> None:
    """
    WebSocket соединение для редактирования документа.
    Клиент должен передать токен в query-параметре: ?token=xxx
    """
    # 1. Авторизация
    # WebSocket не поддерживает заголовки Authorization,
    # поэтому токен обычно передают в URL (query param) или в первом сообщении.
    try:
        # Мы используем нашу функцию декодирования напрямую,
        # так как Depends() в WebSocket работает немного иначе
        from app.core.security import decode_access_token

        payload = decode_access_token(token)
        if not payload:
            await websocket.close(code=4001, reason="Invalid token")
            return

        user_id = payload.get("sub")
        # В реальном приложении здесь мы бы загрузили User из БД
        # user = await get_user(db, user_id)
    except Exception:
        await websocket.close(code=4001, reason="Auth failed")
        return

    # 2. Подключение
    await websocket.accept()
    print(f"User {user_id} connected to document {document_id}")

    try:
        # 3. Цикл чтения сообщений
        while True:
            # Yjs отправляет бинарные данные (bytes), но для теста начнем с текста
            data = await websocket.receive_text()
            print(f"Received: {data}")

            # Эхо: отправляем обратно (в будущем здесь будет рассылка всем в комнате)
            await websocket.send_text(f"Echo: {data}")

    except WebSocketDisconnect:
        print(f"User {user_id} disconnected from document {document_id}")
