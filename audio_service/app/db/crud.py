from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from audio_service.app.db.models import User, AudioFile

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar()

async def create_user(db: AsyncSession, email: str, name: str, is_superuser: bool = False):
    user = User(email=email, name=name, is_superuser=is_superuser)
    db.add(user)
    await db.commit()
    return user

async def get_audio_files_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(AudioFile).filter(AudioFile.user_id == user_id))
    return result.scalars().all()

async def delete_audio_file(db: AsyncSession, file_id: int):
    file = await db.execute(select(AudioFile).filter(AudioFile.id == file_id))
    file = file.scalar()
    if file:
        await db.delete(file)
        await db.commit()
