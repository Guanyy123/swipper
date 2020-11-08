from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common import error

class AuthMiddleware(MiddlewareMixin):
    '''User Authentation'''
    def process_request(self, request):
        uid = request.session.get('uid')
        if 'uid':
            try:
                request.user = User.objects.get(id=uid)
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, code=error.LOGIN_ERROR)