from django.db import models
from pgvector.django import VectorField

class Sources(models.Model):
    # The vector field to hold your vector embeddings
    embedding = VectorField(dimensions=512)  # Set the appropriate dimensions for your use case
    # The text field to hold your text data
    text = models.TextField()  

    def __str__(self):
        return self.text_data  # or however you want to represent the object
