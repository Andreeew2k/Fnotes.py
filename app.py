from flask import Flask
from gevent.pywsgi import WSGIServer


from sqlalchemy import Column, Integer, String, ARRAY, create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:12345678@localhost/dbforpp', echo=True)


Session = sessionmaker(bind=engine)
session = Session()

@app.route('/api/v1/hello-word-17')
def index():
    return "Hello world 17"

if __name__=="__main__":
    WSGIServer(('', 5000), app).serve_forever()