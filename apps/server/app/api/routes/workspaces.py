from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_workspaces() -> dict[str, str]:
    """List all workspaces."""
    return {"message": "Not implemented yet"}


@router.post("/")
async def create_workspace() -> dict[str, str]:
    """Create new workspace."""
    return {"message": "Not implemented yet"}