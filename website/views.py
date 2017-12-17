from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from rest_framework import status
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
class helloapiview(APIView):
    serializer_class=serializers.helloserializer
    def get(self,request,format=None):
        an_api=['kishan','singh','rathore']
        return Response({'message':'hello','an_api':an_api})
    def post(self,request):
        serializer=serializers.helloserializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})


    def delete(self,request,pk=None):
        return Response({'mothod':'delete'})

class helloviewset(viewsets.ViewSet):
    serializer_class=serializers.helloserializer
    def list(self,request):
        a_viewser=['benhoward','lifhouse','pearljam']
        return Response({'message':'hello','a_viewset':a_viewser})
    def create(self,request):
        serializer=serializers.helloserializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'http_mothod':'GET'})
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})


    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

class userprofileviewset(viewsets.ModelViewSet):
    serializer_class = serializers.userprofileserializer
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateownprofile, )
    filter_backends = (filters.SearchFilter, )
    search_fields=('name','email', )


class loginviewset(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    def create(self,request):
        return ObtainAuthToken().post(request)