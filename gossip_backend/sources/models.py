from django.db import models
from pgvector.django import VectorField

class Sources(models.Model):
    # The vector field to hold your vector embeddings
    embedding = VectorField(dimensions=512)  # Set the appropriate dimensions for your use case
    # The text field to hold your text data
    text = models.TextField()  

    author = VectorField(dimensions=512)     # Embedding for the author
    created = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

    def __str__(self):
        return self.text_data  # or however you want to represent the object

# Discussion
# - members
# - list of messages (sources)
