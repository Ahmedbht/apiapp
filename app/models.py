from sqlalchemy import Column, Integer,String, DateTime
from app.database import Base
from datetime import datetime
#Posy =table in db
class Post(Base):
    __tablename__ ="posts"

    id= Column(Integer,primary_key=True ,index=True)
    title= Column(String, nullable=False)
    content= Column(String, nullable= False)
    created_at= Column(DateTime, default=datetime.now)