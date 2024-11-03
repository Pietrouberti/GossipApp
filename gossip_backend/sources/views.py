from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, views
from .utils import recieve_msg
from .serializer import UserSerializer
from .models import User

# Create your views here.

# Login endpoint
class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate or get the token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
# Define the view to list users
class ListUsersView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
# Create new message endpoint
class CreateMessageView(views.APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        author_id = request.user.id
        print("\n \n ", request.data)
        if 'discussion' in request.data:
            
            discussion_id = request.data.get('discussion')
            text = request.data.get('text')
            
            if recieve_msg(text=text, user_id=author_id, discussion_id=discussion_id):
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # TODO: Manage priority
            priority = request.data.get('priority')
            collaborators = request.data.get('collaborators')
            text = request.data.get('text')
            
            if recieve_msg(text=text, user_id=author_id, collaborators=collaborators):
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GetDiscussionsView(views.APIView):
    pass
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def request(self, request):
    """
        