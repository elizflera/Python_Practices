import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GAMES.csv', delimiter=';')

# Какие годы были самыми популярными с точки зрения выхода игр?
games = df.groupby('Год издания')['Название'].count().to_frame('Количество').reset_index()
games.plot.bar(x='Год издания', y='Количество', figsize=(20, 10))
plt.suptitle('Количество выпущенных игр по годам')

# Какие жанры были популярны в различные периоды времени?
figsize_big = (20, 12)
fontsize = 20
fig, ax = plt.subplots(figsize=figsize_big)

for genre in df['Жанр'].unique():
    data = df[df['Жанр'] == genre].groupby('Год издания')['Название'].count()
    a = data
    ax.bar(data.index, data, label=genre, alpha=0.4)

plt.legend(title="Платформа", fontsize=fontsize, title_fontsize=fontsize)
plt.suptitle('Динамика продаж по жанрам', fontsize=fontsize)
plt.xlabel('Год издания', fontsize=fontsize)
plt.ylabel('Количество выпущенных игр', fontsize=fontsize)
plt.xticks(rotation=90)
plt.show()

