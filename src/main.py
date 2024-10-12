from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/disk/create", response_model=schemas.Disk)
def create_disk(disk: schemas.DiskCreate, db: Session = Depends(get_db)):
    return crud.create_disk(db=db, disk=disk)


@app.get("/disk/read/id/{disk_id}", response_model=schemas.Disk)
def read_disk(disk_id: int, db: Session = Depends(get_db)):
    db_disk = crud.get_disk(db, disk_id=disk_id)
    if db_disk is None:
        raise HTTPException(status_code=404, detail="Disk not found")
    return db_disk


@app.get("/disk/read/name/{disk_name}", response_model=schemas.Disk)
def read_disk_by_name(disk_name: str, db: Session = Depends(get_db)):
    db_disk = crud.get_disk_by_name(db, disk_name=disk_name)
    if db_disk is None:
        raise HTTPException(status_code=404, detail="Disk not found")
    return db_disk


@app.get("/disk/delete/id/{disk_id}")
def delete_disk_by_id(disk_id: int, db: Session = Depends(get_db)):
    affected_rows = crud.delete_disk_by_id(db, disk_id=disk_id)
    if affected_rows != 1:
        raise HTTPException(status_code=404, detail="Delete Disk error")


@app.get("/disk/delete/name/{disk_name}")
def delete_disk_by_name(disk_name: str, db: Session = Depends(get_db)):
    affected_rows = crud.delete_disk_by_name(db, disk_name=disk_name)
    if affected_rows != 1:
        raise HTTPException(status_code=404, detail="Delete Disk error")


@app.get("/disks/", response_model=list[schemas.Disk])
def read_disks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    disks = crud.get_disks(db, skip=skip, limit=limit)
    return disks
