import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEVELOPER = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbmies',
        'USER': 'dba',
        'PASSWORD': 'dba_2021',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'OPTIONS': {
        'init_command': 'SET default_storage_engine=INNODB'
    }
}

DEVELOPER_AWS = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mies',
        'USER': 'backend',
        'PASSWORD': 'backend',
        'HOST': 'database-mies.cqrwgacibigl.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mies',
        'USER': 'root',
        'PASSWORD':'',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'OPTIONS': {
        'init_command': 'SET default_storage_engine=INNODB'
    }
}

ORACLE = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'entrepreneur',
        'USER': 'admin2021',
        'PASSWORD': 'admin2021**',
        'HOST': 'localhost',
        'PORT': '1540',
    }
}
