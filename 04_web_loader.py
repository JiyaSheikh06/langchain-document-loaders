
from langchain_community.document_loaders import WebBaseLoader

url = "https://python.langchain.com/docs/introduction/"

loader = WebBaseLoader(url)

docs = loader.load()

print("Total Documents:", len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
