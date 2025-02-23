from rest_framework import generics, permissions, viewsets, status
from .serializers import RestaurantSerializer, HotelSerializer, PlanViajeSerializer
from .models import Restaurant, Hotel, PlanViaje
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

IsEmployeeOrOwner = type(
    "IsEmployeeOrOwner",
    (permissions.BasePermission,),
    {
        "has_permission": lambda self, request, view: request.user and (
            request.user.is_authenticated and 
            (getattr(request.user, "is_employee", False) or getattr(request.user, "is_owner", False))
        )
    }
)
 
class RestaurantsListAPIView (generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantsCreateAPIView (generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsEmployeeOrOwner]


class RestaurantsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsEmployeeOrOwner]


class HotelsListAPIView (generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelsCreateAPIView (generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsEmployeeOrOwner]


class HotelsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsEmployeeOrOwner]

class PlanViajeViewSet(viewsets.ModelViewSet):
    queryset = PlanViaje.objects.all()
    serializer_class = PlanViajeSerializer
    permission_classes = [permissions.IsAuthenticated]  

class PlanViajeUpdateAPIView(APIView):
    def put(self, request, pk):
        plan_viaje = get_object_or_404(PlanViaje, pk=pk)

        serializer = PlanViajeSerializer(plan_viaje, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)