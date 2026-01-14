from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from apps.models import Buyer
from apps.serializers import BuyerSerializer


@extend_schema(tags=['Buyer List'])
class BuyerListAPIView(ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


@extend_schema(tags=['Buyer Create'])
class BuyerCreateAPIView(CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


@extend_schema(tags=['Detail Buyer'])
class DetailBuyerAPIView(RetrieveAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


@extend_schema(tags=['Update Buyer'])
class UpdateBuyerAPIView(UpdateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


@extend_schema(tags=['Delete Buyer'])
class DeleteBuyerAPIView(DestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
