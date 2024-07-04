from rest_framework import serializers
from .models import Territory, Organization, Building


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

