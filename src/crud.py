from sqlalchemy.orm import Session
from . import models, schemas

import logging

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


def get_disk(db: Session, disk_id: int):
    return db.query(models.Disk).filter(models.Disk.id == disk_id).first()


def get_disk_by_name(db: Session, disk_name: str):
    return db.query(models.Disk).filter(models.Disk.name == disk_name).first()


def get_disks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disk).offset(skip).limit(limit).all()


def create_disk(db: Session, disk: schemas.DiskCreate):
    db_disk = models.Disk(
        name=disk.name, provider=disk.provider, device=disk.device, port=disk.port
    )
    db.add(db_disk)
    db.commit()
    db.refresh(db_disk)
    return db_disk


def delete_disk_by_id(db: Session, disk_id: int):
    affected_rows = db.query(models.Disk).filter(models.Disk.id == disk_id).delete()
    if affected_rows > 0:
        db.commit()
    return affected_rows


def delete_disk_by_name(db: Session, disk_name: str):
    affected_rows = db.query(models.Disk).filter(models.Disk.name == disk_name).delete()
    if affected_rows > 0:
        db.commit()
    return affected_rows
