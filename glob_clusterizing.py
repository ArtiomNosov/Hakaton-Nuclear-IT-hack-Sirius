
import pandas as pd
from transformers import pipeline

if __name__ == '__main__':
    model_sensitive = pipeline(model = 'seara/rubert-tiny2-russian-sentiment')
    df = pd.read_csv('ctables/test.csv')
    sen = []
    score = []
    pos_count = 0
    neg_count = 0
    neutral_count = 0
    pos_themes = ''
    neutral_themes = ''
    negative_themes = ''
    for i,row in df.iterrows():
        arg = row['q1']
        ans = model_sensitive(arg)
        sens = ans[0]['label']
        sen.append(sens)
        sc = ans[0]['score']
        score.append(sc)
        if sens == 'positive':
            pos_count += 1
            pos_themes += str(row['q1']) + ','
        elif sens == 'neutral':
            neutral_count += 1
            neutral_themes += str(row['q1']) + ","
        else:
            neg_count += 1
            negative_themes += str(row['q1']) + ","

    df['sen'] = sen
    df['score'] = score
    df.to_csv('ctables/first_clustering.csv')

    with open('prompts/pos_prompt.txt', 'w+') as file:
        file.write(pos_themes)
    with open('prompts/neg_prompt.txt', 'w+') as file:
        file.write(negative_themes)
    with open('prompts/neu_prompt.txt', 'w+') as file:
        file.write(neutral_themes)

    data = {'pos':[pos_count], 'neu': [neutral_count], 'neg': [neutral_count]}
    pnn_df = pd.DataFrame(data)
    pnn_df.to_csv('ctables/pnn_dist.csv')

