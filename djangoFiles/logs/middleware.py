import html2text

from django.utils import timezone

from logs.dbio import AccessLogDbIO


class AccessLogMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.get_full_path()
        if 'admin' in path:
            return self.get_response(request)
        request_data = request.body[0:4900]
        requested_at = timezone.now()
        response = self.get_response(request)
        ip = request.META.get('REMOTE_ADDR')
        method = request.method
        user = None
        if request.user.is_authenticated:
            user = request.user

        response_time = timezone.now() - requested_at
        response_time = response_time.total_seconds() * 1000
        status_code = response.status_code
        try:
            response_data = html2text.html2text(
                response.__dict__['_container'][0])
        except Exception:
            response_data = str(response)[0:4900]
        AccessLogDbIO().create_obj({
            'path': path,
            'method': method,
            'request_data': request_data,
            'created_by': user,
            'response_time': response_time,
            'status_code': status_code,
            'response_data': response_data,
            'ip': ip,
            'user_agent': request.META.get('HTTP_USER_AGENT')[0:90]
        })

        return response