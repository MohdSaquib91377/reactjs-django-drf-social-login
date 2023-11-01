import requests 


from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import *
from rest_framework import generics
from accounts.models import Account
class CreateAccount(APIView):
   permission_classes=[permissions.AllowAny]

   def post(self,request):
       reg_serializer=RegistrationSerializer(data=request.data)
       if reg_serializer.is_valid():
           new_user=reg_serializer.save()
           if new_user:
              #add these
               r=requests.post('http://127.0.0.1:8000/api-auth/token', data = {
                   'username':new_user.email,
                   'password':request.data['password'],
                   'client_id':'SD0K0F3VLxArI9sUg5WJ2WwksITcLxJJi60Vh4eu',
                   'client_secret':'8oTM7oZ56qo9bee8aCeKj24VC57jbmF9CGr8KPRncrt0hrAac2ktvrvgEfNSC9qrUoiyJfNbEFf7NErSo8cBjRcmQI7ji6RbmQQJALj3dxBnYZ2HK1OWfWtqXP0j3hrb',
                   'grant_type':'password'
               })
               return Response(r.json(),status=status.HTTP_201_CREATED)
       return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AllUsers(generics.ListAPIView):
   permission_classes=[permissions.AllowAny]
   queryset=Account.objects.all()
   serializer_class=UsersSerializer

class CurrentUser(APIView):
   permission_classes = (permissions.IsAuthenticated,)
   def get(self, request):
       serializer = UsersSerializer(self.request.user)
       return Response(serializer.data)