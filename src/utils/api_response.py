from flask import Response
import jsonpickle

def api_response(result):
    response = Response(jsonpickle.encode(result, unpicklable=False))
    response.headers['Content-Type'] = 'application/json'

    return response