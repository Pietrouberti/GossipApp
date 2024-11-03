# Embedding model
import tensorflow_hub as hub
import numpy as np
from .models import Sources, Users, Discussion
from typing import List
from pgvector.django import L2Distance

''' Hitting endpoint CreateMessageView with payload
{'text': 'fsdf', 'priority': '2', 'collaborators': ['fsdfsd']}'''

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

def recieve_msg(text: str, user_id:int, diss_id=None, collaborators=None) -> int:
    """ Function manages receiving a message

    Returns:
       the discussion id it was added to 
    """
    if is_relevant(text, diss_id):
        diss_id = create_source(text, user_id, diss_id, collaborators)
        update_user(user_id)
    else:
      # TODO: handle this
      pass

    return diss_id
    
# --------- LLM -------------

def is_relevant(text: str, diss_id: int) -> bool:
    """ Handles deciding a message relevancy
        depending on its context if it has any
    """
    return True # for now

def summarize(text: str) -> str:
  # AI magic
  # TODO: OLI your job
  return sum

# ---------- Discussions ---

def update_discussions(diss_id: int) -> int:
  discussion = Discussion.objects.get(diss_id=diss_id)
  sources = discussion.sources
  history = " ".join(source.text for source in sources)
  discussion.summary = summarize(history)
  discussion.save()
  return diss_id
  
def create_discussion(collaborators: List[int], base_id=None):
  if base_id is not None:
    source = Sources.objects.get(source_id=base_id)
    summary = summarize(source.text)
    discussion = Discussion(base_id=base_id, summary=summary, summ_emb=embed(summary))
    discussion.collaborators.set(collaborators)
  else:
    # no summ or embedding
    discussion = Discussion(base_id=base_id)
    discussion.collaborators.set(collaborators)

  return discussion.diss_id
  

# ---------- Users ---------

def update_user(user_id: int):
  # Get all the sources of this user
  # NOTE: user must exist
  sources = Sources.objects.filter(user_id=user_id)
  history = " ".join(source.text for source in sources)
  user = Users.objects.get(user_id=user_id)
  user.summary = summarize(history)
  user.save()
    
# -------- Sources ---------

def store_source(embedding: np.ndarray, text: str, diss_id: int, user_id: int):
    # get is used for a single discussion
    discussion = Discussion.objects.get(diss_id=diss_id)
    author = Users.objects.get(user_id=user_id)
    # Create and save a new Sources entry
    new_entry = Sources(
      embedding=embedding, 
      text=text, 
      diss_id=discussion, 
      author=author
    )
    new_entry.save()

    return new_entry.source_id

def create_source(text:str, user_id: int, diss_id=None, collaborators=None):
    """ Function abstracts embedding and makes
        creating 
    """
    # Handle if a Discussion does not exist
    if diss_id is not None:
      # Discussion exists
      store_source(embed(text), text, diss_id, user_id)
      update_discussion(diss_id)

    elif collaborators is not None:
      # create a discussion
      diss_id = create_discussion(collaborators)

      # store the source with its diss id
      source_id = store_source(embed(text), text, diss_id, user_id)

      # update the discussion
      update_discussions(diss_id)

    else:
      print("no collaborators or id")

    
    return source_id

# -------------------------

def query(query: str, n: int) -> List[Sources]:
    """ Searches the database for the n most near neighbours

    This also does some filtering to remove a duplicate from the original query
    """
    query_embedding = embed(query).numpy()
    results = get_similar(query_embedding , n)
    return [source for source in results if not np.array_equal(query_embedding, source.embedding)]
            
def get_similar(query: np.ndarray, n: int) -> List[Sources]:
    return Sources.objects.alias(distance=L2Distance('embedding', query)).filter(distance__lt=5)[:n]

