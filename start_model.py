from split_docs_tools import split_document
from vectorstore_tools import vectorstore_process

import requests
import json


if __name__ == "__main__":

    # split documents
    docs = split_document(
        documents_path='documents/hp1.txt',
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

    user_input = "What is Nearly Headless Nick’s real name?"

    # similarity search from vector vectorstore_db
    docs = db.similarity_search(user_input)
    relevant_document = docs[0].page_content
    # print results
    print('-----------------')
    print('relevant_document:')
    print(relevant_document)

    # Ollama API
    # https://github.com/jmorganca/ollama/blob/main/docs/api.md
    prompt = """
    You are a bot that makes recommendations based on document. You answer in very short sentences and do not include extra information.
    This is the recommended document: {relevant_document}
    The user input is: {user_input}
    Compile a recommendation to the user based on the recommended document and the user input.
    """

    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "mistral",
        "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document)
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
    full_response = []
    try:
        count = 0
        for line in response.iter_lines():
            if line:
                decoded_line = json.loads(line.decode('utf-8'))
                full_response.append(decoded_line['response'])
    finally:
        response.close()

    bot_answer = ''.join(full_response)
    print('-----------------')
    print(f'Q: {user_input}')
    print(f'A: {bot_answer}')