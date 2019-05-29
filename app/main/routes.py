from flask import Blueprint

from core.hooks import resp_err, resp_success

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=['GET'])
def app_info():
    result = {
        "tes": True
    }

    return resp_success(result)
