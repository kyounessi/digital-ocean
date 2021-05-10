from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

FRONTEND_PORT = 2345

def home(req):
    return render_to_response('templates/home.html', {}, request = req)

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')

        config.add_route('home','/')
        config.add_view(home, route_name = 'home')

        config.add_static_view(name = '/', path = './public', cache_max_age = 3600)

        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', FRONTEND_PORT, app)
        server.serve_forever()