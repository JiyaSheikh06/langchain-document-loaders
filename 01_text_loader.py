
from langchain_community.document_loaders import TextLoader

loader = TextLoader("company_policy.txt", encoding="utf-8")

docs = loader.load()

print("Total Documents:", len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
