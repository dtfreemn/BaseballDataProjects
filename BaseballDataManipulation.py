########################################
#									   #
#        IMPORT MODULES BEGINS         #
#									   #	
########################################

import csv
import numpy as np #"as np" helps with easier calling later
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

########################################
#									   #
#      OPEN DATA SOURCE(S) BEGINS      #
#									   #	
########################################

pitchingdata = open('lahman-csv_2015-01-24/Pitching.csv') #opens specific csv and turns it into an object

csv_pitchingdata = csv.reader(pitchingdata) #creates an object in which the opened csv is read into system

salarydata = open('lahman-csv_2015-01-24/Salaries.csv')

csv_salarydata = csv.reader(salarydata)

########################################
#									   #
#    DEFINE COLUMNS AS LISTS BEGINS    #
#									   #	
########################################

pitcherera = [] 
pitcherwalksperout = [] 
pitcherwalks = [] 
pitcherearnedruns = [] 
pitcherIDs = []
pitcherseasons = []

########################################
#									   #
#       READ AND FILL DATA BEGINS      #
#									   #	
########################################

########  Pitching Data  ###########

#Creates variable to be used to skip first row of data (because it's the header)
r = 0

#for loop to read over rows of data
for row in csv_pitchingdata:
	# Remove nonsense data and prevent filling with header
	if r>0 and row[12] != '' and float(row[12]) >0:
		ERA = float(row[19])
		walks = float(row[16])
		outs = float(row[12])
		innings = outs/3
		WPO = walks/outs #walks per out
		earnedruns = float(row[14])
		pitcherID = row[0] #unique code assigned to each pitcher data line
		seasonyear = float(row[1])
		# Cut data
		if innings>150. and ERA != "" and WPO != "": #if number of innings pitched in a season is 150+
			pitcherera.append(ERA) #adds ERA to list
			pitcherwalksperout.append(WPO) #adds walks per out to list
			pitcherwalks.append(walks) #adds walks to list
			pitcherearnedruns.append(earnedruns) #adds earned runs to list
	r = r+1

#####
##### 
##### TO DO ###### Look up how to append only if element is present in another list 
#####
#####

###########################################
#             							  #
#           SCATTER PLOTS BEGIN           #
#										  #
###########################################

###############ERA vs WPO Scatterplot (with Trend Line) Begins

#Creates Framework for Graph
fig = plt.figure()
ax = fig.add_subplot(111)

#Define independent variable
x = pitcherwalksperout

#Define dependent variable
y = pitcherera

#Creates Scatter Plot
ax.scatter(x,y,c='red') #Simpler code but no linear regression 

#Draws Trend Line
plt.plot(x,np.poly1d(np.polyfit(x,y,1))(x))

#R2
p = np.poly1d(np.polyfit(x,y,1))
ybar = np.sum(y)/len(y)
ssreg = np.sum((p(x)-ybar) ** 2)
sstot = np.sum((y-ybar) ** 2)
Rsqr = ssreg / sstot

#Plot R2
plt.text(0.8 * max(x) + 0.2 * min(x), 0.8 * np.max(y) + 0.2 * np.min(y), '$R^2 = %0.2f$' % Rsqr)

#Labels Axes
ax.set_xlabel('Walks Per Out')
ax.set_ylabel('ERA')
ax.grid(True)
ax.set_title('ERA vs Walks Per Out')

#Save File
scatfile = 'Plots/ERAvsWPOScatter.png'
print "Saving scatter as:",scatfile
fig.savefig(scatfile)

###############Earned Runs vs Walks Scatterplot (with Trend Line) Begins

#Creates Framework for Graph
fig = plt.figure()
ax = fig.add_subplot(111)

#Define independent variable
x = pitcherwalks

#Define dependent variable
y = pitcherearnedruns

#Creates Scatter Plot
ax.scatter(x,y,c='red') #Simpler code but no linear regression 

#Draws Trend Line
plt.plot(x,np.poly1d(np.polyfit(x,y,1))(x))

#R2
p = np.poly1d(np.polyfit(x,y,1))
ybar = np.sum(y)/len(y)
ssreg = np.sum((p(x)-ybar) ** 2)
sstot = np.sum((y-ybar) ** 2)
Rsqr = ssreg / sstot

#Plot R2
plt.text(0.8 * max(x) + 0.2 * min(x), 0.8 * np.max(y) + 0.2 * np.min(y), '$R^2 = %0.2f$' % Rsqr)

#Labels Axes
ax.set_xlabel('Walks')
ax.set_ylabel('Earned Runs')
ax.grid(True)
ax.set_title('Earned Runs vs Walks')

#Save File
scatfile = 'Plots/ERvsWalksScatter.png'
print "Saving scatter as:",scatfile
fig.savefig(scatfile)

###########################################
#             							  #
#             HISTOGRAMS BEGIN            #
#										  #
###########################################

###############ERA Histogram Begins

#Creates Framework for Graph
fig = plt.figure()
ax = fig.add_subplot(111)

#Defines variable
x = pitcherera

#Creates Histogram
n, bins, patches = ax.hist(x,facecolor='blue',bins=200,range=(0,20),align='mid')

#Labels Axes
ax.set_xlabel('ERA')
ax.set_ylabel('Number of Pitchers')
ax.grid(True)
ax.set_title('Histogram of Pitcher ERA')

#Save File
histfile = 'Plots/ERAHistogram.png'
print "Saving histogram as:",histfile
fig.savefig(histfile)
#plt.show() #opens up visualization of histogram in new window

###############Walks Histogram Begins

#Creates Framework for Graph
fig = plt.figure()
ax = fig.add_subplot(111)

#Defines variable
x = pitcherwalks

#Creates Histogram
n, bins, patches = ax.hist(x,facecolor='blue',bins=100,range=(0,200),align='mid')

#Labels Axes
ax.set_xlabel('Walks')
ax.set_ylabel('Number of Pitchers')
ax.grid(True)
ax.set_title('Histogram of Pitcher Walks')

#Save File
histfile = 'Plots/WalksHistogram.png'
print "Saving histogram as:",histfile
fig.savefig(histfile)


#Closes CSV File When Done
pitchingdata.close()