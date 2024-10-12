from sqlalchemy import Column, Integer, String
from .database import Base


class Disk(Base):
    __tablename__ = "disks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    provider = Column(String, index=True)
    device = Column(String, index=True)
    port = Column(Integer, index=True)
