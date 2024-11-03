from django.shortcuts import render

# Import necessary packages
from rest_framework.response import Response
from rest_framework import status, views
from .utils import store_source, query

# Create your views here.

# View to handle the send_data endpoint
class SendDataView(views.APIView):
    def post(self, request):
        # Extract title and description from the incoming JSON payload
        # text = request.data.get('text')

        # print("got ", text)
        # embedding = embed(text)

        # store_source(embedding, text)

        res = query("Project: Implementing a New Fraud Detection System\nDescription: This project involves developing a sophisticated fraud detection system using machine learning algorithms and real-time data analysis. The ideal candidate should possess expertise in machine learning, data mining, and statistical modeling.  Experience with big data technologies like Hadoop or Spark is a plus.  This project requires the ability to identify patterns, build predictive models, and integrate the system with existing banking infrastructure. Successful completion will reduce financial losses due to fraud and improve security.", 2)
        print(
            [r.text for r in res]
        )

        return '{ "ok": "true" }'
