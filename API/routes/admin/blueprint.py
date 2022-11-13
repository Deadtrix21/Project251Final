from core.base import reClass
from .schemaRoutes import GraphQl

main = reClass.Blueprint("adminsMain", __name__)


@main.route("/admins", methods=["GET"])
def shows():
    return f"<h3>{reClass.datetime.datetime.now()}</h3>"

@main.route("/admins", methods=["POST"])
def QueryLang():
    data = reClass.request.get_json()
    success, result = reClass.SyncGraphql(
        GraphQl, data, context_value={"request": reClass.request}
    )
    status_code = 200 if success else 400
    response = reClass.jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response , status_code
