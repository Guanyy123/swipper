import json

from django.conf import settings
from django.http import HttpResponse

def render_json(data, code):
    result = {
        'code': code,
        'data': data
    }
    if settings.Debug:
        json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = json.dumps(result, ensure_ascii=True, separators=[',', ':'])
    return HttpResponse(json_str)
