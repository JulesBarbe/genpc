import openai
import qdrant_client
import enhancer
import os
from config import settings
from qdrant_client.http.models import Batch
from langchain_openai import OpenAIEmbeddings

def init():
  pass

embeddings = OpenAIEmbeddings(api_key=settings.open_api_key)
# enhancer_chain = enhancer.chain()
qdrant_client = qdrant_client.QdrantClient()
# vec_store = Qdrant(
#     client=client, collection_name="texts", 
#     embeddings=embeddings,
# )



# Add text (or text file) to vector store
def process_text(text):
  pass
# Create docs from keywords and return to user before adding to vector store
def enhance_text(keyw):
  pass


#TODO: Query