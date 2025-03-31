from fastapi import APIRouter
import audio_service.app.api.routers.files as files
import audio_service.app.api.routers.users as users
import audio_service.app.api.routers.auth as auth


api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(files.router, prefix="/files", tags=["Files"])
