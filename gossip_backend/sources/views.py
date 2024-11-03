from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, views
from .utils import create_discussion

# Create your views here.

# Login endpoint
class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        print(f"{username} - {password}")

        if user is not None:
            # Generate or get the token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Create new molecule endpoint
class CreateDiscussionView(views.APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def post(self, request):
        # Extract title and description from the incoming JSON payload
        text = request.data.get('text')
        
        
        # Call the store_data function
        if create_discussion(text):
            # If storing data is successful, return a success status
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            # If there was an error (in future logic), return an error status
            return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
