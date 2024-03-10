from langchain_community.vectorstores import Chroma

from tools import is_directory_empty, decorator_timer


def process_vectorstore(embeddings, persist_directory, chunks,
                     silent=True):
    if is_directory_empty(persist_directory):
    # Create Ollama embeddings and vector store
        if not silent:
            print(f'Creating vector store...')
        @decorator_timer
        def create_vector_store():
            vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings, persist_directory=persist_directory)
            vectorstore.persist()
            return vectorstore

        vectorstore, exe_time = create_vector_store()
        if not silent:
            print(f'Vector store created and saved to {persist_directory}')
            print(f'Time spent: {exe_time} seconds')
    else:
        if not silent:
            print('Loading vector store...')

        @decorator_timer
        def load_vector_store():
            vectorstore = Chroma(embedding_function=embeddings, persist_directory=persist_directory)
            return vectorstore

        vectorstore, exe_time = load_vector_store()
        if not silent:
            print(f'Time spent: {exe_time} seconds')

    return vectorstore