from django.core.cache import cache
import string
import random
from .utils import send_otp


class ServiceOtp:

    @staticmethod
    def generate_code():
        digits = string.digits
        return "".join(random.choice(digits) for _ in range(6))
    
    @staticmethod
    def generate_otp(user):
        code = ServiceOtp.generate_code()
        print(f"=============== Code Verify : {code} =============")
        otp = cache.set(f"otp_{user}",code,timeout=120)
        send_otp(user,code)
        return otp
    
    @staticmethod
    def verify_otp(user,code):
        otp = cache.get(f"otp_{user}")
        if otp and int(otp) == code:
            cache.delete(otp)
            return True
        else:
            return False
    
    @staticmethod
    def resend_otp(user):
        otp = cache.get(f"otp_{user}")
        if otp:
            cache.delete(otp)
        ServiceOtp.generate_otp(user)
        return "Code Resens"
        
        
            