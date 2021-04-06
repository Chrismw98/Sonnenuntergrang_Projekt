# Auswirkungen von variierenden Abstufungen von Helligkeit, Kontrast und Saturation auf die wahrgenommene Ästhetik verschiedener Bilder von Sonnenuntergängen & Auswirkungen von unterschiedlichen Rating-Skalen auf die Bewertung des selben Bildes

## Matti Zinke, Christian Wohlhaupt, Bozhidar Rusev, Iliya Velev

### Seminar: Visuelle Wahrnehmung beim Menschen und Bildqualität - WiSe 2020/21

_Wir beziehen uns des öfteren auf den ersten bzw. zweiten Teil des Projekts. Der erste Teil ist der mit variierenden Abstufungen von Helligkeit, Kontrast und Saturation. Der zweite Teil ist der mit den unterschiedlichen Bewertungsskalen._

Eine Liste mit allen benutzten Bibliotheken und Packages


```python
#Zur Erstellung des veränderten Bildmaterials
from PIL import Image, ImageEnhance

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np
import math
%matplotlib inline

import os
import errno

#Weitere Imports zur Datenauswertung des ersten Teils (mit Plots)
import re
from os import listdir
from os.path import isfile, join
import seaborn as sns

#Weitere Imports für die Datenauswertung des ersten Teils mit Heatmaps
import csv
import pandas as pd
from pandas import Series,DataFrame
import glob

```
<!---
    
    Bad key "text.kerning_factor" on line 4 in
    D:\ProgramData\Anaconda3\lib\site-packages\matplotlib\mpl-data\stylelib\_classic_test_patch.mplstyle.
    You probably need to get an updated matplotlibrc file from
    https://github.com/matplotlib/matplotlib/blob/v3.1.2/matplotlibrc.template
    or from the matplotlib source distribution
    
-->

```python
#Dieser Import ist nur um Plotting Funktionen schnell und übersichtlich hier einbringen zu können
import Datenauswertungsfunktionen as daf
import Heatmapfunktionen as hmf
import Skalenfunktionen as skf
```


```python
#open all csv files for skalas
path =r'.\data_scales'
filenames = glob.glob(path + "/*.csv")
df = pd.concat(map(pd.read_csv, filenames))
```

## 1. Einleitung

Sonnenuntergänge werden allgemein als ein *schönes* Naturphänomen angesehen. Aber was macht diese *Schönheit* auf einem Bild eines Sonnenuntergangs aus? Eigenschaften wie Helligkeit, Kontrast und Saturation sind allzu bekannt und haben eine hohe Auswirkung auf die *Schönheit* eines Bildes für einen Betrachter. Verändern wir diese Eigenschaften (durch Intensivierung oder Abschwächung) beobachten wir eine entsprechende Änderung der wahrgenommenen Ästhetik. Wir versuchen diese subjektiv wahrgenommene Ästhetik zu bemessen. Für unser Projekt kamen somit zwei **wissenschaftliche Fragestellungen** in Betracht:
1. Welchen Effekt haben Helligkeit, Kontrast und Saturation jeweils auf die wahrgenommene Ästhetik eines Bildes von einem Sonnenuntergang?
2. Welchen Effekt hat die Wahl der Skala auf die Bewertung der Ästhetik eines Bildes von einem Sonnenuntergang?

Um das zu schaffen haben wir paarweise Bildvergleiche auf unseren Bilddaten, sowie eine Skalenbewertung vereinzelnter Bilder durchgeführt.
Folgende **Hypothesen** haben wir untersucht:
1. Kontrast und Saturation sollten eine höhere wahrgenommene Ästhetik als Helligkeit bewirken.
2. Die Ergebnisse nähern sich einer optimalen Abstufung (je Eigenschaft) an.
3. Eine negative Saturation bewirkt eine niedriger wahrgenommene Ästhetik.
4. Man tendiert auf bekannten Bewertungsskalen strenger zu bewerten.


```python

```

## 2. Experimentelles Design

### Teil 1
Im ersten Teil haben wir mit 6 selbstgemachten Bildern von Sonnenuntergängen gearbeitet. Für jedes Bild haben wir pro Eigenschaft (Helligkeit, Kontrast, Saturation) jeweils 6 Abstufungen ausgewählt und untereinander verglichen. Die Werte beschreiben den Multiplikationsfaktor, welcher im Funktionsaufruf der _PIL_-Bibliothek für die jeweilige Eigenschaft übergeben wird. Der Wert 1 steht somit für das Originalbild. Der Wert 0.5 bei Helligkeit würde also bedeuten _"die Hälfte der Helligkeit des Originalbildes"_. Die Werte für die wir uns entschieden haben sind:
* Helligkeit: 0.7, 0.85, 1, 1.15, 1.3, 1.45
* Kontrast: 0.7, 0.85, 1, 1.15, 1.3, 1.45
* Saturation: 0.75, 0.9, 1, 1.2, 1.4, 1.6

_Bemerkung:_ Bei der Saturation gibt es keine gleichmäßigen Schritte. Das liegt daran, dass wir nach ausgiebigem Testen beobachtet haben, dass gleichmäßige Schritte bei der Saturation zu große bzw. zu kleine Unterschiede ausmachen, die für das menschliche Auge und die Ästhetik zu extrem bzw. unerkennbar sind.

### Teil 2
Im zweiten Teil des Experiments haben wir Bild 2 und Bild 6 verwendet. Dort haben wir die Bilder ästhetisch mit folgenden Messkalen bewertet (schlechteste Bewertung - beste Bewertung):
* Nominalskala: 1 bis 10
* Ordinalskala: sehr schlecht - schlecht - mittel - gut - sehr gut
* Schulnotenskala: 6 bis 1+
* Nominalskala: 1 bis 50

Bild 2 und 6 wurden immer abwechselnd gezeigt und hatten paarweise die selbe Ausprägung. Die Reihenfolge in dem diese Ausprägungen gezeigt wurden unterscheidet sich immer für br, con und sat. Zur Auswahl der Bewertung gab es für die Skalen 1 bis 10, sehr schlecht bis sehr gut und 1+ bis 6 Buttons zur schnellen Auswahl, für die Skale 1 bis 50 einen Schieberegler für eine bessere Übersichtlichkeit. Die Buttons für die Bewertung des Bildes waren dabei direkt links neben dem gezeigten Bild.



```python

```

Die folgende Abbildung zeigt alle im ersten Teil verwendete Stimuli. Hierbei steht **br** für Helligkeit, **con** für Kontrast und **sat** für Saturation. Die Bilder sind von 1 bis 6 durchnummeriert.


```python
brValues = [0.7,0.85,1,1.15,1.3, 1.45] #0.15 Schritte
contrValues = [0.7,0.85,1,1.15,1.3, 1.45] #0.15 Schritte
satValues = [0.75,0.9,1,1.2,1.4,1.6] #Angepasst
pVals = {
    'br': brValues,
    'con': contrValues,
    'sat': satValues
}

def showDataForImage(imageName):
    fig = plt.figure(figsize=(18, 25))
    fig.text(0.115, 0.5, imageName, va='center', rotation='vertical')
    for i, propertyName in enumerate(['br','con','sat']):
        propertyValues = pVals[propertyName]
        
        for j, val in enumerate(propertyValues):
            v = str(val).replace('.','_')
            im = np.array(Image.open(f'./images/{imageName}/{imageName}-{propertyName}-{v}.png'))
            plt.subplot(6,3,i*6+j+1)
            plt.imshow(im)
            plt.axis('off')
            plt.title(f"{propertyName}: {propertyValues[j]}")
                      
for imName in ['im1','im2','im3','im4','im5','im6']:
    showDataForImage(imName)
```


    
![png](images/output_16_0.png)
    



    
![png](images/output_16_1.png)
    



    
![png](images/output_16_2.png)
    



    
![png](images/output_16_3.png)
    



    
![png](images/output_16_4.png)
    



    
![png](images/output_16_5.png)
    


Für den ersten Teil des Experiments haben wir für jedes Bild und Ausprägung einen paarweisen Vergleich der Abstufungen durchgeführt. Dabei muss die Versuchsperson das optisch bzw. ästhetisch ansprechendere Bild wählen. Da wir 6 Abstufungen benutzen ergeben sich $6 \choose 2$ = 15 Vergleiche pro Eigenschaft.
Da wir 3 Eigenschaften pro Bild und 6 Bilder haben, ergeben sich $15*3*6=270$ Vergleiche pro Versuchsdurchlauf. Jeder hat den Versuch drei Mal durchgeführt. Somit ergaben sich 810 paarweise Vergleiche pro Person, was insgesamt ca. 30-40 Minuten beansprucht hat. Das Experiment wurde von allen 4 Gruppenmitgliedern durchgeführt.

## 3. Ergebnisse

### Teil 1

### Barplots
Nachdem das Experiment durchgeführt wird, werden für die Barplots alle Daten konsolidiert und in eine große Liste gespeichert. Im 1. Teil wurde dies aufwendiger gemacht, als gebraucht - im 2. Teil haben wir daraus gelernt und die .csv Daten effizienter und unaufwendiger abgespeichert.<br>
Da der Versuch auf Vergeleich von jeweils 2 Bildern basiert, muss aufgezählt werden wie oft jedes Bild gewählt wurde.<br>
* Minimaler Wert eines Bildes: 0 - das Bild wurde nie gewählt<br>
* Maximaler Wert eines Bildes: 5 - das Bild wurde bei jedem Vergleich gewählt, in dem es gezeigt wurde

Die absoluten Häufigkeiten werden dann über die Anzahl der Versuche gemittelt.<br>
Bei den folgenden Plots sind zum Einen die Plots aller Versuchspersonen unter sich gemittelt zu sehen und zum Anderen die nicht unter uns gemittelten Plots.<br>
**Anmerkung:** n = 4 Versuchspersonen, Anzahl Durchläufe pro Person = 3


```python
#Daten aufbereiten

#Erstelle Liste von allen .csv Dateinamen im <data> folder
fileNames = daf.listFiles()

#Extrahiere und konsolidiere alle Daten aus den .csv Dateien in eine Liste aus Einträgen
allData = daf.consolidate(fileNames)

#Fasse mehrere Versuchs-einträge durch Konkatenation der Wertelisten in jeweils einen Eintrag zusammen
mergedData = daf.mergeTries(allData)
```

    D:\Documents\Uni Kurse\WS 20-21\Perception & Image Quality Seminar\Sonnenuntergang Projekt\Dokumentation - Git\Datenauswertungsfunktionen.py:133: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
      nd = np.array(d) #To work with np
    D:\Documents\Uni Kurse\WS 20-21\Perception & Image Quality Seminar\Sonnenuntergang Projekt\Dokumentation - Git\Datenauswertungsfunktionen.py:140: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
      toMerge = np.array([entry]) #ToMerge list only consists of current entry
    <string>:6: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
    

Die x-Achse besteht aus den einzelnen Abstufungen der jeweiligen Eigenschaft. Die y-Achse beschreibt die Häufigkeit der Auswahl einer bestimmten Abstufung und nimmt somit Werte von 0 bis 5 ein (minimal und maximal erreichbarer Wert). Im Titel ist die Anzahl **n** der Versuchspersonen, der **Bildname**, die betrachtete **Eigenschaft** und der Parameter **avg** zu sehen. Letzterer sagt aus, ob die Daten unter den Versuchspersonen gemittelt wurden oder nicht (avg = average). <br>
Es sind oftmals Trends zu erkennen, was man an den höchsten Balken an einem Bild erkennen kann. Dies bedeutet demnach dass die am meisten gewählte Abstufung einer Eigenschaft auch am ästhetisch ansprechensten interpretiert wurde. Diese variieren von Bild zu Bild, aber auch von Person zu Person, man kann individuelle Favoriten der Personen somit rauslesen.

**Anmerkung:** Auf der x-Achsen Beschriftung ist zudem der MSE zu sehen, welcher nur für interne Zwecke benutzt wurde. Um genauer zu sein, haben wir den MSE als Abweichung der Werte zwischen den Teilnehmern benutzt, um herauszufinden welche Bilder wir im 2. Teil des Experiments benutzen können. Ein hoher Wert bedeutet, dass die Teilnehmer sich nicht einig waren und macht dieses Bild dann zum optimalen Kandidaten für die Untersuchung mit verschiedenen Skalen.


```python
#Alle Barplots für den 1. Teil anzeigen, sowohl gemittelt als auch pro Person
daf.do(mergedData)
```


    
![png](images/output_23_0.png)
    



    
![png](images/output_23_1.png)
    



    
![png](images/output_23_2.png)
    



    
![png](images/output_23_3.png)
    



    
![png](images/output_23_4.png)
    



    
![png](images/output_23_5.png)
    



    
![png](images/output_23_6.png)
    



    
![png](images/output_23_7.png)
    



    
![png](images/output_23_8.png)
    



    
![png](images/output_23_9.png)
    



    
![png](images/output_23_10.png)
    



    
![png](images/output_23_11.png)
    


Obwohl die Daten von Bild zu Bild variieren, lassen sich doch einige Trends erkennen. Wenn wir alle Daten über die Bilder mitteln, bekommen wir somit einen groben Trend unserer Daten. Dabei stellen sich folgende Abstufungen in den Vordergrund:
* Helligkeit: Die Abstufung 1.15
* Kontrast: Die Abstufungen 1.15 und 1.3
* Saturation: Die Abstufungen 1.2, **1.4** und 1.6

Man kann erkennen, dass es bei der Helligkeit einen eindeutigen Sieger gibt. Beim Kontrast sieht man, dass die Häufigkeit der Wahl der Abstufung 1.45 wieder sinkt. Das zeigt, dass Bilder von Sonnenuntergängen mit einem sehr hohen Kontrast eher schlechter bewertet werden. Das liegt vielleicht daran, dass die Bilder als "fake" angesehen werden. Bei der Saturation ist klar zu erkennen, dass die höheren Werte auch bessere Ästhetik mit sich bringen. Das haben wir als Gruppe auch direkt bei der Durchführung des Experimentes gemerkt.


```python
daf.showAverage(mergedData)
```


    
![png](images/output_25_0.png)
    


### Heatmaps
Wir haben heatmaps benutzt um nach Trends zu suchen und um Ausreißer zu neutralisieren.<br>
Dabei haben wir unterschidliche Versionen von Heatmaps untersucht, um unterschiedliche Perspektiven für unsere Daten zu bekommen:

|  | je Versuchsperson | Alle Versuchspersonen |
| --- | --- | --- |
| **je Bild** | 1. Heatmap | 2. Heatmap |
| **Alle Bilder** | 3. Heatmap | 4. Heatmap |

Dabei wird immer nach Eigenschaft unterschieden.

### Absolute Auswahlhäufigkeiten jeweils einer Versuchsperson, je Eigenschaft, je Bild

Hier sieht man wie oft jede Versuchsperson eine Ausprägung einer anderen vorgezogen hat. Dabei steht steht die Diagonale leer, da man ein Bild nicht mit sich selbst verglichen hat. Der Vorteil der Heatmaps ist, dass man präzise erkennen kann wofür sich jeder entschieden hat.

Die __maximale absolute Häufigkeit__ ist __3__, weil alle 3 Experimentdurchführungen in einer Heatmap kombiniert sind.


```python
hmf.f1()
```


    
![png](images/output_29_0.png)
    



    
![png](images/output_29_1.png)
    



    
![png](images/output_29_2.png)
    



    
![png](images/output_29_3.png)
    



    
![png](images/output_29_4.png)
    



    
![png](images/output_29_5.png)
    



    
![png](images/output_29_6.png)
    



    
![png](images/output_29_7.png)
    



    
![png](images/output_29_8.png)
    



    
![png](images/output_29_9.png)
    



    
![png](images/output_29_10.png)
    



    
![png](images/output_29_11.png)
    



    
![png](images/output_29_12.png)
    



    
![png](images/output_29_13.png)
    



    
![png](images/output_29_14.png)
    



    
![png](images/output_29_15.png)
    



    
![png](images/output_29_16.png)
    



    
![png](images/output_29_17.png)
    



    
![png](images/output_29_18.png)
    



    
![png](images/output_29_19.png)
    



    
![png](images/output_29_20.png)
    



    
![png](images/output_29_21.png)
    



    
![png](images/output_29_22.png)
    



    
![png](images/output_29_23.png)
    


### Absolute Auswahlhäufigkeiten für alle Versuchsperson, je Eigenschaft, je Bild

Hier kann man sehen wie oft alle Versuchspersonen zusammengerechnet jede Ausprägung im Experiment gewählt haben. 

Die __maximale absolute Häufigkeit__ ist __12__, weil alle 3 Versuche von alle 4 Versuchspersonen kombiniert sind (3 * 4 = 12).


```python
hmf.f2()
```


    
![png](images/output_32_0.png)
    



    
![png](images/output_32_1.png)
    



    
![png](images/output_32_2.png)
    



    
![png](images/output_32_3.png)
    



    
![png](images/output_32_4.png)
    



    
![png](images/output_32_5.png)
    


### Absolute Auswahlhäufigkeiten jeweils einer Versuchsperson, je Eigenschaft, für alle Bilder

Hier kann man sehen wie oft jeweils eine Versuchsperson jede Ausprägung für alle Bilder im Experiment gewählt hat. So kann man persönliche Vorlieben entdecken und Ausreißer teilweise neutralisieren

Die __maximale absolute Häufigkeit__ ist  __18__, weil alle 3 Versuche für alle 6 Bilder kombiniert sind (3 * 6 = 18).



```python
hmf.f3()
```


    
![png](images/output_35_0.png)
    



    
![png](images/output_35_1.png)
    



    
![png](images/output_35_2.png)
    



    
![png](images/output_35_3.png)
    


### Absolute Auswahlhäufigkeiten für alle Versuchspersonen, je Eigenschaft, für alle Bilder

Hier kann man sehen wie oft alle Versuchspersonen zusammengerechnet jede Ausprägung und für alle Bilder im Experiment gewählt haben.

Die __maximale absolute Häufigkeit__ ist __72__, weil alle 3 Versuche für alle 4 Versuchpersonen für alle 6 Bilder kombiniert sind (3 * 4 * 6 = 72).


```python
hmf.f4()
```


    
![png](images/output_38_0.png)
    


### Schönstes Bild

Hier kann man sehen wie oft alle Versuchspersonen jeden Wert der drei Variablen _(Brightness, Contrast, Saturation)_ für jedes Image gewählt haben.

Ziel: Beste "Version" von jedem Image finden.

Die __absolute Häufigkeit__ = __60__, weil alle 3 Versuche der 4 Versuchpersonen und der Vergleich mit den 5 anderen Ausprägungen von dem Image kombiniert sind (3 * 4 * 5 = 60).<br>
Die höchste Zahl im Diagramm stellt hierbei die am schönsten wahrgenommene Ausprägung eines Bildes dar.


```python
hmf.bestImage()
```


    
![png](images/output_41_0.png)
    



    
![png](images/output_41_1.png)
    



    
![png](images/output_41_2.png)
    



    
![png](images/output_41_3.png)
    



    
![png](images/output_41_4.png)
    



    
![png](images/output_41_5.png)
    


### Absolute Häufigkeiten aller Personen, und Eigenschaften für Bild 2 zusammengerechnet
In unserer Präsentation hatten wir Bild 2 als unser interessantestes und schönstes Bild präsentiert. Das liegt daran, dass wir hier interessanterweise beim Kontrast nicht eine Lieblingsausprägung hatten, sondern zwei. Diese waren 1.15 und 1.3, wie man in folgenden Diagrammen erkennen kann. Für Helligkeit gab es hier die 1.15 und für Saturation die 1.4.
Vielleicht würde sich das mit mehr Personen ändern.


```python
hmf.im2_1()
```


    
![png](images/output_43_0.png)
    


### Absolute Häufigkeiten aller Personen für Bild 2 je Eigenschaft zusammengerechnet
Einfach zur Veranschaulichung der Daten für das 2. Bild.<br>
Man erkennt in den folgenden Heatmaps auch gut wieso die vorherigen diese Werte annehmen, da die Reihen dafür zusammengerechnet wurden.


```python
hmf.im2_2()
```


    
![png](images/output_45_0.png)
    


### Teil 2 Skalenbewertung
Wir haben die Ergebnisse von der Skalenbewertung mit Balkendiagrammen für die Nominalenskalen (1-10, 1-50) und mit Heatmaps für die Ordinal- und Schulnotenskalen dargestellt. Bei den Nominalenskalen haben wir zuerst für jede Versuchperson und dann für die ganze Gruppe ein Balkendiagramm für ein Stimuli. Mit den Heatmaps für die Ordinal- und Schulnotenskalen haben wir es nur für die ganze Gruppe dargestellt, da sondern man die Unterschiede nur für eine Versuchperson nicht erkennen kann.

*Anmerkung: Leider gab es mit Seaborn in diesem Abschnitt einige Probleme mit Subplots, weswegen einige der Plots untereinander stehen*

### Nominalskalen (1-10) und (1-50) für die ganze Versuchsgruppe

Der Aufbau dieses Graphen ist ähnlich zu den vorherigen. Im Gegensatz zu den einzelnen Bewertungen zeigen diese Graphen nur den Durchschnitt. Die x-Achse gibt erneut die Veränderung zum Orignal an und die y-Achse die Bewertung. Links ist die Art der Skala ablesbar, unter dem Graphen welches Bild bewertet wurde und über jedem Graphen welche Art von Ausprägung untersucht wurde. Die Farbe der Säulen ist irrelevant und gilt nur zur einfacheren Unterscheidung der einzelnen Säulen.

Für die Helligkeit von Bild 2 sind die angenommenen Werte von 1.0 oder 1.15 durch alle Skalen hinweg die Beste. Bei der Saturation dieses Bildes teils bei einigen Graphen einen kleinen Favoriten, den Wert 1.4. Jedoch ist erkennbar, dass der 1.6 Wert danach nicht mehr gut ist. Bei dem Kontrast von Bild 2 gibt es keinen optimalen Wert, aber 0.7 hat durchschnittlich eine leicht bessere Bewertung.

Bei Bild 6 lassen sich etwas mehr optimale und schlechte Veränderungen des Bildes ablesen. Für die Helligkeit bleibt es bei zwei optimalen Werten, jedoch verschieben sich diese um eine Abstufung nach oben im Vergleich zu Bild 2 auf 1.15-1.3. Die Bewertung der Saturation sieht im Gegensatz zu Bild 2 sehr viel anders aus und viele Werte sind gleich gut bewertet, sticht der Wert 1.4 leicht heraus. Zuletzt kommt noch der Kontrast von Bild 6. Dieser ist etwas ungewöhnlich, da man normalerweise eine grobe gaußsche Verteilung erwarten würde. Es gibt aber vier circa gleich gute Werte und zwei Werte die klar schlechter bewertet wurden, 0.85 und besonders 1.3. Vor allem, sind von den vier Werten die beiden Ränder etwas besser bewertet worden. 


```python
skf.nominalAll()
```


    
![png](images/output_49_0.png)
    



    
![png](images/output_49_1.png)
    



    
![png](images/output_49_2.png)
    



    
![png](images/output_49_3.png)
    



    
![png](images/output_49_4.png)
    



    
![png](images/output_49_5.png)
    



    
![png](images/output_49_6.png)
    



    
![png](images/output_49_7.png)
    



    
![png](images/output_49_8.png)
    



    
![png](images/output_49_9.png)
    



    
![png](images/output_49_10.png)
    



    
![png](images/output_49_11.png)
    


### Nominalskalen (1-10) und (1-50) für jede Versuchsperson




Diese Graphen zeigen die Bewertungen der einzelnen Teilnehmer für die Skalen 1-10 und 1-50. Auf der x-Achse können die die Veränderungen zum Originalwert abgelesen werden und an der y-Achse die gegebene Bewertung durch den Teilnehmer. Über dem Graphen steht die untersuchte Ausprägung und unter dem Graphen das dazugehörige Bild. Am linken Rand ist die Art der Skala ablesbar und rechts die zur Farbe gehörige Person.

Für manche Personen ist eine Veränderung einer Ausprägung mit die beste, für manche aber die komplett am schlechtesten bewertete. Das ist der Fall bei der Saturationsanalyse von Bild 2 auf der 1-10 Skala bei 1.0. Für grün ist es der schlechteste Wert überhaupt, für gelb hingegen mit der am besten bewertete.  Selten verändert sich auch die Bewertung einer einzelnen Personen zwischen zwei Skalen komplett, wie es vor allem bei dem Kontrast bei Bild 2 zu sehen ist. Bei manchen Personen hat die Skala jedoch auch einen Unterschied gemacht. Blau bewertet durchschnittlich die 1-10 Skala um ca. 20% besser, bei manchen Ausprägungen mehr und bei manchen weniger. 


```python
skf.nominalEach()
```


    
![png](images/output_52_0.png)
    



    
![png](images/output_52_1.png)
    



    
![png](images/output_52_2.png)
    



    
![png](images/output_52_3.png)
    



    
![png](images/output_52_4.png)
    



    
![png](images/output_52_5.png)
    



    
![png](images/output_52_6.png)
    



    
![png](images/output_52_7.png)
    



    
![png](images/output_52_8.png)
    



    
![png](images/output_52_9.png)
    



    
![png](images/output_52_10.png)
    



    
![png](images/output_52_11.png)
    


### Ordinal- und Schulnotenskala für die ganze Versuchsgruppe

Abgebildet sind Heatmaps für die Bewertung der Skalen mit Wörtern von sehr gut bis sehr schlecht und für die Bewertung mit Schulnoten. Es werden erneut die Skalen abwechselnd gezeigt, erst die Heatmaps zu Bild 2 und danach zu Bild 6. Das bewertete Bild steht auch über den Graphen. Unter dem Graphen steht die untersuchte Art. An der x-Achse sind wie zuvor auch die Veränderungen zum Original abgetragen und an der y-Achse die gegebene Bewertung. Daraus entsteht ein Feld und in den einzelnen Zellen ist die Häufigkeit der gegebenen Bewertung. Auf der rechten Seite ist die Erklärung der Farben der einzelnen Zellen.

Generell gibt es auch andere Unterschiede zwischen diesen Skalen und den vorherigen, so wird die Skala mit sehr gut – sehr schlecht öfters komplett gut oder schlecht bewertet als die anderen. Das kann aber an dem kleineren Wertebereich liegen. In der Skala der Schulnoten wurde für Bild 2 die „Bestnote“ nicht einmal verteilt, die schlechteste jedoch häufiger. Andersherum ist es bei Bild 6, dort wurde die Note 6 selten verteilt, die Note 1+ aber häufiger. Um nochmal die Anomalie von Bild 6, Kontrast mehr auszuwerten, haben zwei Personen eine gute Bewertung für dieses Bild abgegeben, die anderen Beiden jedoch eine eher schlechte. Das kann auch eventuell daherkommen, dass man sich einen Favoriten nimmt und weiß, dass dieser noch nicht erreicht wurde und deswegen das Bild, was ähnlich dazu ist, schlechter bewertet. Ein gemeinsamer Trend zwischen beiden Bildern ist, dass eine erhöhte Saturation um 1.4 das Bild am besten aussehen lässt. Generell kann noch gesagt werden, dass einige Personen eher höher bewerten, andere eher geringer. 


```python
skf.ordinal()
```


    
![png](images/output_55_0.png)
    



    
![png](images/output_55_1.png)
    



    
![png](images/output_55_2.png)
    



    
![png](images/output_55_3.png)
    


### Zusammenfassung Skalenbewertung

Generell gibt es keine signifikanten Unterschiede zwischen der Bewertung desselben Bildes auf verschiedenen Skalen. Teils gibt es zwar geringe Unterschiede zwischen den einzelnen Skalen, wie Beispiels bei Bild 2, Saturation, jedoch sind diese nicht aussagekräftig genug. Die Bilder selbst wurden aber unterschiedlich bewertet, Bild 6 hat eine um circa 20 % bessere Bewertung als Bild 2. Jedoch bleibt die beste Verstärkung einer Ausprägung nicht zwingend dieselbe. So ist zum Beispiel für Bild 2 der maximal untersuchte Kontrast mit der schlechteste Wert, für Bild 6 jedoch mit der Beste. Demnach ist erkennbar, dass für verschiedene Sonnenuntergänge andere Bearbeitungen notwendig sind, um die wahrgenommene Schönheit zu erhöhen. Es gibt auch kein klar am besten bewertetes Bild bzw. Ausprägung. 

## 4. Diskussion

Uns ist klar geworden, dass wir für eine bessere Auswertung mehr Daten benötigen. Einerseits mehr Durchläufe pro Person, andererseits würden mehr Testpersonen es auch erleichtern. Zudem wäre es gut, bei dem 2. Teil des Experiments mehr Bilder in den Vergleich einzubeziehen, nicht nur die zwei. 

Uns ist auch aufgefallen, dass jeder Sonnenuntergang sehr individuell ist. Es gibt viele Faktoren die in die generelle Bewertung einfließen und die sich mit dem Verstärken einer Ausprägung ebenfalls ändern. Dazu gehören:
* Erscheinen von Wolken
* Sichtbarkeit der Sonne
* Höhe der Sonne am Horizont
* Existenz eines Motivs (z.B. Stadt, Wasser)
* Farbe des Sonnenuntergangs

Einige Bilder wurden dann bei der Saturation und Helligkeit so grell, dass es nicht mehr schön war, obwohl es bei den anderen Bildern zu positiven Trends gekommen ist. Das ist auch in der Bewertung dieser Bilder erkennbar.
Bei der nächsten Durchführung eines solchen Versuchs würden wir deswegen die Bilder vorher schon vorher Gruppieren und die Ausprägungen auf die Gruppen anpassen.

Dadurch können wir keine klaren Antworten auf unsere aufgestellten Hypothesen liefern. In einigen Bildern mögen unsere angenommenen Thesen zwar übereinstimmen, jedoch nicht in allen. Von den Hypothesen, die sich auf die Ausprägungen beziehen, sind die auf die Saturation bezogenen am meisten verifizierbar, jedoch können wir aufgrund unserer vorhandenen, geringen Daten keine wirkliche Aussage treffen.


Die Bilder wurden meistens ähnlich bewertet, jedoch ist eine persönliche Präferenz erkennbar. Einige von uns bevorzugen genau Abstufung in einem Bild, ein anderer eine andere. Jedoch auf den Durchschnitt von uns gesehen, lässt sich ein Trend sehen, dass alles sehr ähnlich bewertet wurde.

### Mögliche Probleme

1. **Experiment Teil 1:** Man wartet immer auf sein Lieblingsbild und bewertet dieses besser bzw. lässt dieses immer gewinnen. Zudem kennen wir unsere Bilder allgemein sehr gut und wissen schon zuvor welches als nächstes kommen würde und schränken unsere Bewertung dadurch ein.<br>**Lösung:** Mehr Versuchspersonen, eventuell statt eine ganze Bildreihenfolge auf einmal (<font color='green'>im2_br</font> - <font color='green'>im2_con</font> - <font color='green'>im2_sat</font>) zu bewerten, für mehrere Bilder diese untereinander mischen (beispielsweise <font color='red'>im1_br</font> - <font color='green'>im2_con</font> - <font color='blue'>im3_sat</font> - <font color='red'>im1_con</font> - <font color='blue'>im3_br</font> - <font color='green'>im2_br</font> - <font color='red'>im1_sat</font> - <font color='blue'>im3_con</font>) - <font color='green'>im2_sat</font>.


2. **Skalen-Versuch:** Man hat immer nur die zwei Bilder gesehen und dadurch mehr zwischen diesen Bildern einzelnd verglichen und nicht alleinstehend nur nach wahrgenommener Ästehtik. Hier würde eine höhere Bilderanzahl auch helfen. Der verwendete Schiebereglerfür die Skala von 1 bis 50 bringt zusätzlich auch kleine Ungenauigkeiten herein. Die Skala ist eher kurz, wurde kleine Veränderungen teils große Auswirkung auf die Bewertung hat. Manche Skalen bestehen nur aus Wörtern, manche aus Zahlen was teils die Auswertung uns etwas erschwert hat.<br>**Lösung:** Bei einer erneuten Untersuchung würden wir auch die Reihenfolge des Auftretens der Skalen ändern, da diese bei dem jetzigen Versuch fix war. Dadurch kann es auch zur leicht besseren Bewertung der Skala 1-10 kommen, da diese als erstes abgefragt wurde und durchschnittlich auch leicht besser bewertet wurde. Das kann natürlich auch an anderen Gründen liegen, mit unserer Untersuchung können wir das jedoch nicht belegen.


3. **Skalen-Versuch:** Die Bilder wurden beim Experiment mit dem Konzept "gleiche Ausprägung - anderes Bild" also zum Beispiel im2_br_1.15 - im4_br_1.15 bewertet. Dies führte dazu, dass man oft das zweite Bild sehr ähnlich oder gleich dem ersten bewertet hat.<br>**Lösung:** Bilder und Ausprägungen mehr durchmischen und mehr Bilder.

### Offene Fragen

**Gibt es pro Sonnenuntergangsart optimale Ausprägung?** Eventuell wäre eine Untersuchung von zwei Skalen interessant, die dieselbe Anzahl an Werten hat, welche jedoch anders beschrieben sind. Also ähnlich zu unserem Versuch einmal mit Wörtern und einmal mit Zahlen oder mit verschiedenen Wörtern beschriftet.

### Beantwortung der Hypothesen und Fragestellungen
**Hypothesen:**
1. <u>Kontrast und Saturation sollten eine höhere wahrgenommene Ästhetik als Helligkeit bewirken:*</u><br>Unsere Daten können dies nicht beantworten. <br>Jedoch bewirken vergleichsweise **höhere** Werte von Kontrast und Saturation eine höhere wahrgenommene Ästhetik als Helligkeit.
2. <u>Die Ergebnisse nähern sich einer optimalen Abstufung (je Eigenschaft) an:</u><br>Teilweise ja.<br>Teils sind die Bewertungen zwar grob in gemäß einer Glockenfunktion angeordnet, jedoch gibt es auch Unregelmäßigkeiten unter den Bildern. Wenn Sonnenuntergangkategorien eingeführt werden würden, könnte sich dies noch weiter aufklären.
3. <u>Eine negative Saturation bewirkt eine niedriger wahrgenommene Ästhetik:</u><br>Ja.<br>Basierend auf den Daten des 1. Teils kann man klar erkennen, dass eine Saturation <1.0 niemals am meisten bevorzugt wurde.<br>An dieser Stelle müssen wir jedoch sagen, dass im 2. Teil das 2. Bild teilweise bessere Bewertungen für Werte <1.0 bekommt. Um aber eine klare Aussage diesbezüglich machen zu können benötigen wir eine ehreblich größere Menge an Daten.
4. <u>Man tendiert auf bekannten Bewertungsskalen strenger zu bewerten:</u><br>Wahrscheinlich falsch.<br>Unsere Daten aus dem 2. Teil zeigen, dass wir grob ähnlich auf verschiedenen Skalen bewertet haben, also nicht strenger als auf anderen Skalen.<br>Da wir jedoch für eine klare Aussage viel mehr Daten benötigen, ist dies nur eine schwache Aussage.<br>Interessant ist jedoch, dass bei einer kleinen Skala wird oft der beste oder der schlechteste Wert gewählt wird, also teils etwas radikaler bewertet als auf anderen Skalen. 


**Fragestellungen:**
1. <u>Welchen Effekt haben Helligkeit, Kontrast und Saturation jeweils auf die wahrgenommene Ästhetik eines Bildes von einem Sonnenuntergang?</u><br>Helligkeit, Kontrast und Saturation verbessern die Ästhetik eines Bildes eines Sonnenuntergangs, soweit die Werte dieser Eigenschaften erhöht werden. Bei der Helligkeit sind kleine-moderate Erhöhungen ästhetisch ansprechender. Bei Kontrast und Saturation sind moderate-hohe Erhöhungen ästhetisch ansprechender. Werden die Eigenschaften jedoch geschwächt, wird dies als ästhetisch nicht-ansprechender wahrgenommen.
2. <u>Welchen Effekt hat die Wahl der Skala auf die Bewertung der Ästhetik eines Bildes von einem Sonnenuntergang?</u><br>Auf der Basis unseres Versuchs kommen wir zu dem Ergebnis, dass die Wahl der Skala keinen Effekt auf die Bewertung hat, soweit die Skala genügend Auswahlmöglichkeiten hat. <br>Demnach sollte die Skala so gewählt werden, wie sie am besten zum Versuch passt oder ausgewertet werden kann. Desto komplexer die Skala ist, desto schwieriger und länger dauert es die Bewertung auszuführen, wie wir selbst bei der Durchführung bemerkt haben. Die Durchführung unseres Versuches ist jedoch noch optimierbar. So sollte man die Reihenfolge der Skalen ändern oder eventuell im laufenden Versuch mehrmals verändern, so das man nicht ohne denken ein Bild nach dem anderen bewertet und nicht immer mit der selben Skala beginnt.



```python

```
