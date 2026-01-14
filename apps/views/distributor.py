from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from apps.models import Distributor
from apps.serializers import DistributorSerializer


@extend_schema(tags=['Distributor List'])
class DistributorListAPIView(ListAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


@extend_schema(tags=['Distributor Create'])
class DistributorCreateAPIView(CreateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


@extend_schema(tags=['Detail Distributor'])
class DetailDistributorAPIView(RetrieveAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


@extend_schema(tags=['Update Distributor'])
class UpdateDistributorAPIView(UpdateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer


@extend_schema(tags=['Delete Distributor'])
class DeleteDistributorAPIView(DestroyAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
