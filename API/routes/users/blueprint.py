from base import reClass
from .schemaRoutes import GraphQl

main = reClass.Blueprint("usersMain", __name__)


@main.route("/users", methods=["GET"])
def shows():
    return f"<h3>{reClass.datetime.datetime.now()}</h3>"

@main.route("/users", methods=["POST"])
def QueryLang():
    data = reClass.request.get_json()
    success, result = reClass.SyncGraphql(
        GraphQl, data, context_value={"request": reClass.request}
    )
    status_code = 200 if success else 400
    return reClass.jsonify(result), status_code
