from core import Fl2 as FlaskApplication
from routes import users, admin, device
app = FlaskApplication()
# * Loads the program SEGMENTS
app.load_blueprint(users.main)
app.load_blueprint(admin.main)
app.load_blueprint(device.main)
# ? This starts the program
app.run()
