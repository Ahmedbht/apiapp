from fastapi import FastAPI, HTTPException, Depends
from app.schemas import PostCreate, PostResponse
from sqlalchemy.orm import Session
from app import models
from app.database import engine ,get_db
from typing import List

models.Base.metadata.create_all(bind=engine)
app =FastAPI()



@app.get("/posts", response_model=List[PostResponse])
def get_all_posts(db:Session =Depends(get_db)):
    #get all posts from db
    posts= db.query(models.Post).all()
    return posts

@app.get("/posts/{id}", response_model=PostResponse)
def get_posts(id: int, db: Session =Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id ==id).first()
    if not post:
        raise HTTPException(status_code=404 , detail="Page not found")
    return post

@app.post("/posts")
def create_post(post: PostCreate, db:Session =Depends(get_db)):
    new_post= models.Post(
        title=post.title,
        content=post.content,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.delete("/posts/{id}")
def delete_post(id: int,db: Session= Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id ==id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return{"message": f"Post {id} deleted successfully"}