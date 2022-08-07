from core import Fl2 as FlaskApplication
from routes import index, users

app = FlaskApplication()


# * Loads the program SEGMENTS
app.load_blueprint(index.main)
app.load_blueprint(users.main)

# ? This starts the program
app.run()
