import re
from os import listdir
from os.path import isfile, join
import numpy as np
from matplotlib import pyplot as plt
import math
import seaborn as sns
import csv

names = ["Iliya", "Chris", "Matti", "Bozhidar"]
images = ["im1", "im2", "im3", "im4", "im5", "im6"]
variables = ["br", "con", "sat"]

def f1():
    for name in names:
        for image in images:
            
            fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
            fig.set_figwidth(13.5)
            
            for variable in variables:
                
                observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
                
                
                
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
                    
                # Heatmap
                sns.set_style('whitegrid')
                sns.set_context('talk')

                # absolute numbers
                matrix = observations

                # Parametern und Texten anpassen !
                if(variable == 'br'):
                    ax1 = sns.heatmap(matrix, square = True, ax = ax[0], vmin = 0, vmax = 3, cmap = "flare", annot = True)
                    ax1.tick_params(left = True, bottom = True)
                    ax[0].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                    ax[0].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    ax[0].set_xlabel('Brightness (S2)')
                    ax[0].set_ylabel('Brightness (S1)')
                    ax[0].set_title('Abs. frequ. (' + name + ' ' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
                if (variable == 'con'):
                    ax2 = sns.heatmap(matrix, square = True, ax = ax[1], vmin = 0, vmax = 3, cmap = "flare", annot = True)
                    ax2.tick_params(left = True, bottom = True)
                    ax[1].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                    ax[1].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    ax[1].set_xlabel('Contrast (S2)')
                    ax[1].set_ylabel('Contrast (S1)')
                    ax[1].set_title('Abs. frequ. (' + name + ' ' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
                if (variable == 'sat'):
                    ax3 = sns.heatmap(matrix, square = True, ax = ax[2], vmin = 0, vmax = 3, cmap = "flare", annot = True)
                    ax3.tick_params(left = True, bottom = True)
                    ax[2].set_xticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], fontsize = 14)
                    ax[2].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    #ax[2].set_yticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0, fontsize = 14)
                    ax[2].set_xlabel('Saturation (S2)')
                    ax[2].set_ylabel('Saturation (S1)')
                    ax[2].set_title('Abs. frequ. (' + name + ' ' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')

            plt.show()
        
            #f.savefig(name + '_' + image + '_' + variable +'_heatmap_absolut.pdf')

def f2():
    for image in images:
        
        fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
        fig.set_figwidth(13.5)
        
        for variable in variables:

            observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
            
            for name in names:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
            
            # Heatmap
            sns.set_style('whitegrid')
            sns.set_context('talk')

            # absolute numbers
            matrix = observations

            # Parametern und Texten anpassen !
            if(variable == 'br'):
                ax1 = sns.heatmap(matrix, square = True, ax = ax[0], vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax1.tick_params(left = True, bottom = True)
                ax[0].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                ax[0].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                ax[0].set_xlabel('Brightness (S2)')
                ax[0].set_ylabel('Brightness (S1)')
                ax[0].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'con'):
                ax2 = sns.heatmap(matrix, square = True, ax = ax[1], vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax2.tick_params(left = True, bottom = True)
                ax[1].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                ax[1].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                ax[1].set_xlabel('Contrast (S2)')
                ax[1].set_ylabel('Contrast (S1)')
                ax[1].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'sat'):
                ax3 = sns.heatmap(matrix, square = True, ax = ax[2], vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax3.tick_params(left = True, bottom = True)
                ax[2].set_xticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], fontsize = 14)
                ax[2].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                #ax[2].set_yticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0, fontsize = 14)
                ax[2].set_xlabel('Saturation (S2)')
                ax[2].set_ylabel('Saturation (S1)')
                ax[2].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                
        plt.show()
            
        #f.savefig(image + '_' + variable +'_heatmap_absolut.pdf')

def f3():
    for name in names:
        
        fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
        fig.set_figwidth(13.5)
        
        for variable in variables:
            
            observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
            for image in images:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
                    
            # Heatmap
            sns.set_style('whitegrid')
            sns.set_context('talk')
            
            # absolute numbers
            matrix = observations

            # Parametern und Texten anpassen !
            if(variable == 'br'):
                    ax1 = sns.heatmap(matrix, square = True, ax = ax[0], vmin = 0, vmax = 18, cmap = "flare", annot = True)
                    ax1.tick_params(left = True, bottom = True)
                    ax[0].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                    ax[0].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    ax[0].set_xlabel('Brightness (S2)')
                    ax[0].set_ylabel('Brightness (S1)')
                    ax[0].set_title('Abs. frequ. (' + name + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'con'):
                    ax2 = sns.heatmap(matrix, square = True, ax = ax[1], vmin = 0, vmax = 18, cmap = "flare", annot = True)
                    ax2.tick_params(left = True, bottom = True)
                    ax[1].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                    ax[1].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    ax[1].set_xlabel('Contrast (S2)')
                    ax[1].set_ylabel('Contrast (S1)')
                    ax[1].set_title('Abs. frequ. (' + name + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'sat'):
                    ax3 = sns.heatmap(matrix, square = True, ax = ax[2], vmin = 0, vmax = 18, cmap = "flare", annot = True)
                    ax3.tick_params(left = True, bottom = True)
                    ax[2].set_xticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], fontsize = 14)
                    ax[2].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                    #ax[2].set_yticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0, fontsize = 14)
                    ax[2].set_xlabel('Saturation (S2)')
                    ax[2].set_ylabel('Saturation (S1)')
                    ax[2].set_title('Abs. frequ. (' + name + ' ' + variable + ')\n"S1 more beautiful than S2"')
                
        plt.show()
        
        #f.savefig(name + '_' + variable +'_heatmap_absolut.pdf')

def f4():
    fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
    fig.set_figwidth(13.5)

    for variable in variables:
            
        observations = np.array( [  [np.nan, 0, 0, 0, 0, 0],
                                    [0, np.nan, 0, 0, 0, 0],
                                    [0, 0, np.nan, 0, 0, 0],
                                    [0, 0, 0, np.nan, 0, 0],
                                    [0, 0, 0, 0, np.nan, 0],
                                    [0, 0, 0, 0, 0, np.nan]])
            
        for name in names:
            for image in images:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
                    
        # Heatmap
        sns.set_style('whitegrid')
        sns.set_context('talk')

        # absolute numbers
        matrix = observations

        # making heatmap
        #f = plt.figure(figsize=(7, 5))
        #ax = sns.heatmap(matrix, square=True,  vmin = 0, vmax = 72,
        #                         cmap="flare", # can be changed to another sequential colormap
        #                         annot=True) # optional with numbers annotated

        # Parametern und Texten anpassen !
        if(variable == 'br'):
            ax1 = sns.heatmap(matrix, square = True, ax = ax[0], vmin = 0, vmax = 72, cmap = "flare", annot = True)
            ax1.tick_params(left = True, bottom = True)
            ax[0].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
            ax[0].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
            ax[0].set_xlabel('Brightness (S2)')
            ax[0].set_ylabel('Brightness (S1)')
            ax[0].set_title('Abs. frequ. (' + variable + ')\n"S1 more beautiful than S2"')
                    
                    
        if (variable == 'con'):
            ax2 = sns.heatmap(matrix, square = True, ax = ax[1], vmin = 0, vmax = 72, cmap = "flare", annot = True)
            ax2.tick_params(left = True, bottom = True)
            ax[1].set_xticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
            ax[1].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
            ax[1].set_xlabel('Contrast (S2)')
            ax[1].set_ylabel('Contrast (S1)')
            ax[1].set_title('Abs. frequ. (' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
        if (variable == 'sat'):
            ax3 = sns.heatmap(matrix, square = True, ax = ax[2], vmin = 0, vmax = 72, cmap = "flare", annot = True)
            ax3.tick_params(left = True, bottom = True)
            ax[2].set_xticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], fontsize = 14)
            ax[2].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
            #ax[2].set_yticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0, fontsize = 14)
            ax[2].set_xlabel('Saturation (S2)')
            ax[2].set_ylabel('Saturation (S1)')
            ax[2].set_title('Abs. frequ. (' + variable + ')\n"S1 more beautiful than S2"')
                
    plt.show()
        
        #f.savefig(variable +'_heatmap_absolut.pdf')

def bestImage():
    for image in images:
        
        fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
        fig.set_figwidth(13.5)
        fig.set_figheight(3.5)
        
        for variable in variables:

            observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
            
            for name in names:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
            
            # Heatmap
            sns.set_style('whitegrid')
            sns.set_context('talk')

            # absolute numbers
            matrix = [[0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0]]
            
            for i in range (6):
                for j in range (6):
                    if i != j:
                        matrix[i][0] += observations[i][j]

            # Parametern und Texten anpassen !
            if(variable == 'br'):
                ax1 = sns.heatmap(matrix, square = True, ax = ax[0], vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax1.tick_params(left = True, bottom = True)
                ax[0].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0)
                ax[0].set_ylabel('Brightness')
                ax[0].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'con'):
                ax2 = sns.heatmap(matrix, square = True, ax = ax[1], vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax2.tick_params(left = True, bottom = True)
                ax[1].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0)
                ax[1].set_ylabel('Contrast')
                ax[1].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'sat'):
                ax3 = sns.heatmap(matrix, square = True, ax = ax[2], vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax3.tick_params(left = True, bottom = True)
                ax[2].set_yticklabels(['0.7', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0)
                #ax[2].set_yticklabels(['0.7', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0)
                ax[2].set_ylabel('Saturation')
                ax[2].set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                
        plt.show()
            
        #f.savefig(image + '_' + variable +'_heatmap_absolut.pdf')

def im2_1():
    for image in ["im2"]:
        
        fig, ax = plt.subplots(ncols = 3, sharey = False, constrained_layout = True)
        fig.set_figwidth(13.5)
        fig.set_figheight(3.5)
        
        for variable in variables:

            observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
            
            for name in names:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
            
            # Heatmap
            sns.set_style('whitegrid')
            sns.set_context('talk')

            # absolute numbers
            matrix = [[0],
                    [0],
                    [0],
                    [0],
                    [0],
                    [0]]
            
            for i in range (6):
                for j in range (6):
                    if i != j:
                        matrix[i][0] += observations[i][j]
            
    #         f = plt.figure(figsize=(7, 5))

            # Parametern und Texten anpassen !
            if(variable == 'br'):
                plt.sca(ax[0])
                ax1 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax1.tick_params(left = True)
                ax1.set_yticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0)
                ax1.set_ylabel('Brightness', fontsize = 25)
                ax1.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
            if (variable == 'con'):
                plt.sca(ax[1])
                ax2 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax2.tick_params(left = True)
                ax2.set_yticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0)
                ax2.set_ylabel('Contrast', fontsize = 25)
                ax2.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
            if (variable == 'sat'):
                plt.sca(ax[2])
                ax3 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 60, cmap = "flare", annot = True)
                ax3.tick_params(left = True)
                ax3.set_yticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0)
                ax3.set_ylabel('Saturation', fontsize = 25)
                ax3.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
            
    #     fig.savefig("Bild2H1.jpg")

def im2_2():
    for image in ["im2"]:
        
        fig, ax = plt.subplots(ncols = 3, sharey = True, constrained_layout = True)
        fig.set_figwidth(13.5)
        
        for variable in variables:

            observations = np.array( [[np.nan, 0, 0, 0, 0, 0],
                                        [0, np.nan, 0, 0, 0, 0],
                                        [0, 0, np.nan, 0, 0, 0],
                                        [0, 0, 0, np.nan, 0, 0],
                                        [0, 0, 0, 0, np.nan, 0],
                                        [0, 0, 0, 0, 0, np.nan]])
            
            for name in names:
                for versuch in range (3):
                    
                    f = open('data/' + name + '_ordinal_' + image + '_' + variable + '_' + str(versuch) + '.csv')
                    
                    csv_f = csv.reader(f)

                    for row in csv_f:

                        if(row != []):

                            if(row[0] == '0'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[x][y] += 1

                            if(row[0] == '1'):
                                x = int(row[1]) - 1
                                y = int(row[2]) - 1
                                observations[y][x] += 1

                    f.close
            
            # Heatmap
            sns.set_style('whitegrid')
            sns.set_context('talk')

            # absolute numbers
            matrix = observations

            # Parametern und Texten anpassen !
            if(variable == 'br'):
                plt.sca(ax[0])
                ax1 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax1.tick_params(left = True, bottom = True)
                ax1.set_xticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                ax1.set_yticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                ax1.set_xlabel('Brightness (S2)')
                ax1.set_ylabel('Brightness (S1)')
                ax1.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'con'):
                plt.sca(ax[1])
                ax2 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax2.tick_params(left = True, bottom = True)
                ax2.set_xticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], fontsize = 14)
                ax2.set_yticklabels(['0.70', '0.85', '1.00', '1.15', '1.30', '1.45'], rotation = 0, fontsize = 14)
                ax2.set_xlabel('Contrast (S2)')
                ax2.set_ylabel('Contrast (S1)')
                ax2.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                    
                        
            if (variable == 'sat'):
                plt.sca(ax[2])
                ax3 = sns.heatmap(matrix, square = True, vmin = 0, vmax = 12, cmap = "flare", annot = True)
                ax3.tick_params(left = True, bottom = True)
                ax3.set_xticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], fontsize = 14)
                ax3.set_yticklabels(['0.75', '0.90', '1.00', '1.20', '1.40', '1.60'], rotation = 0, fontsize = 14)
                ax3.set_xlabel('Saturation (S2)')
                ax3.set_ylabel('Saturation (S1)')
                ax3.set_title('Abs. frequ. (' + image + ' ' + variable + ')\n"S1 more beautiful than S2"')
                
        plt.show()
            
        #f.savefig(image + '_' + variable +'_heatmap_absolut.pdf')