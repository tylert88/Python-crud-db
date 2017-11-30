from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import backref, relationship
from automagic_api import Base



class Policy(Base):
    @declared_attr
    def __tablename__(cls):
        # API endpoint will take the form '/api/__tablename__'
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    policy_type = Column(String(64))
    amount = Column(String(64))
    expires = Column(String(64))

class Features(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer,
        ForeignKey("policy.id"), nullable=True)
    name = Column(String(64))
    value = Column(String(2000))
    policy = relationship(Policy,
        backref=backref('features'))
    data_type = Column(String(64))
