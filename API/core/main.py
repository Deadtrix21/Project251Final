from yachalk import chalk

from base import reClass


class Fl2:
    def __init__(self):
        self.flask = reClass().Flask(__name__)

    def database():
        return "database"

    def OnError(self, text):
        return chalk.bg_red_bright(text)

    def OnContinue(self, text):
        return chalk.bg_green_bright(text)

    def OnStart(self, text):
        return chalk.bg_blue_bright(text)

    #! Load a split class
    def load_blueprint(self, blueprint: reClass.Blueprint):
        print(f"Loading sequence for {blueprint.name} has {self.OnStart('Started')}")
        try:
            self.flask.register_blueprint(blueprint)
            print(
                f"Loading sequence for {blueprint.name} has {self.OnContinue('Loaded')}"
            )
        except Exception as ErrorOccurrence:
            print(f"Loading sequence for {blueprint.name} has {self.OnError('Failed')}")
            print(ErrorOccurrence)

    #! This is the boot functions
    def __beginProgram(self):
        self.flask.run()

    def boot(self):
        self.__beginProgram()

    def start(self):
        self.__beginProgram()

    def run(self):
        self.__beginProgram()
