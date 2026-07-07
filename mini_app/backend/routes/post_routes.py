
from fastapi import APIRouter
from fastapi import Depends


from fastapi import HTTPException



from sqlalchemy.orm import Session

from database import get_db

from models.post_model import Post
from models.user_model import User

from schemas.post_schema import (
    PostCreate,
    PostResponse
)

from utils.auth import get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.post(
    "/",
    response_model=PostResponse
)
def create_post(

    post: PostCreate,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    new_post = Post(

        content=post.content,

        user_id=current_user.id
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post


@router.get(
    "/",
    response_model=list[PostResponse]
)
def get_posts(
    db: Session = Depends(get_db)
):

    posts = db.query(Post).all()

    return [

        {
            "id": post.id,
            "content": post.content,
            "user_id": post.user_id,
            "username": post.owner.username
        }

        for post in posts
    ]



@router.get(
    "/{post_id}",
    response_model=PostResponse
)
def get_single_post(

    post_id: int,

    db: Session = Depends(get_db)

):

    post = db.query(Post).filter(
        Post.id == post_id
    ).first()

    if not post:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post


@router.delete("/{post_id}")
def delete_post(

    post_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    post = db.query(Post).filter(
        Post.id == post_id
    ).first()

    if not post:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    if post.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="You cannot delete this post"
        )

    db.delete(post)

    db.commit()

    return {
        "message": "Post deleted successfully"
    }






