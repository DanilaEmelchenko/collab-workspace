import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_login_success(client: AsyncClient) -> None:
    """Тест успешного получения токена."""
    # Сначала создаем пользователя
    await client.post("/api/users/", json={"email": "test@example.com", "password": "secret123"})

    # Пытаемся получить токен
    response = await client.post(
        "/api/auth/token", data={"username": "test@example.com", "password": "secret123"}
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient) -> None:
    """Тест логина с неправильным паролем."""
    # Создаем пользователя
    await client.post("/api/users/", json={"email": "test2@example.com", "password": "secret123"})

    # Пытаемся войти с неправильным паролем
    response = await client.post(
        "/api/auth/token", data={"username": "test2@example.com", "password": "wrongpassword"}
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_protected_endpoint_without_token(client: AsyncClient) -> None:
    """Тест защищенного эндпоинта без токена."""
    response = await client.get("/api/workspaces/")

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_protected_endpoint_with_token(client: AsyncClient) -> None:
    """Тест защищенного эндпоинта с валидным токеном."""
    # Создаем пользователя и получаем токен
    await client.post("/api/users/", json={"email": "test3@example.com", "password": "secret123"})

    login_response = await client.post(
        "/api/auth/token", data={"username": "test3@example.com", "password": "secret123"}
    )
    token = login_response.json()["access_token"]

    # Делаем запрос с токеном
    response = await client.get("/api/workspaces/", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
