import os
import urllib.parse as urlparse
DEBUG = os.environ.get("DEBUG", True)
REALM = os.environ.get('REALM', 'local')

PORT = int(os.environ.get('PORT', 8000))
ROOT_URL = "http://localhost:%s" % (PORT)

ENABLE_CORS = False
CORS_ORIGINS = "*"

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz35")

BIN_TTL = os.environ.get("BIN_TTL", 48)*3600
STORAGE_BACKEND = "requestbin.storage.memory.MemoryStorage"
MAX_RAW_SIZE = int(os.environ.get('MAX_RAW_SIZE', 1024*10))
IGNORE_HEADERS = []
MAX_REQUESTS = int(os.environ.get("MAX_REQUESTS", 20))
CLEANUP_INTERVAL = 3600
MAX_JSON_TO_PRETTYPARSE_IN_BYTES = int(os.environ.get('MAX_JSON_TO_PRETTYPARSE_IN_BYTES', 300*1024))

REDIS_URL = ""
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 9

REDIS_PREFIX = os.environ.get("REDIS_PREFIX", "requestbin")

BUGSNAG_KEY = os.environ.get("BUGSNAG_KEY", "")

if REALM == 'prod':
    DEBUG = os.environ.get("DEBUG", False)
    ROOT_URL = os.environ.get("ROOT_URL", "http://requestb.in")

    FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", FLASK_SESSION_SECRET_KEY)

    STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"

    REDIS_URL = os.environ.get("REDIS_URL")
    url_parts = urlparse.urlparse(REDIS_URL)
    REDIS_HOST = url_parts.hostname
    REDIS_PORT = url_parts.port
    REDIS_PASSWORD = url_parts.password
    REDIS_DB = url_parts.fragment

    BUGSNAG_KEY = os.environ.get("BUGSNAG_KEY", BUGSNAG_KEY)

    IGNORE_HEADERS = """
X-Varnish
X-Forwarded-For
X-Heroku-Dynos-In-Use
X-Request-Start
X-Heroku-Queue-Wait-Time
X-Heroku-Queue-Depth
X-Real-Ip
X-Forwarded-Proto
X-Via
X-Forwarded-Port
""".split("\n")[1:-1]
