import re
from os import listdir
from os.path import isfile, join
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import math

#This document is solely based on Datenauswerter.ipynb and its only purpose is to offer functions for conciseness to the README file

'''
Input:
    fileName - A string in the form of "Name_ordinal_im2_br_0.csv"

Splits it into name, scale, image name, property, attempt no.
Returns: [name,scale,image name, property, attempt no.]
'''
def processName(fileName):
    splitFileName = re.split('_|\.',fileName)
    name, scale, imName, prop, attempt = splitFileName[:-1] #Prop is short for property like (br, con, sat)
    # print(name,scale,imName, prop, tr)
    attempt = int(attempt) #Parse from string to int
    return [name,scale,imName,prop,attempt]

'''
Input:
    file - A file to process the name from
Return [name,scale,image name, property, attempt no.]
'''
def processNameFromFile(file):
    fname = file.name.split("\\")[2]
    return processName(fname)

'''
This function is used in the createEntry function
Input:
    file - A single .csv data experiment file
Return:
    Chosen images in order of choice - should be sorted afterwards (image numbers)
'''
def processData(file):
    f = file.read()
    data = re.split('\n |\n\n' ,f)
    data = data[1:-1]
    res = []
#     print(processNameFromFile(file)) #For debugging
#     print(data)
    for entry in data:
        entr = entry.split(',')
#         print(entr)
        resp = int(entr[0])
        chosenImage = int(entr[resp+1]) #Select the image number and add to res[]
#         print(chosenImage,type(chosenImage))
        res.append(chosenImage)
    return res

'''
Simply sorts the given list and also returns it for convenience
'''
def sortData(choices):
    choices.sort()
    return choices

def listFiles():
    mypath = ".\data"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def createEntry(fname):
    #Create and process data
    nameData = processName(fname)
    name,scale,imName,prop,attempt = nameData #For simplicity
    path = ".\\data\\" + fname
    f = open(path,'r') #open the file
#     d = sortData(processData(f)) #Make data
    d = processData(f)
    
    #Create the entry
    entry = []
    entry.append(name) #First part of entry is the subject name
    entry.append(imName) #2nd part = image name
    entry.append(prop) #3rd part = property
    entry.append(attempt) #4th part = attempt no.
    entry.append(d) #5th part of entry is the data list
    return entry

def consolidate(fileNameList):
    res = [createEntry(fname) for fname in fileNameList]
    return res

'''
Retrieves the entries that match the parameters
'''
def get(data, sName = '', imName='', prop='',attempt=''):
    #For safety
    if (data==None or data==[]):
        print("You didn't specify data or your data is empty.")
        return None
    if (sName=='' and imName=='' and prop=='' and attempt==''):
        print("Please specify at least one parameter.")
        return None
    
    #Actual function
    res = data
    if (sName!=''):
        res = [entry for entry in res if entry[0]==sName]
    if (imName!=''):
        res = [entry for entry in res if entry[1]==imName]
    if (prop!=''):
        res = [entry for entry in res if entry[2]==prop]
    if (attempt!=''):
        res = [entry for entry in res if entry[3]==attempt]
    return res

def writeAllData(d):
    f = open("alldata.csv",'w')
    line1 = "SubjectName,ImageName,Property,Attempt,Data\n"
    f.write(line1)
    for entry in d:
        line = ''
        for e in entry:
            s = str(e)+','
            line+=s
        line=line[:-1] #Remove the last ','
        line+="\n"#Add newline
#         print(str(line))
        f.write(line)
    f.close()
    

def mergeTries(data):
    d = list(data) #To not change the original data
    nd = np.array(d) #To work with np
    merged = []
    skiplist = [] #To not iterate over the same items, list of indexes
    for i in range(0,len(d)): #First iteration
        if i in skiplist:
            continue
        entry = d[i]
        toMerge = np.array([entry]) #ToMerge list only consists of current entry
        for j in range(0,len(d)): #Iterate again over list
            e = d[j] #2nd level entry
            if (e[0]==entry[0] and e[1] == entry[1] and e[2] == entry[2] and e[3] != entry[3]): #If entry is found again with different amount of tries:
                toMerge = np.append(toMerge, [e], axis=0) #Put that entry into toMerge list
                skiplist.append(j)
            l = len(toMerge)
        if (l>=1):
            values = np.array(toMerge[:,-1]) #Get the list of values
            vals = []
            for li in values:
                vals+=li
#             vals.sort() #Activate only if you want to sort data
            newEntry = entry[0:-2]
            newEntry.append(-l) #-l means that that amount of tries are finalized and merged
            newEntry.append(vals)
#             print(newEntry)
            merged.append(newEntry)
#             print(merged)
    return merged
        
        
#         if (len(duplicates)==0):
#             duplicates.append(entry)
#         else:
#             if (entry[0] and entry[1] and entry[2] in entries):
                

    
def averageTries(data):
    None

def convertEntry(entry):
    d = entry[4]
    counts = []
    r = [1,2,3,4,5,6]
    for i in r:
        counts.append(d.count(i))
    return counts

def convertEntries(entries):
    res = []
    for e in entries:
        res+=[convertEntry(e)]
    return res

def npConvertEntry(entry):
    return  np.array(convertEntry(entry))

def npConvertEntries(entries):
    return np.array(convertEntries(entries))

def convertAndAverageEntry(entry):
    d = entry[4]
    n = entry[3]*(-1) #That way we can e.g. divide by 2 if attempts is -2
    averagedCounts = []
    r = [1,2,3,4,5,6]
    for i in r:
        averagedCounts.append(d.count(i)/n)
    return averagedCounts

def convertAndAverageEntries(entries):
    res = []
    for e in entries:
        res+=[convertAndAverageEntry(e)]
    return res

def extractNames(entries):
    res = []
    for e in entries:
        name = e[0]
        if (not(name in res)):
            res.append(name)
    return res



yticks = np.arange(0.0,5.5,0.5)
xticks = np.arange(1,7,1)
br = [0.7,0.85,1,1.15,1.3, 1.45]
con = [0.7,0.85,1,1.15,1.3, 1.45]
sat = [0.75,0.9,1,1.2,1.4,1.6]
propertyValues = {
    'br': br,
    'con': con,
    'sat': sat
}
propertyLabels = {
    'br':"Brightness value",
    'con':"Contrast value",
    'sat':"Saturation value"
}

propertyNames = {
    'br':"brightness",
    'con':"contrast",
    'sat':"saturation"
}

# colors = ['orange','blue','green','red','yellow','purple','cyan']
colors = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']
#MSE functions
def mse(entries):
    data = np.array(convertAndAverageEntries(entries))
    avg = np.average(data,axis=0)
    sqDiff = np.power(avg-data,2)
    mse = np.sum(sqDiff)
    return mse

def listAllMse(entries):
    res = []
    maximumMseAndImage = [0.0,'']
    for imName in imgNames:
        imMse = 0.0
        for p in props:
            data = get(entries,imName=imName,prop=p)
            MSE = mse(data)
            imMse+=MSE
            s = f'Image name: {imName}, Property: {propertyNames[p]}, MSE: {"%.3f" % MSE}'
            res.append(s)
        if(maximumMseAndImage[0]<=imMse):
            maximumMseAndImage = [imMse,imName]
        res.append(f'Summed MSE for {imName}: {"%.3f" % imMse}')
    res.append(f'Max MSE: {"%.3f" % maximumMseAndImage[0]} achieved for {maximumMseAndImage[1]}')
    return res
#To create a plot title
def makeTitle(n,stack,average, imname, propname):
    s = ""
    if(stack==True):
        s+= "Stacked bar "
    else:
        s+= "Grouped bar "
    s+= f"plot for n={n} subjects with "
    if (average==True):
        s+= "averaged "
    else:
        s+= "summed "
    s+= f"values\nfor image {imname[2:]} and variated {propertyNames[propname]}"
    return s

'''
Input: 
    entries - Sliced raw data of entries (usually coming from the either the "get" ort he "convertAndAverageEntries" function)
    stack (optional) - Give False if this plot should be merged instead of stacked
Gets raw data and sums up the times each variation was chosen and plots them in stacked bar diagram (for 1 propert and 1 specific image)
'''
def makePlotForSlice(entries, stack=True,average=True):
    if (average == True):
        c = convertAndAverageEntries(entries)
    else:
        c = npConvertEntries(entries)
    
    #Get the names to create a proper stacked bar diagram
    names = extractNames(entries)
    n = len(names) #n = number of subjects
    
    #Get image name
    imname = entries[0][1]
    
    #Get property name
    prop = entries[0][2]
    
    #Assign correct values for x(ticks)
    xNames = propertyValues[prop]
    x = np.array([1,2,3,4,5,6])
#     plt.bar(br,np.sum(c,0),color='blue',alpha=0.5) #Sum up all values across axis-0
    
    #Aesthetic parameters
    width = 0.55
    if (stack==True):
        a = 1.0
        w=0
    else:
        a = 1.0
        w = width/n #To put bars next to each other
    
    bars = []
    for i in range(0,len(c)): #For each entry in c
        if(stack==True):
            if (i==0):
                bar = plt.bar(x,c[i], width,alpha=a)
            else:
                bar = plt.bar(x,c[i], width, bottom=c[i-1],alpha=a)
        elif(stack==False):
            bar = plt.bar(x+(i*w),c[i],width=w,alpha=a)
        bars.append(bar)

    #Set labels
    plt.xticks(x-w/2+width/2,xNames)
    plt.yticks(yticks)
    plt.xlabel(propertyLabels[prop])
    plt.ylabel("Times chosen")
    plt.legend(bars,names)
    title = makeTitle(n,stack, average, imname, prop)
    plt.title(title)
    plt.show()
    
def plotOverallAverageForProperty(entries, p):
    #Process data
    e = get(entries, prop=p)
    c = convertAndAverageEntries(e)
    c = np.array(c)
    c = np.average(c, axis=0)
    names = extractNames(entries)
    n=len(names)
    x = xticks
    xLabels = propertyValues[p]
    
    #Aesthetic parameters
    width = 0.55
    a = 1.0 #alpha
    
    #Plot
#     hlines = plt.hlines(yticks,linestyles='dashed',color='grey',lw=0.5)
    b = plt.bar(x, c, width,alpha=a)
    plt.xticks(x,xLabels)
    plt.yticks(yticks)
    plt.xlabel(propertyLabels[p])
    plt.ylabel("Times chosen")
    plt.title(f"Bar plot for n={n} subjects, for all images\nand variated {propertyNames[p]}")
    plt.show()
    return b

#These are subplotting functions

def plotOverallAverageForPropertyForAxe(entries, p, ax, col='C0'):
    #Process data
    e = get(entries, prop=p)
    c = convertAndAverageEntries(e)
    c = np.array(c)
    c = np.average(c, axis=0)
    names = extractNames(entries)
    n=len(names)
    x = xticks
    xLabels = propertyValues[p]
    
    #Aesthetic parameters
    width = 0.55
    a = 1.0 #alpha
    
    #Plot
    b = ax.bar(x, c, width,alpha=a, color=col)
#     hlines = ax.hlines(yticks,0,1,transform=ax.get_yaxis_transform(),linestyles='dashed',color='grey',lw=0.5,zorder=0)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xticklabels(xLabels)
    ax.set_xlabel(propertyLabels[p])
    ax.set_ylabel("Times chosen")
    ax.set_title(f"Bar plot for n={n} subjects, for all images\nand variated {propertyNames[p]}")
    return b

def plotForImage(entries, imageName, ax, p,col='c0',averageBetweenUsers=False):
    #Process data
    entr = get(entries,imName=imageName) #filter data according to image name
    e = get(entr,prop=p) #e is the filtered data according to property
    c = np.array(convertAndAverageEntries(e)) #c stands for converted entries
    #If users should be consolidated, averafe the converted entries
    if (averageBetweenUsers==True):
        c = np.average(c, axis=0)
    names = extractNames(e)
    n=len(names)
    x=xticks
    xLabels=propertyValues[p]
    MSE = "%.2f" % mse(e)
    
    #Aesthetic parameters
    width=0.55
    w=width
    a = 1.0 #alpha
    
#     print(c)
    #Plot
#     hlines = ax.hlines(yticks,0,1,transform=ax.get_yaxis_transform(),linestyles='dashed',color='grey',lw=0.5,zorder=0)
    if(averageBetweenUsers==True):
        b = ax.bar(x, c, width, alpha=a, color=col)
        ax.set_xticks(x)
        ax.set_xticklabels(xLabels)
    else:
        bs=[]
        w=width/n
#         wHelp = 
        for i in range(0,len(names)):
            name = names[i]
            b = ax.bar(x+(i*w), c[i], w, alpha=a, color=colors[i])
            bs.append(b)
#         ax.set_xticks(x+(w/2)) #Works for n=2
        ax.set_xticks(x-w/2+width/2)
        ax.set_xticklabels(xLabels)
        ax.legend(bs,names)
        
    ax.set_xlabel(f"{propertyLabels[p]}, MSE = {MSE}")
    ax.set_yticks(yticks)
    ax.set_ylabel("Times chosen")
#     ax.set_title(f"Bar plot for n={n} subjects, for all image {imageName[2:]}\nand variated {propertyNames[p]}")
    ax.set_title(f"n={n}, {imageName}, {propertyNames[p]}, avg: {averageBetweenUsers}")
    return b
        
props = ['br','con','sat']
imgNames = ["im1","im2","im3","im4","im5","im6"]
colors = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']

#Takes multiple arguments and converts them to a list
def showAverage(d):
    columns = len(props)
    rows=1
    #Create figure
    fig, axs = plt.subplots(rows,columns,figsize=(columns*5.5,rows*3.5))
    
    for i in range(0,len(axs)):
        ax = axs[i]
        prop = props[i]
        plotOverallAverageForPropertyForAxe(d,prop,ax,colors[i])

def showForImage(d, imName, avg=False):
    columns = len(props)
    rows=1
    #Create figure
    fig, axs = plt.subplots(rows,columns,figsize=(columns*5.5,rows*3.5))
    
    for i in range(0,len(axs)):
        ax = axs[i]
        prop = props[i]
        plotForImage(d, imName, ax, prop, col=colors[i],averageBetweenUsers=avg)
        
def showAll(d, avg=False):
    columns = len(props) #We are going to make a subplot of subplots
    rows = len(imgNames)
    #Create figure
    fig, axs = plt.subplots(rows,columns,figsize=(columns*5.5,rows*4))
#     print(axs)
    fig.tight_layout(pad=5.0)
    for r in range(0,rows):
        imName = imgNames[r] #Row 0 = 1st image
        for c in range(0,columns):
            ax = axs[r,c] #For example: ax = axs[4] for the 2nd row, 2nd column
            prop = props[c] #Iterate properties --> columns
            plotForImage(d, imName, ax, prop, col=colors[c],averageBetweenUsers=avg)


'''
This function makes plots, both average and not, for every image, for every property, based on MERGED DATA
'''
def do(d):
    for im in imgNames:
        showForImage(d,im, avg=True)
        showForImage(d,im, avg=False)