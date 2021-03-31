import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import glob
import csv
import itertools
import random
import datetime
import sys, os
scale1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
scale2 = ['sehr schlecht', 'schlecht', 'mittel', 'gut', 'sehr gut']
scale3 = ['1+', '1', '1-', '2+', '2', '2-', '3+', '3', '3-', '4+', '4', '4-', '5+', '5', '5-', '6+', '6']
scale4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']

images = []


r1 = ["-br-0_7.png","-br-0_85.png","-br-1.png","-br-1_15.png","-br-1_3.png","-br-1_45.png"]
r2 = ["-con-0_7.png","-con-0_85.png","-con-1.png","-con-1_15.png","-con-1_3.png","-con-1_45.png"]
r3 = ["-sat-0_75.png","-sat-0_9.png","-sat-1.png","-sat-1_2.png","-sat-1_4.png","-sat-1_6.png"]
#selectedImage = ['im2', 'im5', 'im6']
selectedImage = ['im2', 'im6']
choices = ["br", "con", "sat"]
varsBr =["0.7", "0.85", "1", "1.15", "1.3", "1.45"]
varsCon =["0.7", "0.85", "1", "1.15", "1.3", "1.45"]
varsSat =["0.7", "0.85", "1", "1.15", "1.3", "1.45"]
randVarsBr= []
randVarsCon= []
randVarsSat= []
preOrderBr = [1, 2, 3, 4, 5, 6]
preOrderCon = [1, 2, 3, 4, 5, 6]
preOrderSat = [1, 2, 3, 4, 5, 6]
randOrderBr = []
randOrderCon = []
randOrderSat = []

ranlen = 6
while len(preOrderBr) > 0:
    nowRand = random.randint(1,ranlen)
    newOrder = preOrderBr.pop(nowRand-1)
    randOrderBr.append(newOrder)
    newVar = varsBr.pop(nowRand-1)
    randVarsBr.append(newVar)
    ranlen -= 1

ranlen = 6
while len(preOrderCon) > 0:
    nowRand = random.randint(1,ranlen)
    newOrder = preOrderCon.pop(nowRand-1)
    randOrderCon.append(newOrder)
    newVar = varsCon.pop(nowRand-1)
    randVarsCon.append(newVar)
    ranlen -= 1

ranlen = 6
while len(preOrderSat) > 0:
    nowRand = random.randint(1,ranlen)
    newOrder = preOrderSat.pop(nowRand-1)
    randOrderSat.append(newOrder)
    newVar = varsSat.pop(nowRand-1)
    randVarsSat.append(newVar)
    ranlen -= 1

"""
print(randOrderBr)
print(randOrderCon)
print(randOrderSat)
print(randVarsBr)
print(randVarsCon)
print(randVarsSat)
"""

for i in randOrderBr:
    for j in range(len(selectedImage)):
        images.append("./images/"+ str(selectedImage[j]) + "/" + str(selectedImage[j]) + str(r1[i-1]))

for i in randOrderCon:
    for j in range(len(selectedImage)):
        images.append("./images/" + str(selectedImage[j]) + "/" + str(selectedImage[j]) + str(r2[i-1]))

for i in randOrderSat:
    for j in range(len(selectedImage)):
        images.append("./images/"+ str(selectedImage[j]) + "/" + str(selectedImage[j]) + str(r3[i-1]))




results1= []
results2= []
results3= []
results4= []



def clicked(method):
    global counter
    global durchlauf


    if(durchlauf == 5):
        # fixing values
        results1.append(results2.pop(0))
        results2.append(results3.pop(0))
        results3.append(results4.pop(0))
        results4.append(method)


        #writing single files, broken because of randomization
        """for j in range(4):
            nr = j + 1
            for image in selectedImage:
                if (nr == 1):
                    verfahren='skala1'
                if (nr == 2):
                    verfahren='skala2'
                if (nr == 3):
                    verfahren='skala3'
                if (nr == 4):
                    verfahren='skala4'
                for procedure in choices:

                    rfls = glob.glob('./data_scales/%s_scales_%s_%s_%s*.csv' % (obsname, image, procedure, verfahren))

                    if len(rfls) > 0:
                        nb = len(rfls)
                    else:
                        nb = 0

                    resultsfile = './data_scales' \
                                  '/%s_scales_%s_%s_%s_%d.csv' % (obsname, image, procedure, verfahren, nb)

                    filename = resultsfile
                    # Force path creation in case of not already existing path
                    if not os.path.exists(os.path.dirname(filename)):
                        try:
                            os.makedirs(os.path.dirname(filename))
                        except OSError as exc:  # Guard against race condition
                            if exc.errno != errno.EEXIST:
                                raise

                    resultswriter = csv.writer(open(resultsfile, 'w'))
                    for lengths in range(len(selectedImage)):
                        for iteration in range(len(r1)):
                            printer = []
                            #printer.append(i+1)
                            for k in range(3):
                                if j == 0:
                                    if (procedure == 'br'):
                                        if (k == 0):

                                            adding = results1[lengths * 18 + randOrderBr[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'con'):
                                        if (k == 1):
                                            adding = results1[lengths * 18 + randOrderCon[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'sat'):
                                        if (k == 2):
                                            adding = results1[lengths * 18 + randOrderSat[iteration] * 3 + k]
                                            printer.append(adding)

                                if j == 1:
                                    if (procedure == 'br'):
                                        if (k == 0):
                                            adding = results2[lengths * 18 + randOrderBr[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'con'):
                                        if (k == 1):
                                            adding = results2[lengths * 18 + randOrderCon[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'sat'):
                                        if (k == 2):
                                            adding = results2[lengths * 18 + randOrderSat[iteration] * 3 + k]
                                            printer.append(adding)
                                if j == 2:
                                    if (procedure == 'br'):
                                        if (k == 0):
                                            adding = results3[lengths * 18 + randOrderBr[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'con'):
                                        if (k == 1):
                                            adding = results3[lengths * 18 + randOrderCon[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'sat'):
                                        if (k == 2):
                                            adding = results3[lengths * 18 + randOrderSat[iteration] * 3 + k]
                                            printer.append(adding)
                                if j == 3:
                                    if (procedure == 'br'):
                                        if (k == 0):
                                            adding = results4[lengths * 18 + randOrderBr[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'con'):
                                        if (k == 1):
                                            adding = results4[lengths * 18 + randOrderCon[iteration] * 3 + k]
                                            printer.append(adding)

                                    if (procedure == 'sat'):
                                        if (k == 2):
                                            adding = results4[lengths * 18 + randOrderSat[iteration] * 3 + k]
                                            printer.append(adding)

                            resultswriter.writerow(printer)"""

                # data print 2; all in one file
        rfls = glob.glob(
            './data_scales/%s_scales_data*.csv' % (obsname))

        if len(rfls) > 0:
            nb = len(rfls)
        else:
            nb = 0

        resultsfile = './data_scales' \
                      '/%s_scales_data%d.csv' % (obsname, nb)

        filename = resultsfile
        # Force path creation in case of not already existing path
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        resultswriter = csv.writer(open(resultsfile, 'w'))
        header = ['name', 'image', 'property', 'variation', 'scale', 'rating', 'attempt']
        resultswriter.writerow(header)

        for imagenr in range(len(selectedImage)):
            if (imagenr == 0):
                imagename = selectedImage[0]
            if (imagenr == 1):
                imagename = selectedImage[1]
            if (imagenr == 2):
                imagename = selectedImage[2]
            procedure = ''
            for varselector in range(len(choices)):
                if (varselector == 0):
                    procedure = 'br'
                if (varselector == 1):
                    procedure = 'con'
                if (varselector == 2):
                    procedure = 'sat'
                for j in range(4):
                    nr = j + 1
                    if (nr == 1):
                        verfahren = '1_10'
                    if (nr == 2):
                        verfahren = 'words'
                    if (nr == 3):
                        verfahren = 'grades'
                    if (nr == 4):
                        verfahren = '1_50'
                    for auspraeg in range(len(r1)):
                        printer = []
                        if j == 0:
                            printer.append(obsname)
                            printer.append(imagename)
                            printer.append(procedure)
                            if procedure == 'br':
                                printer.append(randVarsBr[auspraeg])
                                printer.append(verfahren)
                                adding = results1[imagenr * 18 + auspraeg  * 3 + varselector]

                            if procedure == 'con':
                                printer.append(randVarsCon[auspraeg])
                                printer.append(verfahren)
                                adding = results1[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'sat':
                                printer.append(randVarsSat[auspraeg])
                                printer.append(verfahren)
                                adding = results1[imagenr * 18 + auspraeg * 3 + varselector]
                            printer.append(adding)
                            printer.append(nb)
                            resultswriter.writerow(printer)

                        if j == 1:
                            printer.append(obsname)
                            printer.append(imagename)
                            printer.append(procedure)
                            if procedure == 'br':
                                printer.append(randVarsBr[auspraeg])
                                printer.append(verfahren)
                                adding = results2[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'con':
                                printer.append(randVarsCon[auspraeg])
                                printer.append(verfahren)
                                adding = results2[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'sat':
                                printer.append(randVarsSat[auspraeg])
                                printer.append(verfahren)
                                adding = results2[imagenr * 18 + auspraeg * 3 + varselector]
                            printer.append(adding)
                            printer.append(nb)
                            resultswriter.writerow(printer)

                        if j == 2:
                            printer.append(obsname)
                            printer.append(imagename)
                            printer.append(procedure)
                            if procedure == 'br':
                                printer.append(randVarsBr[auspraeg])
                                printer.append(verfahren)
                                adding = results3[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'con':
                                printer.append(randVarsCon[auspraeg])
                                printer.append(verfahren)
                                adding = results3[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'sat':
                                printer.append(randVarsSat[auspraeg])
                                printer.append(verfahren)
                                adding = results3[imagenr * 18 + auspraeg * 3 + varselector]
                            printer.append(adding)
                            printer.append(nb)
                            resultswriter.writerow(printer)

                        if j == 3:
                            printer.append(obsname)
                            printer.append(imagename)
                            printer.append(procedure)
                            if procedure == 'br':
                                printer.append(randVarsBr[auspraeg])
                                printer.append(verfahren)
                                adding = results4[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'con':
                                printer.append(randVarsCon[auspraeg])
                                printer.append(verfahren)
                                adding = results4[imagenr * 18 + auspraeg * 3 + varselector]

                            if procedure == 'sat':
                                printer.append(randVarsSat[auspraeg])
                                printer.append(verfahren)
                                adding = results4[imagenr * 18 + auspraeg * 3 + varselector]
                            printer.append(adding)
                            printer.append(nb)
                            resultswriter.writerow(printer)





        # row to save is the indices in the vector R, plus one as MLDS package
        # likes indices to start at 1 and not zero.
        exit()

    if ((counter == 36) and (durchlauf == 1)):
        #show buttons for round two; delete buttons from first round
        buttonss.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        buttons.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        buttonm.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        buttong.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        button_sg.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")

        button1.pack_forget()
        button2.pack_forget()
        button3.pack_forget()
        button4.pack_forget()
        button5.pack_forget()
        button6.pack_forget()
        button7.pack_forget()
        button8.pack_forget()
        button9.pack_forget()
        button10.pack_forget()

        durchlauf += 1
        counter = 0

    if ((counter == 36) and (durchlauf == 2)):
        b1p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b1.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b1m.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b2p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b2.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b2m.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b3p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b3.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b3m.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b4p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b4.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b4m.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b5p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b5.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b5m.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b6p.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
        b6.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")


        button_sg.pack_forget()
        buttong.pack_forget()
        buttonm.pack_forget()
        buttons.pack_forget()
        buttonss.pack_forget()

        durchlauf += 1
        counter = 0

    if ((counter == 36) and (durchlauf == 3)):
        slider.pack( padx=5, pady=10,side=tk.TOP, anchor="n")
        slider_button.pack( padx=5, pady=10,side=tk.TOP, anchor="n")

        b1p.pack_forget()
        b1.pack_forget()
        b1m.pack_forget()
        b2p.pack_forget()
        b2.pack_forget()
        b2m.pack_forget()
        b3p.pack_forget()
        b3.pack_forget()
        b3m.pack_forget()
        b4p.pack_forget()
        b4.pack_forget()
        b4m.pack_forget()
        b5p.pack_forget()
        b5.pack_forget()
        b5m.pack_forget()
        b6p.pack_forget()
        b6.pack_forget()

        durchlauf += 1
        counter = 0

    if ((counter == 36) and (durchlauf == 4)):
        slider.pack_forget()
        slider_button.pack_forget()

        final.pack(padx=5, pady=10,side=tk.LEFT, anchor="n")

        durchlauf += 1
        counter = 0
    if (durchlauf == 0):
        durchlauf = 1
        counter = 1
    else:

        if (durchlauf == 1):
            counter += 1
            results1.append(method)

            img_label.img = tk.PhotoImage(file=next(imgs))
            img_label.config(image=img_label.img)
        else:
            if(durchlauf == 2):

                results2.append(method)
                #rating.current(0)
                img_label.img = tk.PhotoImage(file=next(imgs2))
                img_label.config(image=img_label.img)
                counter += 1
            else:
                if (durchlauf == 3):
                    #rating.config(value=scale3)

                    results3.append(method)
                    #rating.current(0)
                    img_label.img = tk.PhotoImage(file=next(imgs3))
                    img_label.config(image=img_label.img)
                    counter += 1
                else:
                    if(durchlauf == 4):
                        #rating.config(value=scale4)
                        results4.append(method)
                        #rating.current(0)
                        img_label.img = tk.PhotoImage(file=next(imgs4))
                        img_label.config(image=img_label.img)
                        counter += 1

obsname= ''
if(obsname==''):
    obsname  = input ('Please input the observer name (e.g. demo): ')

root= tk.Tk()

root.geometry('600x550')


variable = tk.StringVar(root)
variable.set(scale1[0])


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")


imgs = iter(images)
imgs2 = iter(images)
imgs3 = iter(images)
imgs4 = iter(images)

img_label = tk.Label(root)



button1 = tk.Button(root, text="1 ", command=lambda: clicked('1'))
button2 = tk.Button(root, text="2 ", command=lambda: clicked('2'))
button3 = tk.Button(root, text="3 ", command=lambda: clicked('3'))
button4 = tk.Button(root, text="4 ", command=lambda: clicked('4'))
button5 = tk.Button(root, text="5 ", command=lambda: clicked('5'))
button6 = tk.Button(root, text="6 ", command=lambda: clicked('6'))
button7 = tk.Button(root, text="7 ", command=lambda: clicked('7'))
button8 = tk.Button(root, text="8 ", command=lambda: clicked('8'))
button9 = tk.Button(root, text="9 ", command=lambda: clicked('9'))
button10 = tk.Button(root, text="10", command=lambda: clicked('10'))

button_sg = tk.Button(root, text="sehr gut", command=lambda:clicked("sehr gut"))
buttong = tk.Button(root, text="gut", command=lambda:clicked("gut"))
buttonm = tk.Button(root, text="mittel", command=lambda:clicked("mittel"))
buttons = tk.Button(root, text="schlecht", command=lambda:clicked("schlecht"))
buttonss = tk.Button(root, text="sehr schlecht", command=lambda:clicked("sehr schlecht"))

b1p = tk.Button(root, text="1+", command=lambda: clicked('1+'))
b1 = tk.Button(root, text="1 ", command=lambda: clicked('1'))
b1m = tk.Button(root, text="1-", command=lambda: clicked('1-'))
b2p = tk.Button(root, text="2+", command=lambda: clicked('2+'))
b2 = tk.Button(root, text="2 ", command=lambda: clicked('2'))
b2m = tk.Button(root, text="2-", command=lambda: clicked('2-'))
b3p = tk.Button(root, text="3+", command=lambda: clicked('3+'))
b3 = tk.Button(root, text="3 ", command=lambda: clicked('3'))
b3m = tk.Button(root, text="3-", command=lambda: clicked('3-'))
b4p = tk.Button(root, text="4+", command=lambda: clicked('4+'))
b4 = tk.Button(root, text="4 ", command=lambda: clicked('4'))
b4m = tk.Button(root, text="4-", command=lambda: clicked('4-'))
b5p = tk.Button(root, text="5+", command=lambda: clicked('5+'))
b5 = tk.Button(root, text="5 ", command=lambda: clicked('5'))
b5m = tk.Button(root, text="5-", command=lambda: clicked('5-'))
b6p = tk.Button(root, text="6+", command=lambda: clicked('6+'))
b6 = tk.Button(root, text="6 ", command=lambda: clicked('6'))

#slider
slider = tk.Scale(root, from_=1, to_=50, orient=tk.HORIZONTAL)
slider_button = tk.Button(root, text="next", command =lambda: clicked(slider.get()))

final = tk.Button(root, text="end", command=lambda: clicked(slider.get()))

counter = 1
durchlauf = 1

img_label.img = tk.PhotoImage(file=next(imgs))
img_label.config(image=img_label.img)
img_label.pack(padx=10, pady=10, side=tk.BOTTOM )

button1.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button2.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button3.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button4.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button5.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button6.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button7.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button8.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button9.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")
button10.pack(padx=5, pady=10, side=tk.LEFT, anchor="n")

root.mainloop()


