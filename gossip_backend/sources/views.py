from django.shortcuts import render

# Import necessary packages
from rest_framework.response import Response
from rest_framework import status, views
from .utils import store_data

# Create your views here.

# View to handle the send_data endpoint
class SendDataView(views.APIView):
    def post(self, request):
        # Extract title and description from the incoming JSON payload
        text = request.data.get('text')

        # Call the store_data function
        if store_data(text):
            # If storing data is successful, return a success status
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            # If there was an error (in future logic), return an error status
            return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)