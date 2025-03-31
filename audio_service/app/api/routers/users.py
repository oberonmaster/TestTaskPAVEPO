from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from audio_service.app.db.models import User
from audio_service.app.db.base import async_session_maker
from audio_service.app.core.security import get_current_user

router = APIRouter()


async def get_db():
    async with async_session_maker() as session:
        yield session


@router.get("/users/me")
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email, "name": current_user.name}


@router.patch("/users/me")
async def update_user_info(name: str, current_user: User = Depends(get_current_user),
                           db: AsyncSession = Depends(get_db)):
    current_user.name = name
    db.add(current_user)
    await db.commit()
    return {"message": "User updated successfully"}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Access denied")

    user = await db.execute(select(User).filter(User.id == user_id))
    user = user.scalar()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}
