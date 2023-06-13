from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .filters import AdvertisementFilter
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = []
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
             permission_classes = [AllowAny]
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
