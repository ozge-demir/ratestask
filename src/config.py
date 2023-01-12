class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:ratestask@localhost:5432/postgres'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:ratestask@localhost:5432/postgres'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
