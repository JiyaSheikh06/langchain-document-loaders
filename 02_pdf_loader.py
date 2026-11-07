
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample_company_handbook.pdf")

docs = loader.load()

print("Total Pages:", len(docs))

# Print first page
print(docs[0].page_content)

# Print metadata
print(docs[0].metadata)

# Print second page if available
if len(docs) > 1:
    print(docs[1].page_content)
