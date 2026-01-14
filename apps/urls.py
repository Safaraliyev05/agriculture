from django.urls import path

from apps.views import UserListAPIView, UserCreateAPIView, DetailUserAPIView, DeleteUserAPIView, \
    FarmerListAPIView, FarmerCreateAPIView, DetailFarmerAPIView, DeleteFarmerAPIView, SupplierListAPIView, \
    SupplierCreateAPIView, DetailSupplierAPIView, UpdateSupplierAPIView, DeleteSupplierAPIView, UpdateFarmerAPIView, \
    UpdateUserAPIView, BuyerListAPIView, BuyerCreateAPIView, DetailBuyerAPIView, UpdateBuyerAPIView, DeleteBuyerAPIView, \
    DistributorCreateAPIView, DistributorListAPIView, DetailDistributorAPIView, UpdateDistributorAPIView, \
    DeleteDistributorAPIView, SignUpAPIView, LoginAPIView, health

urlpatterns = [
    # User URLs
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/detail/<int:pk>/', DetailUserAPIView.as_view(), name='user-detail'),
    path('user/update/<int:pk>/', UpdateUserAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', DeleteUserAPIView.as_view(), name='user-delete'),

    # Farmer URLs
    path('farmers/', FarmerListAPIView.as_view(), name='farmer-list'),
    path('farmer/create/', FarmerCreateAPIView.as_view(), name='farmer-create'),
    path('farmer/detail/<int:pk>/', DetailFarmerAPIView.as_view(), name='farmer-detail'),
    path('farmer/update/<int:pk>/', UpdateFarmerAPIView.as_view(), name='farmer-update'),
    path('farmer/delete/<int:pk>/', DeleteFarmerAPIView.as_view(), name='farmer-delete'),

    # Supplier URLs
    path('suppliers/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier-create'),
    path('supplier/detail/<int:pk>/', DetailSupplierAPIView.as_view(), name='supplier-detail'),
    path('supplier/update/<int:pk>/', UpdateSupplierAPIView.as_view(), name='supplier-update'),
    path('supplier/delete/<int:pk>/', DeleteSupplierAPIView.as_view(), name='supplier-delete'),

    # Buyer URLs
    path('buyers/', BuyerListAPIView.as_view(), name='buyer-list'),
    path('buyer/create/', BuyerCreateAPIView.as_view(), name='buyer-create'),
    path('buyer/detail/<int:pk>/', DetailBuyerAPIView.as_view(), name='buyer-detail'),
    path('buyer/update/<int:pk>/', UpdateBuyerAPIView.as_view(), name='buyer-update'),
    path('buyer/delete/<int:pk>/', DeleteBuyerAPIView.as_view(), name='buyer-delete'),

    # Distributor URLs
    path('distributor-list/', DistributorListAPIView.as_view(), name='distributor-list'),
    path('distributor-create/', DistributorCreateAPIView.as_view(), name='distributor-create'),
    path('distributor-detail/<int:pk>/', DetailDistributorAPIView.as_view(), name='distributor-detail'),
    path('distributor-update/<int:pk>/', UpdateDistributorAPIView.as_view(), name='distributor-update'),
    path('distributor-delete/<int:pk>/', DeleteDistributorAPIView.as_view(), name='distributor-delete'),

    # Auth URLs
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),

    # Health URL's
    path('health/', health, name='health'),
]
