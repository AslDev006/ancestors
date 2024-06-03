from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *



class PeopleListView(APIView):
    def get(self, request, format=None):
        service = Person.objects.all()
        serializer = PersonSerializer(service, many=True)
        return Response(serializer.data)


class RolesListView(APIView):
    def get(self, request, format=None):
        service = Roles.objects.all()
        serializer = RolesSerializer(service, many=True)
        return Response(serializer.data)


class FamilyListView(APIView):
    def get(self, request, format=None):
        service = Family.objects.all()
        serializer = FamilySerializer(service, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def FamilyDetailView(request, id):
    try:
        user = get_object_or_404(Family, id=id)
    except Family.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FamilySerializer(user)
        return JsonResponse({
            "success": True,
            "data": serializer.data
        }, status=200)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def PersonDetailView(request, id):
    try:
        user = get_object_or_404(Person, id=id)
    except Person.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonSerializer(user)
        return JsonResponse({
            "success": True,
            "data": serializer.data
        }, status=200)