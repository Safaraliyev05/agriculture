from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.models import User
from apps.serializers import UserSerializer


@extend_schema(tags=['User List'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['User Create'])
class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['Detail User'])
class DetailUserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['Update User'])
class UpdateUserAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=['Delete User'])
class DeleteUserAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
