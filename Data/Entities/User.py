from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'