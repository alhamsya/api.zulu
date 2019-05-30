from flask import Blueprint

from core.hooks import resp_err, resp_success
from core.utils import get_now

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=['GET'])
def app_info():
    result = {
        "local_time": get_now('ID')
    }

    return resp_success(result)
