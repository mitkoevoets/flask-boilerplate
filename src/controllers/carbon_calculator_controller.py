from flask import request, Response
from src.utils import api_response


def run():
    body = request.get_json()

    return api_response(body)
