import httpx
from audio_service.app.core.config import settings

YANDEX_OAUTH_URL = "https://oauth.yandex.ru/token"
YANDEX_USER_INFO_URL = "https://login.yandex.ru/info"

async def get_yandex_token(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(YANDEX_OAUTH_URL, data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": settings.YANDEX_CLIENT_ID,
            "client_secret": settings.YANDEX_CLIENT_SECRET,
        })
        return response.json()

async def get_yandex_user_info(token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(YANDEX_USER_INFO_URL, headers={"Authorization": f"OAuth {token}"})
        return response.json()
