import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'README.rst',
)
long_description = open(readme_path).read()
version_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'VERSION',
)
version = open(version_path).read()

setup(
  name='SQLAlchemy-UTCDateTime',
  version=version,
  modules=['sqlalchemy_utcdatetime'],
  author="Nick Whyte",
  author_email='nick@nickwhyte.com',
  description="Convert to/from timezone aware datetimes when storing in a DBMS",
  long_description=long_description,
  url='https://github.com/nickw444/SQLAlchemy-UTCDateTime',
  zip_safe=False,
  install_requires=[
        "sqlalchemy",
        "pytz",
  ],
  classifiers=[
    'Intended Audience :: Developers',
    'Programming Language :: Python',
  ],
)
