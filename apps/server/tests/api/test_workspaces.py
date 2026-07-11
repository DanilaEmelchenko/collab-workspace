import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_workspace(client: AsyncClient) -> None:
    """Тест создания воркспейса."""
    user_response = await client.post(
        "/api/users/", json={"email": "owner@example.com", "password": "secret123"}
    )
    owner_id = user_response.json()["id"]

    response = await client.post(
        "/api/workspaces/", json={"name": "Тестовый воркспейс", "owner_id": owner_id}
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Тестовый воркспейс"
    assert data["owner_id"] == owner_id
    assert "id" in data


@pytest.mark.asyncio
async def test_list_workspaces(client: AsyncClient) -> None:
    """Тест получения списка воркспейсов."""
    user_response = await client.post(
        "/api/users/", json={"email": "list@example.com", "password": "secret123"}
    )
    owner_id = user_response.json()["id"]

    await client.post("/api/workspaces/", json={"name": "Workspace 1", "owner_id": owner_id})
    await client.post("/api/workspaces/", json={"name": "Workspace 2", "owner_id": owner_id})

    response = await client.get("/api/workspaces/")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
