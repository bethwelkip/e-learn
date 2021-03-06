import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/elearn'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bethwelkiplimo:password@localhost/elearn'
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

    #  email configurations

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}