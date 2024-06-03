import django
from rest_framework.serializers import ModelSerializer, Serializer

import models.serializers
from .models import *

class FamilyMediaSerializer(ModelSerializer):
    class Meta:
        model = Family_Media
        fields = "__all__"


class RolesNestedSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class FamilyNestedSerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"

class PersonNestedSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class RolesSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class PersonSerializer(ModelSerializer):
    family_media = FamilyMediaSerializer(many=True, read_only=True)
    roles = RolesSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = '__all__'


class FamilySerializer(ModelSerializer):
    partner = RolesNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Family
        fields = '__all__'


