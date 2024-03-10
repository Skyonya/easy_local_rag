from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings


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
        print(f'Vector store created and saved to {persist_directory}')
    return db


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