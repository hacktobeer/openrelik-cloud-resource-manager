from pydantic import BaseModel


class DiskBase(BaseModel):
    name: str
    provider: str
    device: str
    port: int


class DiskCreate(DiskBase):
    pass


class Disk(DiskBase):
    id: int

    class Config:
        from_attributes = True
