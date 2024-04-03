from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

import logging


def load_document(documents_path):
    # load the document
    loader = TextLoader(documents_path)
    documents = loader.load()
    logging.info('Documents was loaded')
    return documents


def split_document(
        documents,
        chunk_size=1000,
        chunk_overlap=100,
):
    # split documents into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    logging.info('Documents was splitted')
    return docs


def load_and_split_docs(
        documents_path,
        chunk_size=1000,
        chunk_overlap=100,
):
    documents = load_document(documents_path)
    docs = split_document(documents, chunk_size, chunk_overlap)
    logging.info(f'Created {len(docs)} splits from {documents_path}')
    return docs
