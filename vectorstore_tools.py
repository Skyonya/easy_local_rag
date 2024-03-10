from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

from tools import is_directory_empty, decorator_timer


def vectorstore_process(
        docs,
        embedding_model_name,
        persist_directory,
        silent=True
):
    if is_directory_empty(persist_directory):
        if not silent:
            print(f'Creating vector store...')

        @decorator_timer
        def create_vectorstore():
            # create the open-source embedding function
            embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
            # load it into Chroma
            db = Chroma.from_documents(documents=docs, embedding=embedding_function, persist_directory=persist_directory)
            db.persist()
            return db

        db, exe_time = create_vectorstore()
        if not silent:
            print(f'Vector store created and saved to {persist_directory}')
            print(f'Time spent: {exe_time} seconds')

    else:
        if not silent:
            print('Loading vector store...')

        @decorator_timer
        def load_vectorstore():
            # create the open-source embedding function
            embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
            db = Chroma(embedding_function=embedding_function, persist_directory=persist_directory)
            return db

        db, exe_time = load_vectorstore()
        if not silent:
            print(f'Time spent: {exe_time} seconds')

    # # create the open-source embedding function
    # embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model_name)
    #
    # # load it into Chroma
    # vectorstore_db = Chroma.from_documents(docs, embedding_function)
    return db
