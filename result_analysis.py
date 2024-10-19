import matplotlib.pyplot as plt
import re
import pandas as pd
from wordcloud import WordCloud
from transformers import pipeline
model = pipeline(model = 'seara/rubert-tiny2-russian-sentiment')
pos = {}
neu = {}
neg = {}
sense = ['neutral', 'positive', 'negative']
flag = int(input())

path = 'responces/' + sense[flag] + '.txt'
filename = 'images/' +sense[flag] + '.png'

dist = pd.read_csv('ctables/pnn_dist.csv')
text = ''
counter = 0
true_positives = 0
with open(path,'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.split('-')
        if len(line) < 2:
            continue
        label = model(line[0])[0]['label']
        if label == sense[flag]:
            true_positives += 1
        if len(line[0]) > 20:
            continue
        text += str(line[0])
    counter += 1    

print(true_positives/counter)

def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 
    plt.axis("off")

wordcloud = WordCloud(width = 2000, 
height = 1500, 
random_state=1, 
background_color='black', 
margin=20, 
colormap='Pastel1', 
collocations=False).generate(text)

plot_cloud(wordcloud)

wordcloud.to_file('neutral.png')