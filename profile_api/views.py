from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly



from profile_api import serializers
from profile_api import models
from profile_api import permissions
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)



class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedItemViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSeializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticatedOrReadOnly)


    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
