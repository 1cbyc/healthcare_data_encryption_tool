# this is how i would create the basic flask application for this project - the ui wont create itself
from app.routes import app

if __name__ == '__main__':
    app.run(debug=True)
