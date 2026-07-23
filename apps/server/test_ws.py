import asyncio

import websockets

from app.core.security import create_access_token


async def test_websocket() -> None:
    # 1. Создаем фейковый токен (как будто мы залогинились)
    token = create_access_token(data={"sub": "test-user-123"})

    # 2. Подключаемся к серверу
    uri = f"ws://localhost:8000/ws/documents/doc-1?token={token}"

    print(f"Connecting to {uri}...")
    async with websockets.connect(uri) as websocket:
        print("Connected!")

        # 3. Отправляем сообщение
        await websocket.send("Привет, это тест Yjs!")
        print("Sent message")

        # 4. Ждем ответа
        response = await websocket.recv()
        print(f"Received: {response}")


if __name__ == "__main__":
    asyncio.run(test_websocket())
