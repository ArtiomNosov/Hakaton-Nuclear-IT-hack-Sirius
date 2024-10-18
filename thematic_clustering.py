import pandas as pd
from glob_preprocessing import get_token, auth, get_chat_completion


if __name__ == '__main__':
    conversation_history = []
    df = pd.read_csv('/ctables/pnn_dist.csv')
    response = get_token(auth)
    if response != 1:
        giga_token = response.json()['access_token']
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    for i in ['негативные']:
        if i == 'позитивные':
            n = int(df['pos'])
            with open('prompts/pos_prompt.txt','r') as file:
                prompt = file.read()
            filename = 'responces/positive.txt'
        elif i == 'негативные':
            n = int(df['neu'])
            with open('prompts/neg_prompt.txt','r') as file:
                prompt = file.read()
            filename = 'responces/negative.txt'
        else:
            n = int(df['neu']) 
            with open('prompts/neu_prompt.txt','r') as file:
                prompt = file.read()
            filename = 'responces/neutral.txt'
        conversation_history = [{
        'role': 'system',
        'content': f"Представь себя HR-специалистом. Тебе нужно найти {i} словосочетания в следующем списке и разделить их на большие группы так, чтобы в каждой группе было как можно больше близких по смыслу словосочетаний. Ответь в формате: название темы - количество словоочетаний. Убедись, что название каждой группы содержит менее 3 слов. Убедись также, что ты не нумеруешь новую строку"
        }]
        response, conversation_history = get_chat_completion(giga_token, prompt, conversation_history)
        ans = response.json()['choices'][0]['message']['content']
        with open(filename, 'w+') as file:
            file.write(ans)