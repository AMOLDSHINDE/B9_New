from django.shortcuts import render

# Create your views here.
from app1.serializers import EmployeeSerializer
from app1.models import Employee
from rest_framework import viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import  IsAuthenticated,AllowAny

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [BasicAuthentication]
    authentication_classes = [AllowAny]

    authentication_classes = [BasicAuthentication]    #pass the username and password
    permission_classes = [IsAuthenticated]                   #and postman got to Authorization and seletct type basicAuthentication pass the username and password

    @action(detail=False, methods=['post'])
    def obtain_token(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(token_data, status=status.HTTP_200_OK)