from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.serializers import UserSerializer

# Create your views here.
class ProtectedView(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # print(request.user.first_name)
        # print(request.user.email)
        serializer = UserSerializer(request.user)
        return Response(
            serializer.data
            )
        # return Response({"message": "Online"})