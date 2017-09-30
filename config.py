import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = b'\x81\xa6mk\x81i\xea\tm\xce}\x06x\x18\xb4\x15q\xd4\xd0\xea<\xf5M7'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
