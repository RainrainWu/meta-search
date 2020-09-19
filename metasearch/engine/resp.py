import json

def build_status(status_code, message):
    body = {
        "status_code": status_code,
        "message": message
    }
    return body

def build_hateoas(links, status, data = None, embedded = None):
    body = {
        "_links": links,
        "status": status,
        "data": data,
        "embedded": embedded
    }
    return body