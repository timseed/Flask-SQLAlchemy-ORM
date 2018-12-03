from application.database import *
import daiquiri
from application.models import user
logger=daiquiri.getLogger(__name__)
# 2 - generate database schema
Base.metadata.create_all(engine)
