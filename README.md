# LangChain Document Loaders

A hands-on collection of Python examples demonstrating different Document Loaders in LangChain.

Document Loaders are an important part of LangChain. They help load data from different sources and convert it into a standardized format called `Document`, which can be used in LLM applications and Retrieval-Augmented Generation (RAG) systems.

## 📚 What are Document Loaders?

Document Loaders are components in LangChain that load data from different sources, such as text files, PDFs, websites, and CSV files.

They convert the extracted information into LangChain `Document` objects.

Each Document object contains two main attributes:

- **page_content:** Contains the actual text extracted from the source.
- **metadata:** Contains additional information about the document, such as its source, page number, or other relevant details.


## 📂 Document Loaders Covered

### 1. TextLoader

`TextLoader` is used to load plain text files (`.txt`).

It reads the text content from a file and converts it into a LangChain Document object.

### 2. PyPDFLoader

`PyPDFLoader` is used to extract text from PDF documents.

It generally creates a separate Document object for each page of the PDF. Each page also contains metadata, including its source and page number.

### 3. DirectoryLoader

`DirectoryLoader` is used to load multiple files from a directory instead of loading them individually.

It uses a specified loader class to process files. For example, `PyPDFLoader` can be used to load multiple PDF files from a folder.

**Important Parameters:**

- `path`: Specifies the directory containing files.
- `glob`: Specifies which files to load, such as `*.pdf`.
- `loader_cls`: Defines which document loader should process the files.

### 4. WebBaseLoader

`WebBaseLoader` is used to extract content from web pages.

It fetches webpage content and uses HTML parsing to extract information, which is then converted into a Document object.

### 5. CSVLoader

`CSVLoader` is used to load data from CSV files.

It converts each row of a CSV file into a separate Document object. The row's content is stored in `page_content`, while metadata can include the source file and row number.

## 📌 Other Available Document Loaders

LangChain provides many other Document Loaders to work with different data sources and file formats.

The choice of a Document Loader depends on the type of data, project requirements, and specific use case.

Some other available loaders include:

| Document Loader | Purpose |
|---|---|
| JSONLoader | Load and extract data from JSON files. |
| UnstructuredLoader | Load data from different unstructured file formats. |
| Docx2txtLoader | Extract text from Word (`.docx`) files. |
| MarkdownLoader | Load content from Markdown (`.md`) files. |
| BSHTMLLoader | Extract text from HTML files. |
| NotionLoader | Load content from Notion pages and databases. |
| GitLoader | Load files from Git repositories. |
| S3FileLoader | Load files stored in Amazon S3. |
| PlaywrightURLLoader | Load and extract content from web pages using Playwright. |

**Note:** These are just some examples. LangChain supports many more document loaders for different data sources. You should choose a loader based on your application's requirements and the format or source of your data.

Explore more loaders in the [LangChain Documentation](https://docs.langchain.com/oss/python/integrations/document_loaders).


## 🔍 Important Concepts

### Document Object

LangChain uses the `Document` class to represent loaded content.

A Document contains:

```python
Document(
    page_content="Document text goes here",
    metadata={"source": "company_policy.txt"}
)
```

### load() vs lazy_load()

LangChain provides different methods to load documents.

| Method | Description |
|---|---|
| `load()` | Loads all documents and returns them as a list. |
| `lazy_load()` | Returns an iterator that yields documents one at a time. |

**load():**

```python
docs = loader.load()

for doc in docs:
    print(doc.page_content)
```

**lazy_load():**

```python
docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)
```

**Key Difference:**

`load()` loads all documents into memory, whereas `lazy_load()` processes documents incrementally as you iterate over them. Lazy loading can be useful when working with large collections of documents.

## 🔗 Role of Document Loaders in RAG

Document Loaders are typically the first step in a RAG pipeline.

A basic RAG workflow looks like this:

```text
Documents / Data Sources
          |
          ▼
    Document Loaders
          |
          ▼
     Text Splitters
          |
          ▼
       Embeddings
          |
          ▼
     Vector Database
          |
          ▼
      User Query
          |
          ▼
       Retriever
          |
          ▼
      LLM Response
```

**How it works:**

1. **Document Loading:** Load data from PDFs, text files, websites, or other sources.
2. **Text Splitting:** Divide large documents into smaller chunks.
3. **Embeddings:** Convert text chunks into numerical vector representations.
4. **Vector Database:** Store embeddings for efficient similarity search.
5. **Retrieval:** Find relevant chunks based on the user's query.
6. **LLM Response:** Generate an answer using the retrieved context.

Document Loaders prepare the source data for the remaining steps of the RAG pipeline.

## 📁 Project Structure

```text
LangChain-Document-Loaders/
│
├── books/
│
├── 01_text_loader.py
├── 02_pdf_loader.py
├── 03_directory_loader.py
├── 04_web_loader.py
├── 05_csv_loader.py
│
├── company_policy.txt
├── sample_company_handbook.pdf
├── employees.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/JiyaSheikh06/langchain-document-loaders.git
```

**2. Navigate to the project directory**

```bash
cd langchain-document-loaders
```

**3. Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

## 🚀 Running Examples

Run each loader independently:

```bash
python 01_text_loader.py
python 02_pdf_loader.py
python 03_directory_loader.py
python 04_web_loader.py
python 05_csv_loader.py
```

## 🛠️ Technologies Used

- Python
- LangChain
- LangChain Community
- PyPDF
- BeautifulSoup

## 🎯 Learning Objectives

Through this repository, I am exploring:

- Loading documents from different data sources.
- Understanding LangChain Document objects.
- Accessing document content and metadata.
- Working with multiple document formats.
- Understanding `load()` and `lazy_load()`.
- Learning how document loading fits into RAG pipelines.

---

**Part of my hands-on learning journey in LangChain and Generative AI. More practical examples coming soon!** 🚀

## 🤝 Feedback & Contributions

Suggestions, feedback, and discussions are always welcome!

If you find this repository useful, consider giving it a ⭐.

---

## 👩‍💻 Author

**Jiya Sheikh**

GitHub: [@JiyaSheikh06](https://github.com/JiyaSheikh06)