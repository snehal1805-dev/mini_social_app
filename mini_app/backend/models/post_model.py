
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from database import Base

from sqlalchemy.orm import relationship


class Post(Base):

    __tablename__ = "posts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    content = Column(
        String(500),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    owner = relationship(
    "User",
    back_populates="posts"
    )
