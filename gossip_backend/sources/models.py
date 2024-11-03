from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import User

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField()
    # Summary of the user
    summary = models.TextField(null=True, blank=True)
    # Embedding of the summary
    summ_emb = VectorField(dimensions=512, null=True, blank=True)


class Sources(models.Model):
    # The vector field to hold your vector embeddings
    # The text field to hold your text data
    source_id = models.AutoField(primary_key=True)
    # The related_name="sources" option allows you to access all Sources in a Discussion via discussion.sources.
    embedding = VectorField(dimensions=512,  null=True, blank=True)
    text = models.TextField( null=True, blank=True)  
    author = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)  # Allow NULL
    diss_id = models.ForeignKey('Discussion', on_delete=models.CASCADE, related_name="sources")
    created = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

class Discussion(models.Model):
    diss_id = models.AutoField(primary_key=True)
    # sources is made implicitly by the related name before

    summary = models.TextField(null=True, blank=True)
    # embedding of the summary
    
    summ_emb = VectorField(dimensions=512, null=True, blank=True)
    collaborators = models.ManyToManyField(User,  null=True, blank=True)
