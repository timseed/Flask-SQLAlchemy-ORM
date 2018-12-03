from pathlib import Path

class Config:
    __ROOT_PATH = Path(__file__).resolve().parent.parent
    DEBUG = False
    TESTING = False
    SECRET_KEY = b'topsecreTKeY' # Change to a new KEY!
    ROOT_PATH = __ROOT_PATH
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{ROOT_PATH}/db/test.db'    # SQLite, etc.
    STATIC_FOLDER = f'{ROOT_PATH}/views/static'
    TEMPLATE_FOLDER = f'{ROOT_PATH}/views/template'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    __ROOT_PATH = Path(__file__).resolve().parent.parent
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{__ROOT_PATH}/db/prod.db'  # SQLite, etc.
    junk=1


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    ENV = 'development'


class TestingConfig(Config):
    TESTING = True