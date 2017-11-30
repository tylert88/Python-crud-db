import flask
from flask_cors import CORS
import flask_restless
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import *
# from sqlalchemy import event
# import pprint
# pp = pprint

app = flask.Flask(__name__)
app.config['sqlite:///foobar.db'] = os.environ['postgresql-graceful-65432']
db = SQLAlchemy(app)
cors = CORS(app)

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


# # standard decorator style
# @event.listens_for(engine, 'handle_error')
# def receive_handle_error(exception_context):
#     "listen for the 'handle_error' event"
#     print('ERROR - FUCKIN ERRS!')
