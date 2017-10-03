from os import path

class authDevelConfig(object):
    # Statement for enabling the development environment
    DEBUG = True
    DEVELOPMENT = False

    PUBLIC_IP = "0.0.0.0"
    BASE_DIR = path.abspath(path.dirname(__file__))

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection against *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    # OAK client id
    OAK_CLIENT_ID = "0oac9gg3kxbIBDjEg0h7"

    # OAK Client secret
    OAK_SECRET = "3CphCmXG-6CT_6xWPjOaUvZchdquT8roE9Ga7DLu"

