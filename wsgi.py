from app import create_app
from app.models import Tweet

application = create_app()

if __name__ == '__main__':
    application.run(debug=True)
