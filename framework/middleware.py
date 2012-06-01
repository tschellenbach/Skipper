
from framework.view_decorators import _process_response, _prepare_request

class ViewDefaultMiddleware(object):
    def process_request(self, request):
        request.ajax = request.is_ajax() or bool(int(request.REQUEST.get('ajax', 0)))
        request.context = None
        request.jinja = True
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        name = view_func.__name__
        app = view_func.__module__.split('.')[0]

        request = _prepare_request(request, name)

        if app:
            request.template = '%s/%s.html' % (app, name)
        else:
            request.template = '%s.html' % name
    
    
class ViewDefaultResponseMiddleware(object):
    def process_response(self, request, response):
        response = _process_response(request, response)
        return response