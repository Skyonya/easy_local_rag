from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

from split_docs_tools import load_and_split_docs
from tools import is_directory_empty, decorator_timer


@decorator_timer
def create_vectorstore(
        docs,
        embedding_model_name,
        persist_directory,
        silent=True
):
    if not silent:
        print(f'Creating vector store...')
    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
    # load it into Chroma
    db = Chroma.from_documents(documents=docs, embedding=embedding_function, persist_directory=persist_directory)
    db.persist()
    if not silent:
        print(f'Vector store created and saved to folder: {persist_directory}')
    return db


@decorator_timer
def load_vectorstore(
        embedding_model_name,
        persist_directory,
        silent=True
):
    if not silent:
        print('Loading vector store...')
    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
    db = Chroma(embedding_function=embedding_function, persist_directory=persist_directory)
    if not silent:
        print(f'Vector store loaded')
    return db


def get_vectorstore(
        documents_path,
        embedding_model_name,
        persist_directory,
        chunk_size=1000,
        chunk_overlap=100,
        silent=True
):
    if is_directory_empty(persist_directory, silent=silent):

        # load and split documents
        docs = load_and_split_docs(
            documents_path=documents_path,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            silent=silent
        )

        # create vector store db
        db, time = create_vectorstore(
            docs=docs,
            embedding_model_name=embedding_model_name,
            persist_directory=persist_directory,
            silent=silent
        )
        if not silent:
            print(f'Creating time', time)

    else:
        # load vector store db
        db, time = load_vectorstore(
            embedding_model_name=embedding_model_name,
            persist_directory=persist_directory,
            silent=silent
        )
        if not silent:
            print(f'Loading time', time)
    return db
