from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


def split_document(documents_path, chunk_size=1000, chunk_overlap=0):
    # load the document
    loader = TextLoader(documents_path)
    documents = loader.load()

    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs
