from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextChoices, OneToOneField, CASCADE, ForeignKey, SET_NULL, TextField, \
    DecimalField, PositiveIntegerField, DateTimeField, DateField
from django_prometheus.models import ExportModelOperationsMixin


class User(ExportModelOperationsMixin('user'), AbstractUser):
    class Type(TextChoices):
        FARMER = "FARMER", "Farmer"
        SUPPLIER = "SUPPLIER", "Supplier"
        BUYER = "BUYER", "Buyer"
        DISTRIBUTOR = "DISTRIBUTOR", "Distributor"

    role = CharField(max_length=20, choices=Type.choices)


class Farmer(ExportModelOperationsMixin('farmer'), Model):
    user = OneToOneField("User", CASCADE)
    farm_name = CharField(max_length=255)
    location = CharField(max_length=255)


class Supplier(ExportModelOperationsMixin('supplier'), Model):
    user = OneToOneField("User", CASCADE)
    company_name = CharField(max_length=255)
    location = CharField(max_length=255)


class Buyer(ExportModelOperationsMixin('buyer'), Model):
    user = OneToOneField("User", CASCADE)
    company_name = CharField(max_length=255)
    location = CharField(max_length=255)


class Distributor(ExportModelOperationsMixin('distributor'), Model):
    user = OneToOneField("User", CASCADE)
    company_name = CharField(max_length=255)
    vehicle_number = CharField(max_length=50)


# -------------------------------
# 3. Products
# -------------------------------
class ProductCategory(ExportModelOperationsMixin('product_category'), Model):
    name = CharField(max_length=100)


class Product(ExportModelOperationsMixin('product'), Model):
    name = CharField(max_length=255)
    category = ForeignKey(ProductCategory, on_delete=SET_NULL, null=True)
    farmer = ForeignKey(Farmer, on_delete=CASCADE)  # Produced by farmer
    description = TextField(blank=True)
    price_per_unit = DecimalField(max_digits=10, decimal_places=2)
    quantity_available = PositiveIntegerField()


# -------------------------------
# 4. Orders
# -------------------------------
class Order(ExportModelOperationsMixin('order'), Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]
    buyer = ForeignKey(Buyer, on_delete=CASCADE)
    supplier = ForeignKey(Supplier, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    status = CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    total_amount = DecimalField(max_digits=12, decimal_places=2, default=0)


class OrderItem(ExportModelOperationsMixin('order_item'), Model):
    order = ForeignKey(Order, related_name="items", on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = PositiveIntegerField()
    price = DecimalField(max_digits=10, decimal_places=2)  # price per unit at order time


# -------------------------------
# 5. Delivery
# -------------------------------
class Delivery(ExportModelOperationsMixin('delivery'), Model):
    order = OneToOneField(Order, on_delete=CASCADE)
    distributor = ForeignKey(Distributor, on_delete=CASCADE)
    pickup_date = DateField(null=True, blank=True)
    delivery_date = DateField(null=True, blank=True)
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_TRANSIT", "In Transit"),
        ("DELIVERED", "Delivered"),
    ]
    status = CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")


# -------------------------------
# 6. Payments
# -------------------------------
class Payment(ExportModelOperationsMixin('payment'), Model):
    order = OneToOneField(Order, on_delete=CASCADE)
    paid_amount = DecimalField(max_digits=12, decimal_places=2)
    payment_date = DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]
    status = CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
