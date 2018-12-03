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
elif env.startswith("TES"):
            app.config.from_object(TestingConfig)
else:
    app.config.from_object(ProductionConfig)
