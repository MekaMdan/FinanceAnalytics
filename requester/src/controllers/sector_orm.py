from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_orm import Base


class SectorOrm(Base):
    __tablename__ = 'sectors'
    id = Column(Integer, primary_key=True)
    sector_name = Column(String(40))

    def __init__(self,sector:str):
        self.sector_name = sector

    def __repr__(self) -> str:
        return f"Sector({self.id}, {self.sector_name})"

