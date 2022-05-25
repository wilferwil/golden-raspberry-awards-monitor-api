# GRA Monitor API

GRA Monitor API is a Python API for retrieving consecutively awarded movies from Golden Raspberry Awards.

# Requirements

Python version: Python 3.8.10 (default, Mar 15 2022, 12:22:08)

# First steps

'''
python3.8 -m venv .venv
'''

'''
source .venv/bin/activate
'''

'''
pip install -r requirements.txt 
'''

# In-memory database

The application uses an in-memory database, through SQLite in memory mode and utilizes SQLAlchemy as ORM (Object Relational Mapper).

We enabled in-memory SQLite as shown in its documentation:

> The most common way to force an SQLite database to exist purely in memory is to open the database using the special filename ":memory:".

Source: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite

So the SQLAlchemy database URI was configured as ```sqlite:///:memory:```

