import matplotlib.pyplot as plt
import re
import pandas as pd
from wordcloud import WordCloud
pos = {}
neu = {}
neg = {}

dist = pd.read_csv('ctables/pnn_dist.csv')

text = ''
with open('responces/negative.txt','r') as file:
    text = file.read()
text = re.sub(r'==.*?==+', '', text)

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

wordcloud.to_file('negative.png')