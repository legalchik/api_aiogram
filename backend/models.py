import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship
from datetime import datetime

from database import metadata, engine






metadata.create_all(engine)
