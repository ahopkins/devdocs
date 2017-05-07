# devdocs

This is a temporary name for a project in active development.

To get started, install a vitrtual environment running Python 3.6. Then install the requirements.

    $ mkvirtualenv devdocs -p /usr/bin/python3.6
    $ pip install -r ./requirements.txt

All **LOCAL** settings should be stored in `backend/config/settings/local.py`. When you clone this repository, this file will **NOT** exist since it is in `.gitignore`. You will need to create it, and store at least the `DATABASES` setting.

    DATABASES = {
        'default': {
            ...
        }
    }

The other file you will need to create is `backend/config/settings/__init__.py` which also is excluded by `.gitignore`. The contents of this file should be:

    from .development import *
