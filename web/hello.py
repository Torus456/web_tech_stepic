def app(environ, start_repsonse):
    data = '\r\n'.join(environ['QUERY_STRING'].split('&'))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_repsonse(status, response_headers)
    return [bytes(data)]