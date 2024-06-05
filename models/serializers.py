import django
from rest_framework.serializers import ModelSerializer, Serializer
import models.serializers
from .models import *

class AllPeopleSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','full_name', 'date_of_birth', 'date_of_death']

class FamilyMediaSerializer(ModelSerializer):
    class Meta:
        model = Family_Media
        fields = "__all__"


class RolesNestedSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = ["role", "family"]
class PersonNestedSerializer(ModelSerializer):
    roles = RolesNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = ["id",'first_name', 'second_name', 'third_name', 'image', 'gender', 'date_of_birth', 'date_of_death', 'description', 'roles']


class RolesSerializer(ModelSerializer):
    person = PersonNestedSerializer(read_only=True)
    class Meta:
        model = Roles
        fields = ["role", "person", "family"]


class PersonDetailSerializer(ModelSerializer):
    family_media = FamilyMediaSerializer(many=True, read_only=True)
    roles = RolesNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = '__all__'


class FamilySerializer(ModelSerializer):
    partner = RolesSerializer(many=True, read_only=True)
    class Meta:
        model = Family
        fields = '__all__'