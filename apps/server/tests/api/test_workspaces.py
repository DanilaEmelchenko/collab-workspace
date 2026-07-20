import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_workspace(client: AsyncClient) -> None:
    """Тест создания воркспейса (требуется авторизация)."""

    # Шаг 1: Создаём пользователя (владельца воркспейса)
    user_response = await client.post(
        "/api/users/", json={"email": "owner@example.com", "password": "secret123"}
    )
    assert user_response.status_code == 201, "Пользователь должен создаться"
    owner_id = user_response.json()["id"]

    # Шаг 2: Получаем JWT токен для этого пользователя
    login_response = await client.post(
        "/api/auth/token",
        data={"username": "owner@example.com", "password": "secret123"},  # OAuth2 ожидает form-data
    )
    assert login_response.status_code == 200, "Логин должен быть успешным"
    token = login_response.json()["access_token"]

    # Шаг 3: Создаём воркспейс с токеном в заголовке
    response = await client.post(
        "/api/workspaces/",
        json={"name": "Тестовый воркспейс", "owner_id": owner_id},
        headers={"Authorization": f"Bearer {token}"},  # 👈 Передаём токен
    )

    # Проверяем, что воркспейс создался
    assert response.status_code == 201, "Воркспейс должен создаться с кодом 201"
    data = response.json()
    assert data["name"] == "Тестовый воркспейс"
    assert data["owner_id"] == owner_id
    assert "id" in data


@pytest.mark.asyncio
async def test_list_workspaces(client: AsyncClient) -> None:
    """Тест получения списка воркспейсов (требуется авторизация)."""

    # Шаг 1: Создаём пользователя
    user_response = await client.post(
        "/api/users/", json={"email": "list@example.com", "password": "secret123"}
    )
    assert user_response.status_code == 201, "Пользователь должен создаться"
    owner_id = user_response.json()["id"]

    # Шаг 2: Получаем JWT токен
    login_response = await client.post(
        "/api/auth/token", data={"username": "list@example.com", "password": "secret123"}
    )
    assert login_response.status_code == 200, "Логин должен быть успешным"
    token = login_response.json()["access_token"]

    # Шаг 3: Создаём два воркспейса (с токеном)
    await client.post(
        "/api/workspaces/",
        json={"name": "Workspace 1", "owner_id": owner_id},
        headers={"Authorization": f"Bearer {token}"},
    )
    await client.post(
        "/api/workspaces/",
        json={"name": "Workspace 2", "owner_id": owner_id},
        headers={"Authorization": f"Bearer {token}"},
    )

    # Шаг 4: Получаем список воркспейсов (с токеном)
    response = await client.get("/api/workspaces/", headers={"Authorization": f"Bearer {token}"})

    # Проверяем результат
    assert response.status_code == 200, "Список воркспейсов должен возвращаться с кодом 200"
    data = response.json()
    assert isinstance(data, list), "Ответ должен быть списком"
    assert len(data) >= 2, "Должно быть хотя бы 2 воркспейса"
