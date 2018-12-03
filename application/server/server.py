from flask import Flask
from .config import ProductionConfig, TestingConfig, DevelopmentConfig
import os
app = Flask(__name__)
try:
    env=os.getenv("FLASK_ENV").upper()
except:
    print("Error No FLASK_ENV set")
    print("Defaulting to DEVELOPMENT MODE")
    env="DEVELOPMENT"
    pass

if env.startswith("PRO"):
        app.config.from_object(ProductionConfig)
        app.config['FLASK_ENV']="PRODUCTION"
elif env.startswith("TES"):
            app.config.from_object(TestingConfig)
            app.config['FLASK_ENV'] = "TEST"
else:
    app.config.from_object(ProductionConfig)
    app.config['FLASK_ENV'] = "DEVELOPMENT"
