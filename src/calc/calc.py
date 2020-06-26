from cgi import parse_qs
from template import html


def application(environ, start_response):
    status = '200 OK'
    inputs = parse_qs(environ['QUERY_STRING'])
    a = inputs.get('a', [''])[0]
    b = inputs.get('b', [''])[0]
    sum, mul = 0, 0
    result = "False"
    if '' not in [a, b]:
        a, b = int(a), int(b)
        sum = a + b
        mul = a * b
        result = "True"
    response_body = (
        html % {'result': result, 'sum': sum, 'mul': mul}).encode()

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]
