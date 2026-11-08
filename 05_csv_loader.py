
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="employees.csv")

docs = loader.load()

print("Total Rows:", len(docs))

# Print first row
print(docs[0].page_content)
print(docs[0].metadata)

# Print 21st row if available
if len(docs) > 20:
    print(docs[20].page_content)
