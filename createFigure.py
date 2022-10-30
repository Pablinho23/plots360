# Import libs
# -*- coding: utf8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get the data
#df=pd.read_csv(r"C:\Users\Pavel.Ulitin\Documents\avengers_data.csv", sep=';')
def createPlot():
    df=pd.read_csv(r"/home/glowbyte/ulitin_temp/source_file/360.csv", sep=',')
    print(df)

    # Get the data for 1 and 4 obs
    labels=np.array(["SAS","Linux","Oracle","Communication","Managing"])
    labels=np.array(["Деловая переписка","Понимание процесса поддержки","Готовность курировать / Курирование сотрудников","Взаимодействие с коллегами","Взаимодействие с заказчиком","Профессиональная интуиция","Ответственность","Time management","Многозадачность","Инициативность","Оптимизация","SAS","DWH","DBA","LINUX","SQL","SAS Macro/Base","JAVA","Python"])
    stats=df.loc[0,labels].values
    stats1=df.loc[1,labels].values
    stats2=df.loc[2,labels].values
    print(stats)
    print(stats1)
    print(df.loc[0,"Кто оценивает"])

    # Make some calculations for the plot
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats=np.concatenate((stats,[stats[0]]))
    stats1=np.concatenate((stats1,[stats1[0]]))
    stats2=np.concatenate((stats2,[stats2[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    # Plot stuff
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2, label=df.loc[0,"Кто оценивает"])
    #ax1 = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats1, 'o-', linewidth=2, label=df.loc[1,"Кто оценивает"])
    ax.plot(angles, stats2, 'o-', linewidth=2, label=df.loc[2,"Кто оценивает"])
    ax.fill(angles, stats, alpha=0.25) 
    ax.fill(angles, stats1, alpha=0.25)
    ax.fill(angles, stats2, alpha=0.25)

    ax.legend(loc="lower left")

    angles1=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    ax.set_thetagrids(angles1 * 180/np.pi, labels)  # сопоставление статы углам
    #ax.set_title([df.loc[0,"Кто оценивает"]])
    ax.grid(True)

    figure = plt.gcf()
    print(figure)


    #plt.show()
    plt.savefig("/home/glowbyte/ulitin_temp/result/plot")#, dpi = 222300)

#createPlot()
