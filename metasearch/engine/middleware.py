class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('---- One-time configuration and initialization. ----')
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('---- 1 ----')
        response = self.get_response(request)
        print('---- 4 ----')

        # Code to be executed for each request/response after
        # the view is called.

        return response


    # process_view(), process_exception(), process_template_response()
    # special methods to class-based middleware

    def process_view(self, request, view_func, view_args, view_kwargs):
        # process_view() is called just before Django calls the view.
        # It should return either None or an HttpResponse object
        print('---- 2 ----')
        return None

    def process_exception(self, request, exception):
        # Django calls process_exception() when a view raises an exception
        # It should return either None or an HttpResponse object
        print('---- exception.args ----')
        return None

    def process_template_response(self, request, response):
        # return TemplateResponse object
        print('---- 3 ----')
        return response