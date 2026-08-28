from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.features.identity.api.dependencies import get_uc
from src.features.identity.application.user_usecases import UserUC
from src.features.identity.api.commands.write_commands import CreateUserCommand
from src.features.identity.application.dtos.user_dto import CreateUser

router = APIRouter(prefix="/auth")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    data: CreateUserCommand,
    uc: UserUC = Depends(get_uc),
):
    await uc.register_user(
        CreateUser(
            email=data.email,
            password=data.password,
        ),
    )
    return JSONResponse(
        content={"response": "User Created"},
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/token")
async def login():
    return


@router.post("/refresh")
async def refresh_token():
    return
