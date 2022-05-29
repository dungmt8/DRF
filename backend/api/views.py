from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    """
    DRF Api View
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    instance = Product.objects.all().order_by("?").first()

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not got data"}, status=400)

    # data = {}
    # if instance:
    #     # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    #     data = ProductSerializer(instance).data
    #
    #
    #
    # return Response(data)