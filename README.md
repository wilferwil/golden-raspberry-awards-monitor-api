# GRA Monitor API

GRA Monitor API is a Python API developed on Flask framework for retrieving consecutively awarded movies from Golden Raspberry Awards.

# Pre-Requirements

Python version: Python 3.8.10 (default, Mar 15 2022, 12:22:08)

# First steps to run the API

These are the first steps to run the API locally.

On shell run the following command to create the .venv folder:

<pre><code>python3.8 -m venv .venv</code></pre>

Activate the venv on shell, running this next command:

<pre><code>source .venv/bin/activate</code></pre>

Now that we activated venv, run the following pip command to install the required Python packages:

<pre><code>pip install -r requirements.txt </code></pre>

If you are on a Linux, set flask enviroment variable executing:

<pre><code>export FLASK_APP="app:create_app('config')"</code></pre>

Or if you are on Windows, set the enviroment through this command:

<pre><code>set FLASK_APP="app:create_app('config')"</code></pre>

Now, to start serving the API we just need to execute:

<pre><code>flask run</code></pre>

Integration tests can be run through the command below in the API root directory:

<pre><code>python -m pytest tests/ </code></pre>

# Documentation on Swagger UI (flasgger)

API documentation can be read while the it's being served in a Swagger-like user interface, through this local link below:

[http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

# In-memory database

The application uses an in-memory database, through SQLite in memory mode and utilizes SQLAlchemy as ORM (Object Relational Mapper).

We enabled in-memory SQLite as shown in its documentation:

> The most common way to force an SQLite database to exist purely in memory is to open the database using the special filename ":memory:".

Source: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite

So the SQLAlchemy database URI was configured as ```sqlite:///:memory:```
