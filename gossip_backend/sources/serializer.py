from .models import Users
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'username']