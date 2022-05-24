import numpy as np
import pandas as pd
import pandas as py
from PIL import Image
import matplotlib.pyplot as plt
def zad1():
    plt.figure(figsize=(8,6))

    x1 = np.arange(0, 5, 1)
    x2 = np.arange(0, 4, 1)
    x3 = np.arange(0, 6, 1)

    y1 = [105, 70, 75, 25, 50]
    y2 = [20, 10, 30, 10]
    y3 = [120,120,120,120,120,120]

    plt.bar(x1,y1, color=['teal', 'darkgreen', 'darkkhaki', 'pink', 'lime'])
    plt.bar(x2,y2, color=['indigo', 'cyan', 'olive', 'dodgerblue'])
    plt.plot(x3, y3,'g-')
    plt.ylim(0,150)
    plt.title('Tytuł')

    plt.show()

def zad2():

    xlsx = pd.read_excel('mieszkania1.xlsx')
    df = pd.DataFrame(data=xlsx)
    df.pivot(index='Rok', columns=['Zakres przedmiotowy', 'Formy budownictwa' ], values='Wartość').plot(kind='bar', figsize=(15, 8), edgecolor='black')

    plt.ylabel('Wartości')
    plt.legend(loc='upper right')
    plt.title('Mieszkania')
    plt.yticks(np.arange(0,85000,5000))

    plt.text(-0.45, 75000, '165912',
            verticalalignment='bottom', horizontalalignment='left',
            color='b', fontsize=15, bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 5})

    # ADD a custom grid
    # plt.grid(axis="x", color="green", alpha=.3, linewidth=2, linestyle=":")
    plt.grid(axis="y", color="black", alpha=.5, linewidth=.5)

    plt.savefig('zad2.png')
    plt.show()


    im1 = Image.open('zad2.png')
    im1 = im1.convert('RGB')
    im1.save('zad2.pdf')

def zad3():
    xlsx = pd.read_excel('turystyka1.xlsx')
    df = pd.DataFrame(data=xlsx)
    # df2 = df.rename(columns=df.iloc[0]).drop(df.index[0]).T

    df2 = df.T
    df2.columns = ['Rok', 'Liczba Kategorii']
    x14 = df2.loc[df2['Rok'] == 2014].sum()[1]
    x15 = df2.loc[df2['Rok'] == 2015].sum()[1]

    x19 = df2.loc[df2['Rok'] == 2019].sum()[1]
    x17 = df2.loc[df2['Rok'] == 2017].sum()[1]
    labels1=['2014', '2015']
    labels2=['2019', '2017']
    colors=['#aabbcc', '#abcdef']


    fig, axes = plt.subplots(2,2)

    axes[0,0].pie([x14,x15], labels=labels1, colors=colors)
    axes[1,1].pie([x19,x17], labels=labels2, colors=colors)
    axes[0,0].set_title('względny udział różnych kategorii hoteli\n w danych latach')


    fig.delaxes(axes[0,1])
    fig.delaxes(axes[1,0])
    plt.subplots_adjust(hspace=0)
    plt.show()

zad3()