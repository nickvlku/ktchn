from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .permissions import IsAuthenticatedOrCreate

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrCreate]