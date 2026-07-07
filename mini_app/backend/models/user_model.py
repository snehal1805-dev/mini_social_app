from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    posts = relationship(
    "Post",
    back_populates="owner"
    )

