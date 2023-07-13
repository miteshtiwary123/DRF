import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    '''
    DRF API view
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)


