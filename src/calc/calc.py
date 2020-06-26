from cgi import parse_qs
from template import html


def application(environ, start_response):
    status = '200 OK'
    inputs = parse_qs(environ['QUERY_STRING'])
    a = inputs.get('a', [''])[0]
    b = inputs.get('b', [''])[0]

    if '' not in [a, b]:
        a, b = int(a), int(b)
        result = str(a + b) + " and " + str(a * b) + \
            '<a href="/homework-20203070"> return </a>'
        response_body = result
    else:
        response_body = html

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]
