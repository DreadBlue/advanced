from rest_framework import serializers
from .models import Restaurant, Hotel, AdminUser, PlanViaje

class RestaurantSerializer (serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class HotelSerializer (serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

        from rest_framework import serializers

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ["id", "correo", "name", "is_employee", "is_owner", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = AdminUser.objects.create_user(
            correo=validated_data["correo"],
            contrasena=validated_data["password"],
            name=validated_data["name"],
            is_employee=validated_data.get("is_employee", False),
            is_owner=validated_data.get("is_owner", False),
            is_user=validated_data.get("is_user", False),
        )
        return user

class PlanViajeSerializer(serializers.ModelSerializer):
    restaurantes = serializers.PrimaryKeyRelatedField(many=True, queryset=Restaurant.objects.all())
    hoteles = serializers.PrimaryKeyRelatedField(many=True, queryset=Hotel.objects.all())
    user = serializers.StringRelatedField()

    class Meta:
        model = PlanViaje
        fields = "__all__"