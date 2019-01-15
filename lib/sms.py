from random import randrange

import requests
from django.core.cache import cache

from proj import config

from common import keys

def v_code(length=6):
    start_num = 10 ** (length - 1)
    end_num = 10 ** length
    result = randrange(start_num, end_num)
    return result


def send_sms(phone):
    VCode = v_code()
    # print(VCode)
    sms_api = config.YZX_SMS_API
    sms_params = config.YZX_SMS_PARAMS.copy()
    sms_params['mobile'] = phone
    sms_params['param'] = VCode
    print(phone, VCode)

    # 讲验证码缓存到cache中
    cache.set(keys.VCODE_KEY % phone, VCode, timeout=600)
    # 状态判断
    resp = requests.post(sms_api, json=sms_params)
    if resp.status_code == 200:
        result = resp.json()
        # print(result)
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return '短信服务器忙'


