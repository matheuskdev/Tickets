from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    name = 'user_registration'
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny,]


class UserProfileView(generics.RetrieveAPIView):
    name='user_profile'
    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(username=kwargs['username'])
        user_serializer = UserSerializer(user)
        #tickets = Ticket.objects.filter(user=user)
        #tickets_serializer = PinUserSerializer(tickets, many=True)
        return Response({
            'user': user_serializer.data,
            #'pins': tickets_serializer.data
        })