from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_documents() -> dict[str, str]:
    """List all documents."""
    return {"message": "Not implemented yet"}


@router.post("/")
async def create_document() -> dict[str, str]:
    """Create new document."""
    return {"message": "Not implemented yet"}
