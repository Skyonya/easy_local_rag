from model_answer import get_model_answer
from vectorstore_tools import get_vectorstore

documents_path = 'documents/hp1.txt'
db_path = 'vectorstore_db'
silent = False  # enable or disable log comments

if __name__ == "__main__":

    # chunk document and save vector db
    # or load current vector db
    db = get_vectorstore(
        documents_path=documents_path,
        embedding_model_name="all-MiniLM-L6-v2",
        persist_directory='vectorstore_db',
        chunk_size=2500,
        chunk_overlap=500,
        silent=silent
    )

    # =============================================

    while True:
        user_input = input("Q: ")

        # similarity search from vector vectorstore_db
        # docs = db.similarity_search(user_input)
        # relevant_document = docs[0].page_content

        relevant_document, score = db.similarity_search_with_relevance_scores(user_input)[0]
        relevant_document = relevant_document.page_content

        if not silent:
            print('score ', score)
            if score < 0.4:
                print('score is too low, trying to answer without docs')
                relevant_document = None
            else:
                # print results
                print('-----------------')
                print('relevant_document:')
                print(relevant_document)

        bot_answer = get_model_answer(
            user_input=user_input,
            model_name="mistral",
            relevant_document=relevant_document
        )

        print('-----------------')
        print(f'Q: {user_input}')
        print(f'A: {bot_answer}')
        print('-----------------')
