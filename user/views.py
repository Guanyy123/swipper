from django.shortcuts import render

from user.logic import send_verify_code


def get_verify_code(request):
    ''''Phone registeration'''
    phone_num = request.GET.get('phone')
    send_verify_code(phone_num)


def login(request):
    '''Text verify login'''
    # code = cache.get(key)

def get_profile(request):
    pass
def update_profile(request):
    pass
def upload_avatar(request):
    pass