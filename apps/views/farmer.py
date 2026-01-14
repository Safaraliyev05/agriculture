from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import Farmer
from apps.permissions import IsFarmer
from apps.serializers import FarmerSerializer


@extend_schema(tags=['Farmer List'])
class FarmerListAPIView(ListAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsFarmer]


@extend_schema(tags=['Farmer Create'])
class FarmerCreateAPIView(CreateAPIView):
    model = Farmer
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsFarmer]


@extend_schema(tags=['Detail Farmer'])
class DetailFarmerAPIView(RetrieveAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsFarmer]


@extend_schema(tags=['Update Farmer'])
class UpdateFarmerAPIView(UpdateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsFarmer]


@extend_schema(tags=['Delete Farmer'])
class DeleteFarmerAPIView(DestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated, IsFarmer]
