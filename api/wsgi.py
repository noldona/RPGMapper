import os

from api.app import app

if __name__ == '__main__':
    ENVIRONMENT_DEBUG = True if os.environ.get('APP_ENV', 'prod') == 'dev' else False
    ENVIRONMENT_PORT = o.environ.get('APP_PORT', 8080)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
