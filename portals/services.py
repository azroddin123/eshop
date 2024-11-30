import jwt
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def generate_token(mobile_number):
    payload = {
        "mobile_number" :mobile_number
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


def user_verification_email(mail, otp):
    subject = "Vecto Password  Reset OTP "
    msg = "Your one time password for resetting the password at <strong> Vecto </strong> is as follows: <strong>{}</strong> <br>\nPlease do not share this with anyone.".format(otp)
    # Create an EmailMultiAlternatives object to support HTML content 
    email = EmailMultiAlternatives(subject, msg, '33azharoddin@gmail.com', [mail])
    email.attach_alternative(msg, "text/html")  # Specify HTML content type
    
    try:
        res = email.send()
        if res == 1:
            msg = 1
        else:
            print("no")
            msg = 0
    except Exception as e:
        print(e)
        msg = 0
    
    return msg


from django.core.paginator import Paginator, EmptyPage
def paginate_model_data(model, serializer, request, filter_key=None):
    try:
        limit = max(int(request.GET.get('limit', 0)), 1)
        page_number = max(int(request.GET.get('page', 0)), 1)
        if filter_key:
            filter_value = request.GET.get(filter_key)
            data = model.objects.filter(**{filter_key: filter_value})
        else:
            data = model.objects.all()
        paginator = Paginator(data, limit)
        try:
            current_page_data = paginator.get_page(page_number)
        except EmptyPage:
             return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        serialized_data = serializer(current_page_data, many=True).data
        response_data = {
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serialized_data
        }
        return response_data
    except Exception as e:
        return Response({"error": True, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Q
def paginate_data(model, serializer, request,data):
    try:
        limit = int(request.GET.get('limit', 1))
        page_number = int(request.GET.get('page', 1))
        search   = request.GET.get('search')
        data = data
        if search:
                q_objects = Q()
                for field in model._meta.fields:
                    if not field.is_relation:
                        q_objects |= Q(**{f"{field.name}__icontains": search})
                    elif hasattr(field, 'related_model'):
                        related_model = field.related_model
                        if related_model:
                            for related_field in related_model._meta.fields:
                                if not related_field.is_relation:
                                    q_objects |= Q(**{f"{field.name}__{related_field.name}__icontains": search})
                data = model.objects.filter(q_objects)  
        else :   
                data = data
        paginator = Paginator(data, limit)
        try:
            current_page_data = paginator.get_page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serialized_data = serializer(current_page_data, many=True).data
        except Exception as e:
            return Response({"error": True, "message": f"Serialization error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        response_data = {
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serialized_data
        }
        return response_data
    except Exception as e:
        return Response({"error": True, "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    