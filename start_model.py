from split_docs_tools import split_document
from vectorstore_tools import load_vectorstore, create_vectorstore
from model_answer import get_model_answer
from tools import is_directory_empty

documents_path = 'documents/hp1.txt'
persist_directory = 'vectorstore_db'

if __name__ == "__main__":

    if is_directory_empty(persist_directory):

        # split documents
        docs = split_document(
            documents_path=documents_path,
            chunk_size=2000,
            chunk_overlap=100,
            silent=False
        )

        db = create_vectorstore(
            docs=docs,
            embedding_model_name="all-MiniLM-L6-v2",
            persist_directory='vectorstore_db',
            silent=False
        )

    else:
        db = load_vectorstore(
            embedding_model_name="all-MiniLM-L6-v2",
            persist_directory='vectorstore_db',
            silent=False
        )

    # =============================================

    while True:
        user_input = input("Q: ")

        # similarity search from vector vectorstore_db
        docs = db.similarity_search(user_input)
        relevant_document = docs[0].page_content
        # print results
        print('-----------------')
        print('relevant_document:')
        print(relevant_document)

        bot_answer = get_model_answer(
            user_input=user_input,
            relevant_document=relevant_document
        )

        print('-----------------')
        print(f'Q: {user_input}')
        print(f'A: {bot_answer}')
