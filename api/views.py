from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()

    print(request.GET)

    data = {}
    # try:
    #     data = json.loads(request.body)
    # except:
    #     pass
    # print(data)
    if instance:
        data = ProductSerializer(instance).data
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # data['params'] = dict(request.GET)

    return Response(data)
