from flask import Flask
from flask_restful import Resource, Api

from gevent.pywsgi import WSGIServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controller import *

app = Flask(__name__)
api = Api(app)

engine = create_engine('postgresql://ppadmin:admin@localhost/ppdb-andrew', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
#test_user2 = Note("Test note", "Note text...",0)
#session.add(test_user2)
#session.commit()

if __name__=="__main__":

    api.add_resource(GetNote, '/note/<int:id>')
    api.add_resource(DeleteNote, '/note/<int:id>')
    api.add_resource(AddNote, '/note')
    api.add_resource(GetNotesByGroup, '/note/get_by_group/<int:group_id>')
    api.add_resource(UpdateNote, '/note/<int:id>')

    api.add_resource(DeleteUser, '/user/<int:id>')
    api.add_resource(GetUser, '/user/<int:id>')
    api.add_resource(AddUser, '/user/')
    api.add_resource(UpdateUser, '/user/<int:id>')
    WSGIServer(('', 5000), app).serve_forever()