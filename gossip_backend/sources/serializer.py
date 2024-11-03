from .models import Users, Discussion, Sources
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'username']
        

class DiscussionSerializer(ModelSerializer):
    class Meta:
        model = Discussion
        fields = ['diss_id', 'summary']

class SourcesSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Sources
        fields = ['source_id', 'text', 'author', 'created']