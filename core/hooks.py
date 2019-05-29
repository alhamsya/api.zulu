from flask import jsonify


def resp_err(message, error_num=None, err_code=400):
    content = {
        "status": False,
        "message": message,
        "meta": {
            "response_code": err_code,
            "error_code": error_num
        }
    }
    return jsonify(content), err_code


def resp_success(data, message=None, code=200):
    content = {
        "status": True,
        "message": message,
        "data": data
    }
    return jsonify(content), code
