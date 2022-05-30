from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

from api.mixins import StaffEditorPermissionMixin


class ProductListAPIView(
    StaffEditorPermissionMixin,
    generics.ListAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, instance):
        title = instance.validated_data.get('title')
        content = instance.validated_data.get('content')

        if content is None:
            content = title
        instance.save(content=content)
        # send a Django signal


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, instance):
        title = instance.validated_data.get('title')
        content = instance.validated_data.get('content')

        if content is None:
            content = title
        instance.save(content=content)


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_list_view = ProductListAPIView.as_view()
product_create_view = ProductCreateAPIView.as_view()
product_detail_view = ProductDetailAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_destroy_view = ProductDestroyAPIView.as_view()


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.create(request, *args, **kwargs)

    def perform_create(self, instance):
        title = instance.validated_data.get('title')
        content = instance.validated_data.get('content')

        if content is None:
            content = title
        instance.save(content=content)


product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid': 'not good data'}, status=400)
