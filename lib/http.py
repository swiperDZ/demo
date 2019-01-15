import json

from django.http import HttpResponse

from proj import settings


def rend_json(data, code=0):
    result = {
        'data': data,
        'code': code,
    }

    if settings.DEBUG:
        json_data= json.dumps(result, indent=4, sort_keys=True)
    else:
        json_data= json.dumps(result, separators=[';', ':'], ensure_ascii=False)

    return HttpResponse(json_data)