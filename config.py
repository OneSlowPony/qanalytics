from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))
_datadirectory = join(_cwd, "data")
SECRET_KEY = 'weusiej4es6jerioe904yt6swrhdjrhjuiejos8d23eh'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_datadirectory, 'qanalytics_data.db')
SQLALCHEMY_ECHO = True