from django.shortcuts import render
from rest_framework import viewsets



from profile_api import serializers
from profile_api import models
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
