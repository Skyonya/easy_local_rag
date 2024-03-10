from split_docs_tools import split_document
from vectorstore_tools import vectorstore_process
from model_answer import  get_model_answer

if __name__ == "__main__":

    # split documents
    docs = split_document(
        documents_path='documents/hp1.txt',
        chunk_size=2000,
        chunk_overlap=100,
        silent=False
    )

    # =============================================

    # create embeddings and save to Chroma vectorstore_db
    db = vectorstore_process(
        docs=docs,
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
