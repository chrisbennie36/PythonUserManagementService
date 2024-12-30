from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, Select
from Domain.Dtos.UserDto import UserDto
from Data.Entities.User import User

class UserRepository(DeclarativeBase):
    def __init__(self):
        global database
        database = SQLAlchemy(model_class=UserRepository)

        global app
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users-collection.db"
        database.init_app(app)

        class User(database.Model):
            __tablename__ = 'Users'
            id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
            username: Mapped[str] = mapped_column(String(250), nullable=False)

            def __init__(self, username):
                self.username = username

            def __repr__(self):
                return f'<User {self.username}>'

        with app.app_context():
            database.create_all()

    def getUserById(self, user_id: int):
        with app.app_context():
            return database.get_or_404(User, user_id)

    def addUser(self, user_dto: UserDto):
        with app.app_context():
            new_user = User(username=user_dto.username)
            database.session.add(new_user)
            database.session.commit()

    def deleteUser(self, user_id: int):
        with app.app_context():
            user_to_delete = database.get_or_404(User, user_id)
            database.session.delete(user_to_delete)
            database.session.commit()

    def updateUserUsername(self, user_id: int, user_dto: UserDto):
        with app.app_context():
            user_to_update = database.session.execute(database.select(User).where(User.id == user_id)).scalar()
            # or user_to_update = database.get_or_404(User, user_id)  
            user_to_update.username = user_dto.username
            database.session.commit() 
