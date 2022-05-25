# Instantiate SQLite as an in-memory database
# https://www.sqlite.org/inmemorydb.html
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_TRACK_MODIFICATIONS = False