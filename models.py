from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/flask_intro"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    bio = db.Column(db.String(150))

    posts = db.relationship("Post", back_populates="author", lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, name={self.name}, bio={self.bio}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "bio": self.bio
        }

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(150), unique=True, nullable=False)
    body = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))

    author = db.relationship("User", back_populates="posts", lazy="subquery")

    def __repr__(self):
        return f"Post(id={self.id}, header={self.header}, body={self.body}, author_id={self.author_id}"

    def as_dict(self):
        return {cname: getattr(self.c.name) for c in self.__table__.columns}
        