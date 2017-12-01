
import io
import flask
import flask_restless
from flask_cors import CORS
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import *
from flask_heroku import Heroku


app = flask.Flask(__name__)
heroku = Heroku(app)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# Create our SQLAlchemy DB engine
engine = create_engine('sqlite:///foobar.db')
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
s = scoped_session(Session)

Base = declarative_base()
Base.metadata.bind = engine

# Import all models to add them to Base.metadata
from .models import Features, Policy

Base.metadata.create_all()

manager = flask_restless.APIManager(app, session=s)
# Register flask-restless blueprints to instantiate CRUD endpoints
from .controllers import features_api_blueprint, policy_api_blueprint
app.register_blueprint(policy_api_blueprint)
app.register_blueprint(features_api_blueprint)
