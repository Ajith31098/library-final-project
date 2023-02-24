from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserAprovalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets
from user_app.models import MemberShip, User

# Create your views here.


class Registration_view(APIView):
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['notification'] = 'Successfully Registered ,Waiting for Approval of Librarian'
        return Response(data, status=status.HTTP_200_OK)


class Aproval_view(viewsets.ModelViewSet):

    queryset = MemberShip.objects.all()
    serializer_class = UserAprovalSerializer

    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    # to specify whether one or more object showen
    @action(detail=True, methods=['put'])
    def set_aproval(self, request, pk=None):
        member = MemberShip.objects.get(pk=pk)
        if member.aproval == MemberShip.Register.REGISTER:
            return Response({'Note': 'approval is already given to this user'})
        if member.aproval == MemberShip.Register.CANCEL:
            return Response({'Note': 'approval is denied for this user'})
        member.aproval = MemberShip.Register.REGISTER
        member.save()
        newuser = User(username=member.username,
                       email=member.email, usertype=User.UserType.MEMBER)
        newuser.set_password(member.password)
        newuser.save()
        return Response({member.username: 'is added to the user model'})


class Logout_view(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'Logout': 'Successfull'}, status=status.HTTP_200_OK)
