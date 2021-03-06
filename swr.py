#!/usr/bin/env python

#import
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

#variables
buttonY = 0.05
buttonHight = 0.1

buttonList = [['1.81','1.88'], ['3.50','3.80'], ['7.00','7.10'], ['10.10','10.15'], ['14.00','14.35'], ['18.06','18.17'], ['21.00','21.45'], ['24.89','24.99'], ['28.00','29.70'], ['144','146']]

buttonPos = [0] * len(buttonList)
buttonObject = [0] * len(buttonList)
buttonWeight = 1 / len(buttonList)

#simulate data
x = np.arange(0.0, 30.0, 0.01)
y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))

#add figure
fig = plt.figure(figsize=(8,6))

#plot figure 0
ax = fig.add_subplot(211, axisbg='#FFFFCC')
plt.subplots_adjust(bottom=0.2)
ax.plot(x, y, '-')

#plot figure 1
ax2 = fig.add_subplot(212, axisbg='#FFFFCC')
plt.subplots_adjust(bottom=0.2)
ax2.plot(x, y, '-')

#add title
ax.set_title('Antenna analyzer by PB4M')

#button event
class Click_class:
    def __init__(self, minFreq, maxFreq):
        self.minFreq = minFreq
        self.maxFreq = maxFreq
    def Click(self, event):
        ax2.set_xlim(self.minFreq, self.maxFreq)
        plt.draw()


#draw buttons
for index, string in enumerate(buttonList):
    buttonX = ( buttonWeight * index ) 
    buttonPos[index] = plt.axes([buttonX, buttonY, buttonWeight, buttonHight])
    buttonObject[index] = Button(buttonPos[index], string[0] + "-" + string[1])
    buttonObject[index].on_clicked(Click_class(float(string[0]), float(string[1])).Click)

#show screen
plt.show()
