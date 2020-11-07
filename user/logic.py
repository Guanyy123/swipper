import random

import requests
from django.core.cache import cache

from swipper import config
from worker import call_by_worker


def generate_verify_code(length=6):
    return random.randrange(10 ** (length-1), 10 ** length)

@call_by_worker
def send_verify_code(phone_num):
    '''Send code to the phone'''
    code = generate_verify_code()
    key = 'VerifyCode-%s' % phone_num
    cache.set(key, code, 120) # expire time is 2min

    sms_config = config.HY_SMS_PARAMS.copy()
    sms_config['content'] = sms_config['content'] % code
    sms_config['mobile'] = phone_num
    response = requests.post(config.HY_SMS_URL, data=sms_config)
    return response

