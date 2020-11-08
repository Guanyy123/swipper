import json

from django.http import HttpResponse

from common import error
from user.logic import send_verify_code, check_code
from lib.http import render_json
from user.models import User, Profile

def get_verify_code(request):
    ''''Phone registeration'''
    phone_num = request.GET.get('phone')
    send_verify_code(phone_num)
    return render_json(None, 0)

def login(request):
    '''Text verify login'''
    phone_num = request.POST.get('phone')
    code = request.POST.get('code')
    if check_code(phone_num, code):
        # get User
        user, created = User.objects.get_or_create(phone=phone_num)
        # save user status
        request.session['uid'] = user.id
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, error.CODE_ERROR)

def get_profile(request):
    user = request.user
    return render_json(user.profile.to_dict())

def update_profile(request):
    pass
def upload_avatar(request):
    pass