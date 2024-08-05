from rest_framework.serializers import ModelSerializer
from .models import *

class AllPeopleSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','full_name', 'date_of_birth', 'date_of_death']

class FamilyMediaSerializer(ModelSerializer):
    class Meta:
        model = Family_Media
        fields = "__all__"

class PersImageSerializer(ModelSerializer):
    class Meta:
        model = PersonalImages
        fields = ['image']


class RolesNestedSerializer(ModelSerializer):
    class Meta:
        model = Roles
        fields = ["role", "family"]
class PersonNestedSerializer(ModelSerializer):
    roles = RolesNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ["id",'first_name', 'second_name', 'third_name', 'image', 'gender', 'date_of_birth', 'notfound_birth', 'date_of_death', 'notfound_death', 'description', 'roles']

class PersonDetailSerializer(ModelSerializer):
    family_media = FamilyMediaSerializer(many=True, read_only=True)
    images = PersImageSerializer(many=True, read_only=True)
    roles = RolesNestedSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = '__all__'


class RolesSerializer(ModelSerializer):
    person = PersonDetailSerializer(read_only=True)
    class Meta:
        model = Roles
        fields = ["role", "person", "family"]




class FamilySerializer(ModelSerializer):
    partner = RolesSerializer(many=True, read_only=True)
    class Meta:
        model = Family
        fields = '__all__'