

import os

BASE_DIR = os.path.dirname(__file__)
print(f'__file__:{__file__}')
print(f'BASE_DIR:{BASE_DIR}')


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"