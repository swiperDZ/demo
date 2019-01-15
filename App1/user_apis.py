from django.core.cache import cache
from django.http import JsonResponse

from common import keys

from App1.models import User

from lib.http import rend_json

from common import errors

from lib.sms import send_sms


def number_verification(request):
    """发送短信"""
    phone = request.POST.get("phone")
    send_sms(phone)
    # print(phone)
    return rend_json(None)


def v_code_verification(request):
    """验证码验证，登陆注册"""
    phone = request.POST.get("phone")
    v_code = request.POST.get("Vcode")
    print(phone,v_code)

    cache_v_code = cache.get(keys.VCODE_KEY % phone)

    print(cache_v_code)
    if str(cache_v_code) == str(v_code):
        user, _ = User.objects.get_or_create(u_phone=phone, u_username=phone)

        request.session['uid'] = user.id
        return rend_json(user.to_dict())
    else:
        return rend_json(data="验证码不正确", code=errors.VCODE_ERR)





# def send_sms(request):
#     return
#
#
# def send_sms(request):
#     return