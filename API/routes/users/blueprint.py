from base import reClass

main = reClass.Blueprint("usersMain", __name__)


@main.route("/users", methods=["GET"])
def shows():
    return f"<h3>{reClass.datetime.datetime.now()}</h3>"

@main.route("/users", methods=["POST"])
def QueryLang():
    return f"<h3>{reClass.datetime.datetime.now()}</h3>"