from flask import json, Response, request
from flask_restful import Resource, Api
from models import *


from sqlalchemy import Column, Integer, String, ARRAY, create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

from types import SimpleNamespace

from app import session

class GetNote(Resource):
    def get(self, id):
        note = session.query(Note).get(id)
        if note:
            return Response(
                response=json.dumps(note, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )

class DeleteNote(Resource):
    def delete(self, id):
        note = session.query(Note).filter(Note.id==id).delete()
        if note:
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )

class AddNote(Resource):
    def post(self):
        data = request.json
        try:
            note = Note(data["name"],data["text"],data["group_id"])
            session.add(note)
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class UpdateNote(Resource):
    def put(self, id):
        data = request.json
        try:
            note = session.query(Note).get(id)
            if "name" in data:
                note.name = data["name"]
            if "text" in data:
                note.text = data["text"]
            if "group_id" in data:
                note.group_id = data["group_id"]
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except Exception as e:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class GetNotesByGroup(Resource):
    def get(self, group_id):
        notes = session.query(Note).filter(Note.group_id==group_id).all()
        if notes:
            return Response(
                response=json.dumps(notes, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps({"message": "Not found"}),
            status=400,
            mimetype="application/json"
        )


class AddUser(Resource):
    def post(self):
        data = request.json
        try:
            user = User(data["username"],data["first_name"],data["last_name"],data["email"],data["password"])
            session.add(user)
            session.flush()
            if "groups" in data:
                for group in data["groups"]:
                    invited = Invited(user.id,group)
                    session.add(invited)
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )

class UpdateUser(Resource):
    def put(self, id):
        data = request.json
        try:
            user = session.query(User).get(id)
            if "username" in data:
                user.username = data["username"]
            if "first_name" in data:
                user.first_name = data["first_name"]
            if "last_name" in data:
                user.last_name = data["last_name"]
            if "email" in data:
                user.email = data["email"]
            if "password" in data:
                user.password = data["password"]
            if "groups" in data:
                session.query(Invited).filter(Invited.user_id==user.id).delete()
                for group in data["groups"]:
                    invited = Invited(user.id,group)
                    session.add(invited)
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except Exception as e:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class GetUser(Resource):
    def get(self, id):
        user = session.query(User).get(id)
        if user:
            return Response(
                response=json.dumps(user, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )



class DeleteUser(Resource):
    def delete(self, id):
        user = session.query(User).filter(User.id==id).delete()
        if user:
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )