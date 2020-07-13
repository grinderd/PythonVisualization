#Alt+Shift+E to execute selection
#Purpose: Notes from chapter 9 of Python for Data analysis.  Also will work to make example code work


#9.1

#Simple line plot
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(10)
plt.plot(data)
plt.show() #Generates the plot in a window


#Plots exist in a figure object:

#Create a figure object:

fig = plt.figure()

#must add subplot to make a plot:

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

#plotting commands write to the last subplot and figure called

plt.plot(np.random.randn(50).cumsum(),'k--')
#Going to ax3
#If no figure is created prior to the plot command, the system will create one on the fly

#ax1, ax2, ax3 is an AxesSubplot objects
#Can directly plot on the other empty subplots

_ = ax1.hist(np.random.rand(100), bins = 20, color = 'k', alpha = 0.3)

ax2.scatter(np.arange(30), np.arange(30) + 3*np.random.randn(30))

#Comprehensive catalog of plot types in matplotlib.sourceforge.net

#Creating plots with subplots can be done quickly below:

fig, axes = plt.subplots(2,3)
axes

#Reference the subplot using the slicing: axes[0,1 would access the top middle plot

#Options alow some useful changes
'''
nrows = number of rows of subplots
ncols = number of cols of subplots
sharex = all subplots should use the same x-axis ticks; adjusting the xlim will affect all subplots
sharey = all subplots should use the same y-axis ticks; adjusting the ylim will affect all subplots
subplot_kw = dict of keywords passed to add_subplot call used to create each subplot
**fig_kw = Additional keywords to subplots are used when creating the figure, such as plt.subplots(2,2,figsize = 8,6))
'''

#subplots_adjust can change the whitespace around subplots: wspace, hspace adjusts whitesace around width and height


fig, axes = plt.subplots(2,2, sharex = True, sharey = True)

for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k',alpha =0.5)

plt.subplots_adjust(wspace = 0, hspace = 0)
#plt.subplots_adjust(wspace = 0.25, hspace = 0.25)
#plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
#plt.subplots_adjust(wspace = 0.75, hspace = 0.75)
#plt.subplots_adjust(wspace = 0.99, hspace = 0.99)

#Colors, Markers, and Line Styles

fig = plt.figure()

x = np.random.randn(500)
y = np.random.randn(500)

ax = fig.add_subplot(2,2,1)
ax.plot(x,y, 'g--')

#or

ax = fig.add_subplot(2,2,2)
ax.plot(x,y, linestyle = '--', color = 'g')

#Can use the hex code for color as well as the abbreviation

ax = fig.add_subplot(2,2,3)
ax.plot(x,y, linestyle = '--', color = '#CECECE')

#Marker

plt.plot(np.random.randn(30).cumsum(), 'ko-')
#or
plt.plot(np.random.randn(30).cumsum(), color = 'g', linestyle = 'solid', marker = 'o')

#Playing with line interpolation

data = np.random.randn(30).cumsum()

plt.plot(data,'k--',label = 'Default')
plt.plot(data,'k-',drawstyle = 'steps-post', label = 'steps-post')
plt.legend(loc = 'best')

#Ticks, Labels, and Legends

#Two ways to access matplotlib.pyplot
#1. Using the procedural pyplot interface

#2. More object-oriented native matplotlib API

#1 - pyplot interface: interactive use
'''
methods such as xlim, xticks, xticklabels
called without parameters returns the current levels e.g. plt.xlim()
with parameters sets the paramters e.g. plt.xlim([0,10])

Works with most recent created AxesSubplot

Corresponding methods on the object itself e.g. ax.get_xlim, ax.set_xlim
'''

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())

ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'],
                            rotation = 30, fontsize = 'small')

ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')

#axes class has set method to batch update plot properties

props = {
    'title': 'My first matplotlib plot',
    'xlabel': 'Stages'
}
ax.props(**props )

#Appears that you can pass a dictionary of kwargs with the '**' notation to work this.  Could be useful to set common
# parameters and apply them

#Ways to add legends:

#1: pass a label argument when additng each piece of the plot

#Figure 9-10
from numpy.random import randn
fig = plt.figure(); ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(),'k', label = 'one')
ax.plot(randn(1000).cumsum(),'g--', label = 'two')
ax.plot(randn(1000).cumsum(),'r.', label = 'three')

#Now call either plt.legend() or ax.legend

ax.legend()

# legend has the loc parameter to determine location of the legend in plot
# To leave a plot off the legend, pass no label or '_nolegend_' in the label

# Annotations and drawing on a subplot:

# Functions for annotations include text, arrow, or annotate functions

from datetime import datetime

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = pd.read_csv('examples/spx.csv', index_col - 0, parse_dates=True)
spx = data['SPX']

spx.plot(ax=ax, style='k-')


