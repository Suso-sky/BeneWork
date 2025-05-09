import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Verificar credenciales con el User Service
        response = requests.post(
            "http://localhost:8000/api/users/verify/",
            json={"email": email, "password": password}
        )

        if response.status_code == 200 and response.json().get("valid"):
            return Response({"token": "mock_token_12345"}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
