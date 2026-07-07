from sqlalchemy import Column, Integer,String
from app.database import Base

#Posy =table in db
class Post(Base)
    __tablename__ ="posts"

    id= Column(Integer,primary_key=True ,index=True)
    title= Column(String, nullable=False)
    content= Column(String, nullable= False)