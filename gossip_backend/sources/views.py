from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, views
from .utils import recieve_msg
from .serializer import UserSerializer, DiscussionSerializer, SourcesSerializer
from .models import Users, Discussion

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

class DiscussionSummariesView(views.APIView):
    def get(self, request):
        try: 
            discussions = Discussion.objects.all()
            serializer = DiscussionSerializer(discussions, many=True)
        except Discussion.DoesNotExist:
            return Response({'error':'Discussion not found'})
        return Response(serializer.data)

class DiscussionSourcesView(views.APIView):
    def get(self, request, diss_id):
        try:
            discussion = Discussion.objects.get(diss_id=diss_id)
        except Discussion.DoesNotExist:
            return Response({'error': 'Discussion not found'}, status=status.HTTP_404_NOT_FOUND)

        sources = discussion.sources.all().order_by('created')
        serializer = SourcesSerializer(sources, many=True)
        return Response(serializer.data)


# Define the view to list users
class ListUsersView(generics.ListAPIView):
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class GetSourcesUserIDView(views.APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        django_username = request.user.username
        
        try:
            # Find the user in Django's User model
            user = Users.objects.get(username=django_username)
            user_id = user.user_id

            # Return the user ID in the response
            return Response(
                {'user_id': user_id},
                status=status.HTTP_200_OK
            )
        except Users.DoesNotExist:
            # Handle the case where the user is not found
            return Response(
                {'error': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
# Create new message endpoint
class CreateMessageView(views.APIView):

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        
        author_id = request.data.get('username')
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
        
