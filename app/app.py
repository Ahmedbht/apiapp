from fastapi import FastAPI, HTTPException, Depends
from app.schemas import PostCreate
from sqlalchemy.orm import Session
from app import models
from app.database import engine ,get_db

models.Base.metadata.create_all(bind=engine)
app =FastAPI()

text_posts = {
    "1": {"title": "New Post", "content": "Cool test post"},
    "2": {"title": "Python Tip", "content": "Use list comprehensions for cleaner loops."},
    "3": {"title": "Daily Motivation", "content": "Consistency beats intensity every time."},
    "4": {"title": "Fun Fact", "content": "The first computer bug was an actual moth found in a Harvard Mark II."},
    "5": {"title": "Update", "content": "Just launched my new project! Excited to share more soon."},
    "6": {"title": "Tech Insight", "content": "Async IO in Python can massively speed up I/O-bound tasks."},
    "7": {"title": "Quote", "content": "Programs must be written for people to read, and only incidentally for machines."},
    "8": {"title": "Weekend Plans", "content": "Might finally clean up my GitHub repos... or just play some Minecraft."},
    "9": {"title": "Question", "content": "What's the most underrated Python library you've ever used?"},
    "10": {"title": "Mini Announcement", "content": "New video drops tomorrow covering the weirdest Python features!"},
}



@app.get("/posts")
def get_all_posts(db:Session =Depends(get_db)):
    #get all posts from db
    posts= db.query(models.Post).all()
    return posts

@app.get("/posts/{id}")
def get_post(id :int):
    if str(id) not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(str(id))

@app.post("/posts")
def create_post(post : PostCreate):
    new_id= str(len(text_posts)+1)

    text_posts[new_id]={
        "title" :post.title,
        "content": post.content
    }
    return {"id": new_id,"tilte": post.title, "content": post.content}

@app.delete("/posts/{id}")
def delete_post(id:int):
    if str(id) not in text_posts:
        raise HTTPException(status_code= 404, detail="Page not found")

    del text_posts[str(id)]
    return {"message": f"Post {id} deleted successfully"}
    