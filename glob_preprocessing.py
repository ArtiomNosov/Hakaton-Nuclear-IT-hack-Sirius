import pandas as pd
import base64
import requests
import json
import uuid




auth = "MDhiOTZhYWUtNjhkYy00MTgwLTljZmUtODZlN2UzYTM2YmQwOjA3YzhlMjhlLWM2YjYtNDZkYS1hMGRmLTI2MzYwYWQxYzIwMg=="

def get_token(auth_token, scope = "GIGACHAT_API_PERS"):
  rq_uid = str(uuid.uuid4())
  url = url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
  
  headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }
    
  payload = {
        'scope': scope
    }
  try:
    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response
  except requests.RequestException as e:
      print(f"Ошибка: {str(e)}")
      return -1




def get_chat_completion(auth_token, user_message, conversation_history=None):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    if conversation_history is None:
        conversation_history = []

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": conversation_history,
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1,
        "update_interval": 0
    })


    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response_data = response.json()
        print(response_data)

        conversation_history.append({
            "role": "assistant",
            "content": response_data['choices'][0]['message']['content']
        })

        return response, conversation_history
    except requests.RequestException as e:
        print(f"Произошла ошибка: {str(e)}")
        return None, conversation_history

conversation_history = [{
    'role': 'system',
    'content': 'из отправленного запроса извлеки ключевые слова'

}

]
if __name__ == "__main__":
    df = pd.read_excel('ctables/nhack.xlsx')
    df = df.dropna()
    df = df.drop_duplicates()
    response = get_token(auth)
    if response != 1:
        giga_token = response.json()['access_token']
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    new_df = {'q1':[], 'q3':[],'q4':[], 'q5':[]}
    new_df = pd.DataFrame(new_df)
    for i,row in df.iterrows():
        prompt = row[0] + row[1]
        response, conversation_history = get_chat_completion(giga_token, prompt, conversation_history)
        ans = response.json()['choices'][0]['message']['content']
        new_df.loc[len(new_df)] = [ans, row[2],row[3],row[4]]
    new_df.to_csv('ctables/test.csv')
