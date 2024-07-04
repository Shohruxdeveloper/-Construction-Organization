from .models import Territory, Organization, Building
from .serializers import TerritorySerializer, OrganizationSerializer, BuildingSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import CustomPermission


class TerritoryView(ModelViewSet):
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        return Territory.objects.all()


class OrganizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        return Organization.objects.all()


class BuildingView(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        return BuildingView.objects.all()