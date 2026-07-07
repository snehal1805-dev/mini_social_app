from fastapi import APIRouter
from fastapi import Header
from fastapi import Depends
from fastapi import HTTPException


from utils.auth import get_current_user


from sqlalchemy.orm import Session

from database import get_db

from models.user_model import User

from schemas.user_schema import UserCreate

from utils.auth import hash_password

from schemas.user_schema import UserLogin
from utils.auth import verify_password
from utils.auth import create_access_token

from utils.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm




router = APIRouter()


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = hash_password(
        user.password[:72]
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Registered Successfully 😎"
    }


@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=400,
            detail="Invalid Email"
        )

    is_password_correct = verify_password(
        form_data.password,
        existing_user.password
    )

    if not is_password_correct:

        raise HTTPException(
            status_code=400,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        data={
            "user_id": existing_user.id
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }







