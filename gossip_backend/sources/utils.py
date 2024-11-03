# Embedding model
import tensorflow_hub as hub
import numpy as np
from .models import Sources
from typing import List
from pgvector.django import L2Distance


model_use = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
def embed(text: str) -> np.ndarray:
  """Embeds the given text using the Universal Sentence Encoder.

  Args:
    text: The text to embed.

  Returns:
    The embedding as a NumPy array.
  """
  print("Embedding ...")
  embedding = model_use([text])
  return embedding[0]


def store_source(embedding: np.ndarray, text: str):
    new_entry = Sources(embedding=embedding, text=text)
    new_entry.save()

def get_similar(query: np.ndarray, n: int) -> List[Sources]:
    return Sources.objects.alias(distance=L2Distance('embedding', query)).filter(distance__lt=5)[:n]


def save_source(text:str):
    """ Function abstracts embedding and makes
        Saving a 1 liner
    """
    store_source(embed(text), text)


def query(query: str, n: int) -> List[Sources]:
    """ Searches the database for the n most near neighbours

    This also does some filtering to remove a duplicate from the original query
    """
    query_embedding = embed(query).numpy()
    results = get_similar(query_embedding , n)
    return [source for source in results if not np.array_equal(query_embedding, source.embedding)]
            
