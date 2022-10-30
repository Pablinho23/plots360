from config import conf_360 as conf

from cProfile import label
from xml.etree.ElementTree import tostring
import pandas as pd
import numpy as np
import gspread
import matplotlib.pyplot as plt
import sys
from datetime import datetime

from oauth2client.service_account import ServiceAccountCredentials

import logging

logging.basicConfig(level=logging.INFO)

def createFifure(df, labels, skill_direction):

    logging.info('-------------')
    logging.info('Start to create %s plot' % skill_direction)

    try:
            
        stats=df.loc[0,labels].values
        stats1=df.loc[1,labels].values
        stats2=df.loc[2,labels].values
        
        # Make some calculations for the plot
        angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        stats=np.concatenate((stats,[stats[0]]))
        stats1=np.concatenate((stats1,[stats1[0]]))
        stats2=np.concatenate((stats2,[stats2[0]]))
        angles=np.concatenate((angles,[angles[0]]))

        # Plot stuff
        fig = plt.figure(figsize=(14,14))
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=2, label=df.loc[0,"Кто оценивает"])
        ax.plot(angles, stats1, 'o-', linewidth=2, label=df.loc[1,"Кто оценивает"])
        ax.plot(angles, stats2, 'o-', linewidth=2, label=df.loc[2,"Кто оценивает"])
        ax.fill(angles, stats, alpha=0.25) 
        ax.fill(angles, stats1, alpha=0.25)
        ax.fill(angles, stats2, alpha=0.25)

        # Define legend location
        ax.legend(loc="lower left", bbox_to_anchor=(-0.1, -0.05), shadow=True, ncol=1)

        angles1=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        # mapping labels with angles
        ax.set_thetagrids(angles1 * 180/np.pi, labels)              
        ax.grid(True)

        current_date_and_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        current_date_and_time_string = str(current_date_and_time)

        plt.savefig("{}{}_{}.pdf".format(conf['plot_location'],skill_direction, current_date_and_time))
        #plt.savefig(conf['plot_location'] +"/%s.pdf" % skill_direction)
        #plt.show()

        logging.info('-------------')
        logging.info('Finish create %s plot' % skill_direction)
    except Exception as e:
        logging.error('Something get wrong. Check log for errors')
        logging.error(e)
        raise


def plotMain():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    try:
        # Get access to GS with consultant marks
        creds = ServiceAccountCredentials.from_json_keyfile_name(conf['secret_json_location'], scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open(conf['root_spreadsheet'])

        # Get target sheet
        project_matrix = spreadsheet.worksheet(conf['root_sheet'])
        list_of_hashes = project_matrix.get_all_records()
        mark_matrix = pd.DataFrame(list_of_hashes)
        labels = list(mark_matrix)
        
        # Hardcode divide skills by sof and hard
        labels_soft = labels[1:12]
        labels_hard = labels[12:]
        
        # Call function to create plots
        createFifure(mark_matrix, labels_soft, 'soft_plot')
        createFifure(mark_matrix, labels_hard, 'hard_plot')
    

    except Exception as e:
        logging.error('Something get wrong. Check log for errors')
        logging.error(e)
        raise


