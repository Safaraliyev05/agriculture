from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField

from .models import (
    User, Farmer, Supplier, Buyer, Distributor,
    ProductCategory, Product, Order, OrderItem,
    Delivery, Payment
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "first_name", "last_name"]


class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Farmer
        fields = ["id", "user", "farm_name", "location"]


class SupplierSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Supplier
        fields = ["id", "user", "company_name", "location"]


class BuyerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Buyer
        fields = ["id", "user", "company_name", "location"]


class DistributorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Distributor
        fields = ["id", "user", "company_name", "vehicle_number"]


class SignUpSerializer(serializers.Serializer):
    email = EmailField(max_length=255)
    username = CharField(max_length=150)
    password = CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=True
        )


class LoginSerializer(serializers.Serializer):
    email = EmailField(max_length=255)
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Login or password incorrect")

        if not user.check_password(password):
            raise ValidationError("Login or password incorrect")

        attrs['user'] = user
        return attrs


# -------------------------------
# 3. Product Serializers
# -------------------------------
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(read_only=True)
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "farmer", "description", "price_per_unit", "quantity_available"]


# -------------------------------
# 4. Order Serializers
# -------------------------------
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "buyer", "supplier", "created_at", "status", "total_amount", "items"]


# -------------------------------
# 5. Delivery Serializer
# -------------------------------
class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    distributor = DistributorSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = ["id", "order", "distributor", "pickup_date", "delivery_date", "status"]


# -------------------------------
# 6. Payment Serializer
# -------------------------------
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "order", "paid_amount", "payment_date", "status"]
