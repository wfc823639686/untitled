from django.http import JsonResponse, HttpResponse
from util.utils import ApiResult
from util.utils import WebJsonEncoder

try:
    from django.utils.deprecation import MiddlewareMixin # Django 1.10.x
except ImportError:
    MiddlewareMixin = object # Django 1.4.x - Django 1.9.x


class ApiResultMiddleware(MiddlewareMixin):

    def process_request(self, request):
        return None

    def process_response(self, request, response):
        if isinstance(response, HttpResponse):
            return response
        if isinstance(response, ApiResult):
            return JsonResponse(response, encoder=WebJsonEncoder, safe=False)
        return JsonResponse({'code': 0, 'msg': '', 'data': response}, safe=False)