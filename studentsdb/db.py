import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
	 # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'studentsdb.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'l;buehlf',
        'NAME': 'students_db',
    }
}