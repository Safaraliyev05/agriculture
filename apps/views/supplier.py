from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from apps.models import Supplier
from apps.serializers import SupplierSerializer


@extend_schema(tags=['Supplier List'])
class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


@extend_schema(tags=['Supplier Create'])
class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


@extend_schema(tags=['Detail Supplier'])
class DetailSupplierAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


@extend_schema(tags=['Update Supplier'])
class UpdateSupplierAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


@extend_schema(tags=['Delete Supplier'])
class DeleteSupplierAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
