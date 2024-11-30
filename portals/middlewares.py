from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
import jwt
from accounts.models import User
from django.conf import settings
# from portals.permissions import IsBusinessOwner, IsAgent, IsClient



class CustomAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/") or request.path.endswith("nt/") or request.path.startswith("/customers") or request.path.startswith("/media") or request.path.startswith("/booking/enquiry") or request.path.startswith("/cars/car-detail") or request.path.startswith("/static") or request.path.startswith("/booking/contact") or request.path.startswith("/booking/blog") or request.path.startswith("/cars/blog") or request.path.startswith("/cars/car-filter") or request.path.startswith("/cars/car-filter1"):
            request.thisUser = None
            response = self.get_response(request)
            return response
        token = request.headers.get('x-access-token')
        if not token:
           return JsonResponse({"message" :"Credentials Not Found ..Please Login"},status=status.HTTP_403_FORBIDDEN)
        try : 
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user = User.objects.filter(mobile_number=payload["mobile_number"]).first()
            request.thisUser = user
            response = self.get_response(request)
            return response    
        except Exception as e :
            return JsonResponse({"message": str(e)}, status=status.HTTP_403_FORBIDDEN)

        



