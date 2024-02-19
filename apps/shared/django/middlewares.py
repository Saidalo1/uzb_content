from django.utils.translation import activate


class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_prefix = request.LANGUAGE_CODE

        activate(language_prefix)

        response = self.get_response(request)

        return response
