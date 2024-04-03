from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

from split_docs_tools import load_and_split_docs
from tools import is_directory_empty, decorator_timer

import logging


@decorator_timer
def create_vectorstore(
        docs,
        embedding_model_name,
        persist_directory,
):
    logging.info('Creating vector store...')
    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
    # load it into Chroma
    db = Chroma.from_documents(documents=docs, embedding=embedding_function, persist_directory=persist_directory)
    db.persist()
    logging.info(f'Vector store was created and saved to folder: {persist_directory}')
    return db


@decorator_timer
def load_vectorstore(
        embedding_model_name,
        persist_directory,
):
    logging.info('Loading vector store...')
    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
    db = Chroma(embedding_function=embedding_function, persist_directory=persist_directory)
    logging.info('Vector store was loaded')
    return db


def get_vectorstore(
        documents_path,
        embedding_model_name,
        persist_directory,
        chunk_size=1000,
        chunk_overlap=100,
):
    if is_directory_empty(persist_directory):

        # load and split documents
        docs = load_and_split_docs(
            documents_path=documents_path,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        # create vector store db
        db, time = create_vectorstore(
            docs=docs,
            embedding_model_name=embedding_model_name,
            persist_directory=persist_directory,
        )
        logging.info(f'Creating time', time)

    else:
        # load vector store db
        db, time = load_vectorstore(
            embedding_model_name=embedding_model_name,
            persist_directory=persist_directory,
        )
        logging.info(f'Loading time', time)
    return db
