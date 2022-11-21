from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]