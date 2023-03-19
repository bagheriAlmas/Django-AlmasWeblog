from rest_framework import viewsets, permissions, generics
from ..models import CustomUser
from ..serializers import ReporterSerializer


class ReporterListView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=True)
    serializer_class = ReporterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

