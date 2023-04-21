import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-random-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NEWSCATCHER_API_KEY = 'bGKlOygnb-efR7oP01LBTC2flS7xZ3Cjzm1JgDYSNVs'
    RAPIDAPI_KEY = '210763df38msh07fbd1b41b83d8bp1e9624jsnf40268a5c904'

