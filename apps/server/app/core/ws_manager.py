import contextlib

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        # ID документа -> список активных WebSocket соединений
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, document_id: str, websocket: WebSocket) -> None:
        """Принимает соединение и добавляет пользователя в комнату."""
        await websocket.accept()
        if document_id not in self.active_connections:
            self.active_connections[document_id] = []
        self.active_connections[document_id].append(websocket)

    def disconnect(self, document_id: str, websocket: WebSocket) -> None:
        """Удаляет пользователя из комнаты при отключении."""
        if document_id in self.active_connections:
            self.active_connections[document_id].remove(websocket)
            # Если комната пуста, удаляем её из памяти, чтобы не засорять RAM
            if not self.active_connections[document_id]:
                del self.active_connections[document_id]

    async def broadcast(
        self, document_id: str, message: bytes, exclude: WebSocket | None = None
    ) -> None:
        """Рассылает сообщение всем в комнате, кроме отправителя."""
        if document_id in self.active_connections:
            for connection in self.active_connections[document_id]:
                if connection != exclude:
                    # Yjs работает с бинарными данными (bytes)
                    with contextlib.suppress(Exception):
                        await connection.send_bytes(message)


# Создаем глобальный экземпляр менеджера
manager = ConnectionManager()
