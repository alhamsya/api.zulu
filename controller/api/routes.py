from flask import Blueprint

from core.hooks import resp_err, resp_success
from core.decorators import is_connection
from core.helpers.helper_zulu import get_the_east, get_tonight_show, get_malam

api_bp = Blueprint("api", __name__)


@api_bp.route('<program>/', defaults={'page': 1})
@api_bp.route("<program>/<int:page>", methods=['GET'])
@is_connection
def the_east(program, page):
    result = []
    zulu = []

    list_program = [
        "the-east",
        "tonight-show",
        "malam"
    ]

    if program not in list_program:
        return resp_err("Request wrong", 1, 406)

    for i in range(1, page + 1):
        if program == "the-east":
            temp = get_the_east(i)
        elif program == "tonight-show":
            temp = get_tonight_show(i)
        elif program == "malam":
            temp = get_malam(i)

        for j in temp:
            zulu.append(j)

    for data in zulu:
        url_video = "https://youtube.com/watch/%s" % data.get('youtube')
        url_mobile = "youtube.com/watch?v=%s" % data.get('youtube')
        thumb_url = "https://thumb.zulu.id/?url={}&w=950&h=530".format(data.get('image_cover'))
        content = {
            "episode": data.get('episode_no'),
            "title": data.get('title'),
            "thumb_url": thumb_url,
            "img_url": data.get('image_cover'),
            "url_mobile": url_mobile,
            "url_video": url_video
        }
        result.append(content)

    return resp_success(result)
