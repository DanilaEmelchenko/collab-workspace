import asyncio

import websockets

from app.core.security import create_access_token


async def simulate_user(user_name: str, token: str, doc_id: str) -> None:
    uri = f"ws://localhost:8000/ws/documents/{doc_id}?token={token}"
    async with websockets.connect(uri) as ws:
        print(f"[{user_name}] Подключен!")

        await asyncio.sleep(1)

        msg = f"Привет от {user_name}!".encode()
        await ws.send(msg)
        print(f"[{user_name}] Отправил: {msg!r}")

        try:
            response = await asyncio.wait_for(ws.recv(), timeout=2.0)

            if isinstance(response, bytes):
                print(
                    f"[{user_name}] Получил (bytes): {response.decode('utf-8', errors='replace')}"
                )
            else:
                print(f"[{user_name}] Получил (str): {response}")

        except TimeoutError:
            print(f"[{user_name}] Ничего не получил (это нормально, если он был один)")


async def main() -> None:
    token1 = create_access_token(data={"sub": "user-1"})
    token2 = create_access_token(data={"sub": "user-2"})
    doc_id = "doc-123"

    await asyncio.gather(
        simulate_user("User-1", token1, doc_id), simulate_user("User-2", token2, doc_id)
    )


if __name__ == "__main__":
    asyncio.run(main())
