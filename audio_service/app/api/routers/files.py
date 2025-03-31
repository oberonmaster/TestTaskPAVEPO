import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from audio_service.app.db.models import AudioFile
from sqlalchemy.ext.asyncio import AsyncSession
from audio_service.app.db.base import async_session_maker

router = APIRouter()

@router.post("/files/upload")
async def upload_audio(file: UploadFile = File(...), db: AsyncSession = Depends(async_session_maker)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    audio = AudioFile(filename=file.filename, path=file_path)
    db.add(audio)
    await db.commit()
    return {"filename": file.filename, "path": file_path}
