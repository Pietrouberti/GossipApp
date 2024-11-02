# Import necessary packages
from rest_framework.response import Response
from rest_framework import status, views

# Function to store data (currently just returns True)
def store_data(title, description):
    # You can add actual data storage logic here in the future
    return True

# View to handle the send_data endpoint
class SendDataView(views.APIView):
    def post(self, request):
        # Extract title and description from the incoming JSON payload
        title = request.data.get('title')
        description = request.data.get('description')

        # Call the store_data function
        if store_data(title, description):
            # If storing data is successful, return a success status
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            # If there was an error (in future logic), return an error status
            return Response({'status': 'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
