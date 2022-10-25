from base import reClass

main = reClass.Blueprint("IndexMain", __name__)


@main.route("/", methods=["GET", "POST"])
def shows():
    return f"<h3>{reClass.datetime.datetime.now()}</h3>"
