from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MenClothes(Base):
    __tablename__ = 'men_clothes'
    sku    = Column(Integer, primary_key=True, nullable=False)
    name   = Column(String, nullable=False)
    price  = Column(Float, nullable=False)
    images = Column(String, nullable=False)

class WomenClothes(Base):
    __tablename__ = 'women_clothes'
    sku    = Column(Integer, primary_key=True, nullable=False)
    name   = Column(String, nullable=False)
    price  = Column(Float, nullable=False)
    images = Column(String, nullable=False)

class Acessories(Base):
    __tablename__ = 'acessories'
    sku    = Column(Integer, primary_key=True, nullable=False)
    name   = Column(String, nullable=False)
    price  = Column(Float, nullable=False)
    images = Column(String, nullable=False)


sectionList       = [MenClothes, WomenClothes, Acessories]
sectionListString = ['MenClothes', 'WomenClothes', 'Acessories']