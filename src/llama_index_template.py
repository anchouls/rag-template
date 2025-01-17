from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
import os

from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModelType

PERSIST_DIR = "./storage"
DATA_DIR = "./data"


def initialize_index():
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        embed_model = OpenAIEmbedding(model=OpenAIEmbeddingModelType.TEXT_EMBED_3_SMALL, api_key=os.getenv("OPENAI_API_KEY"))
        index = VectorStoreIndex.from_documents(documents, show_progress=True, embed_model=embed_model)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index

def query_index(index, user_query):
    query_engine = index.as_query_engine()
    return query_engine.query(user_query)
