from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Household
from .serializers import HouseholdSerializer

class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer
    permission_classes = [IsAuthenticated]