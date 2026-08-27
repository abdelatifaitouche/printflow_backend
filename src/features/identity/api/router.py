from fastapi import APIRouter


router = APIRouter(prefix="/auth")


@router.post("/register")
async def register_user():
    return


@router.post("/token")
async def login():
    return


@router.post("/refresh")
async def refresh_token():
    return
