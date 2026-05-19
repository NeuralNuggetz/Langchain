from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader =  DirectoryLoader(
    path = 'Document_Loader/Directory_Loader/books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)


