from apps.views.user import UserListAPIView, UserCreateAPIView, DetailUserAPIView, UpdateUserAPIView, DeleteUserAPIView
from apps.views.farmer import FarmerListAPIView, FarmerCreateAPIView, DetailFarmerAPIView, UpdateFarmerAPIView, \
    DeleteFarmerAPIView
from apps.views.buyer import BuyerListAPIView, BuyerCreateAPIView, DetailBuyerAPIView, UpdateBuyerAPIView, \
    DeleteBuyerAPIView
from apps.views.distributor import DistributorListAPIView, DistributorCreateAPIView, DetailDistributorAPIView, \
    UpdateDistributorAPIView, DeleteDistributorAPIView
from apps.views.supplier import SupplierListAPIView, SupplierCreateAPIView, DetailSupplierAPIView, \
    UpdateSupplierAPIView, DeleteSupplierAPIView
from apps.views.auth import SignUpAPIView, LoginAPIView
from apps.views.health import health