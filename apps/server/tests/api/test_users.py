import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient) -> None:
    """Тест создания пользователя."""
    response = await client.post(
        "/api/users/", json={"email": "test@example.com", "password": "secret123"}
    )

    assert response.status_code == 201

    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["is_active"] is True
    assert "id" in data
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_create_user_duplicate_email(client: AsyncClient) -> None:
    """Тест создания пользователя с дублирующимся email."""
    await client.post(
        "/api/users/", json={"email": "duplicate@example.com", "password": "secret123"}
    )

    response = await client.post(
        "/api/users/", json={"email": "duplicate@example.com", "password": "secret456"}
    )

    assert response.status_code == 400
    assert "email уже существует" in response.json()["detail"]


@pytest.mark.asyncio
async def test_get_user_by_id(client: AsyncClient) -> None:
    """Тест получения пользователя по ID."""
    create_response = await client.post(
        "/api/users/", json={"email": "getuser@example.com", "password": "secret123"}
    )
    user_id = create_response.json()["id"]

    response = await client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == "getuser@example.com"


@pytest.mark.asyncio
async def test_get_user_not_found(client: AsyncClient) -> None:
    """Тест получения несуществующего пользователя."""
    response = await client.get("/api/users/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
