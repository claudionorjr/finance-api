import os

# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CRYPT_KEY = os.environ.get("CRYPT_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DEV_DATABASE_URL') 

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')

class UnixConfig(ProductionConfig):
    """Configuração para inplantação em sistemas baseados em Unix"""

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        #log disponivel para administrador do SO em syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'unix' : UnixConfig,

    'default':DevelopmentConfig
}