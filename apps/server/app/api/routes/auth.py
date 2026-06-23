from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register() -> dict[str, str]:
    """Register new user."""
    return {"message": "Not implemented yet"}


@router.post("/login")
async def login() -> dict[str, str]:
    """Login user."""
    return {"message": "Not implemented yet"}