SQLAlchemy-UTCDateTime
============================================

Installation
++++++++++++

  pip install sqlalchemy-utcdatetime

Sample Usage
++++++++++++

.. code-block:: python

  import sqlalchemy as sa
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy_utcdatetime import UTCDateTime
  import datetime, pytz

  Base = declarative_base()

  class MyModel(Base):
      __tablename__ = 'my_model'
      
      id = sa.Column(sa.Integer(), primary_key=True)
      my_datetime = sa.Column(UTCDateTime())


  m = MyModel()
  m.my_datetime = datetime.datetime.now(pytz.timezone('Australia/Sydney'))

