from llama_index.core import (
    VectorStoreIndex, SimpleDirectoryReader, Settings,StorageContext, load_index_from_storage
)
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
import os.path

# définition du modèle de plongement vectoriel à utiliser
Settings.embed_model = resolve_embed_model("local:BAAI/bge-m3")

# définition du LLM à utiliser
Settings.llm = Ollama(model="llama3:8b", request_timeout=300.0)

# définition du répertoire de stockage de l'index
DOSSIER_STOCKAGE_INDEX = "./index"

# si l'index n'existe pas, on le crée
if not os.path.exists(DOSSIER_STOCKAGE_INDEX):

    # chargement des documents préalablement stockés dans le dossier data
    documents = SimpleDirectoryReader("data").load_data()

    # création de l'index
    index = VectorStoreIndex.from_documents(documents,)

    # stockage de l'index
    index.storage_context.persist(persist_dir=DOSSIER_STOCKAGE_INDEX)

# sinon, on le charge
else:
    # chargement de l'index s'il existe
    storage_context = StorageContext.from_defaults(persist_dir=DOSSIER_STOCKAGE_INDEX)
    index = load_index_from_storage(storage_context)

# utilisation de l'index pour effectuer une requête
query_engine = index.as_query_engine()
response = query_engine.query("Qui est Sam Altman ?")
print(response)




