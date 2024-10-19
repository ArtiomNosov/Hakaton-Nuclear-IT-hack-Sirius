from glob_preprocessing import get_token,get_chat_completion,auth
 
response = get_token(auth)
if response != 1:
    giga_token = response.json()['access_token']
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
conversation_history = [{
        'role': 'system',
        'content': f"Представь себя HR-специалистом. На основе отзыва уволившегося сотрудника составь рекомендацию для компании о том, что нужно улучшить в рабочем процессе, а так же предположи, позитивный это отзыв, негативный или нейтральный, и обоснуй, почему"
        }]
prompt = input()
response, conversation_history = get_chat_completion(giga_token, prompt, conversation_history)
ans = response.json()['choices'][0]['message']['content']
with open('responces/recomendation.txt', 'w+') as file:
    file.write(ans)    