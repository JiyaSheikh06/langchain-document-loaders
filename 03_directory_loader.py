
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# Load all documents at once
docs = loader.load()

print("Total Pages:", len(docs))

for doc in docs:
    print(doc.metadata)


# docs = loader.lazy_load()

# for doc in docs:
#     print(doc.metadata)