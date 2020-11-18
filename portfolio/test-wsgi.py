import sys
# this was named with a .wsgi extension but trying to call it from the browser to verify the venv

def application(environ, start_response):
    status = '200 OK'

    output = u'Hello World! -- Specifics = '
    output += u'Python module search path: sys.path = %s' % repr(sys.path)
    output += u'sys.version = %s\n' % repr(sys.version)
    output += u'sys.prefix = %s\n' % repr(sys.prefix)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output.encode('UTF-8')]