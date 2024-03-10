import requests
import json


def get_model_answer(user_input, relevant_document):
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
    return bot_answer

