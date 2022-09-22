def app(environ, start_repsonse):
    data = b'Hello world!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_repsonse(status, response_headers)
    return iter([data])