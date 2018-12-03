from application.database import *
from application.models import user

# 2 - generate database schema
Base.metadata.create_all(engine)
