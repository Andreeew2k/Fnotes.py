from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    is_public = Column(Boolean)

    def __init__(self, name, is_public):
        self.name = name
        self.is_public = is_public

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    text = Column(String)
    group_id = Column(Integer)

    def __init__(self, name, text,  group_id):
        self.name = name
        self.text = text
        self.group_id = group_id

class Invited(Base):
    __tablename__ = 'invited'
    id = Column(Integer,primary_key=True, unique=True)
    user_id = Column(Integer)
    group_id = Column(Integer)

    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

