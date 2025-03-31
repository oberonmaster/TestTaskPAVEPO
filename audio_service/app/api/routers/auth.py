from fastapi import APIRouter, Depends
from audio_service.app.services.yandex_auth import get_yandex_token, get_yandex_user_info

router = APIRouter()

@router.get("/auth/yandex")
async def login_via_yandex():
    return {"login_url": f"https://oauth.yandex.ru/authorize?response_type=code&client_id=your_client_id"}

@router.get("/auth/yandex/callback")
async def yandex_callback(code: str):
    token_data = await get_yandex_token(code)
    user_info = await get_yandex_user_info(token_data["access_token"])
    return user_info
