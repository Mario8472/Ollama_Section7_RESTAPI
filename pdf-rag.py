# 1. ingest PDF files
# 2. Exract text from PDF files and split into small chunks
# 3. Send the chunks to the embedding model
# 4. Save the embeddings to a vector database
# 5. Perform the similatity search on the vector database to find similar documents
# 6. Retreive the similar documents and present them to the user

from langchain_community.document_loaders import PyPDFLoader    # this is alternative to UnstructuredPDFLoader
#from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/BOI.pdf"
model = "llama3.2:latest"

# Local PDF File uploads
if doc_path:
    #loader = UnstructuredPDFLoader(file_path=doc_path)
    loader = PyPDFLoader(doc_path)
    data = loader.load()
    print("done loading...")
else:
    print("Upload a PDF file")

# Preview first page - just for test
#content = data[0].page_content
#print(content[:100])

# Extract text from PDF and Split into small chunks
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split and chunk
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("done sliptting...")

# test
#print(f"Number of chunks: {len(chunks)}")
#print(f"Example chunk: {chunks[1]}")

# Add to vector database
import ollama
ollama.pull("nomic-embed-text")

# create vector database
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"
)

print("done adding to vector database...")
