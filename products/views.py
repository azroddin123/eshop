

from django.shortcuts import render

# Create your views here.
from products.models import * 
from products.serializers import * 
from portals.GM2 import GenericMethodsMixin

from portals.services import paginate_data
from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

    
class CategoryAPI(GenericMethodsMixin,APIView):
    model            = Category
    serializer_class = CategorySerializer
    lookup_field     = "id"
    
class ProductAPI(GenericMethodsMixin,APIView):
    model            = Product
    serializer_class = ProductSerializer
    lookup_field     = "id"
    
class GetAllProductsBySubCategoryAPI(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        try : 
            if pk in ["0", None]:
               category = request.GET.get('category')
               if category is None : 
                    data = Product.objects.all()
               else :
                    data = Product.objects.filter(category=category)
               response = paginate_data(Product, ProductSerializer, request,data)
               return Response(response,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : True , "message" : str(e) , "status_code" : 400},status=status.HTTP_400_BAD_REQUEST,)

class ContactUsAPI(GenericMethodsMixin,APIView):
    model            = ContactUs
    serializer_class = ContactSerialzer
    lookup_field     = "id"