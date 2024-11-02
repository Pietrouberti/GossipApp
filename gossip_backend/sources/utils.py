# Function to store data (currently just returns True)
def store_data(text: str):
    # You can add actual data storage logic here in the future
    return True

# Embedding model
import tensorflow_hub as hub

def embed(text: str) -> np.ndarray:
  """Embeds the given text using the Universal Sentence Encoder.

  Args:
    text: The text to embed.

  Returns:
    The embedding as a NumPy array.
  """
  model_use = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
  embedding = model_use([text])
  return embedding[0]


from .models import Sources

def store(self, embedding: np.ndarray, text: str):
    new_entry = Sources(embedding=embedding, text=text)
    new_entry.save()
