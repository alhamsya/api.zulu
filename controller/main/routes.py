from datetime import datetime

from flask import Blueprint

from core.hooks import resp_err, resp_success

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=['GET'])
def app_info():

    local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = {
        "local_time": local_time
    }

    return resp_success(result)
