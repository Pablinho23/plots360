from cProfile import label
import pandas as pd
import numpy as np
import gspread
import matplotlib.pyplot as plt
import sys

from oauth2client.service_account import ServiceAccountCredentials

import logging

def createFifure(df, labels, skill_direction):
    stats=df.loc[0,labels].values
    stats1=df.loc[1,labels].values
    stats2=df.loc[2,labels].values
    print(stats)

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


    plt.show()
    plt.savefig("/home/glowbyte/ulitin_temp/result/skill_direction")


def plotMain():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    try:
        # получаем доступ к Google Sheet с матрицей проектов
        creds = ServiceAccountCredentials.from_json_keyfile_name("/glowbyte/support_bot/conf/client_secret.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Оценка 360 (Responses)")

        # обращаемся к листу с консультантами
        project_matrix = spreadsheet.worksheet('график')
        list_of_hashes = project_matrix.get_all_records()
        mark_matrix = pd.DataFrame(list_of_hashes)
        print(mark_matrix)
        #labels=np.array(["Деловая переписка","Понимание процесса поддержки","Готовность курировать / Курирование сотрудников","Взаимодействие с коллегами","Взаимодействие с заказчиком","Профессиональная интуиция","Ответственность","Time management","Многозадачность","Инициативность","Оптимизация","SAS","DWH","DBA","LINUX","SQL","SAS Macro/Base","JAVA","Python"])
        #labels = project_matrix_df.columns.get_values()
        labels = list(mark_matrix)
        labels_soft = labels[1:12]
        labels_hard = labels[12:]
        #labels = labels.tolist()
        print(labels_soft)
        print(labels_hard)
        
        createFifure(mark_matrix, labels_soft, 'soft_plot')
        createFifure(mark_matrix, labels_hard, 'hard_plot')
    

    except Exception as e:
        logging.error('Unnable to get Google Sheet with project matrix')
        logging.error(e)
        raise

plotMain()
