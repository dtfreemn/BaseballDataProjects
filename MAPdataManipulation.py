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

MAPdata = open('Data/DPCHS_MAPData_2015-2016-Students.csv') #opens specific csv and turns it into an object

csv_MAPdata = csv.reader(MAPdata) #creates an object in which the opened csv is read into system



########################################
#									   #
#    DEFINE COLUMNS AS LISTS BEGINS    #
#									   #	
########################################

LanguageScores = []
MathScores = []
ReadingScores = []

########################################
#									   #
#       READ AND FILL DATA BEGINS      #
#									   #	
########################################

#Creates variable to be used to skip first row of data (because it's the header)
r = 0

#for loop to read over rows of data
for row in csv_MAPdata:
	# Remove nonsense data and prevent filling with header
	if r>1 and row[5] != 'NOT TAKEN' and row[8] != 'NOT TAKEN'and row[11] != 'NOT TAKEN':
		Lang = float(row[5])
		Math = float(row[8])
		Read = float(row[11])
		if Lang != 'NOT TAKEN' and float(Lang > 0) and Math != 'NOT TAKEN' and float(Math > 0) and Read != 'NOT TAKEN' and float(Read > 0):
			LanguageScores.append(Lang)
			MathScores.append(Math)
			ReadingScores.append(Read)
	r = r+1

###########################################
#             							  #
#           SCATTER PLOTS BEGIN           #
#										  #
###########################################

#################  Language Score vs Reading Score  ##################

#Creates Framework for Graph
LangScorevsReadScorefig = plt.figure()
LangScorevsReadScoreax = LangScorevsReadScorefig.add_subplot(111)

#Define independent variable
x = ReadingScores

#Define dependent variable
y = LanguageScores

#Creates Scatter Plot
LangScorevsReadScoreax.scatter(x,y,c='red') #Simpler code but no linear regression 

#Draws Trend Line
plt.plot(x,np.poly1d(np.polyfit(x,y,1))(x))

#R2
p = np.poly1d(np.polyfit(x,y,1))
ybar = np.sum(y)/len(y)
ssreg = np.sum((p(x)-ybar) ** 2)
sstot = np.sum((y-ybar) ** 2)
Rsqr = ssreg / sstot

#Plot R2
plt.text(0.8 * max(x) + 0.2 * min(x), 0.85 * np.max(y) + 0.2 * np.min(y), '$R^2 = %0.2f$' % Rsqr)

#Labels Axes
LangScorevsReadScoreax.set_xlabel('Reading Scores')
LangScorevsReadScoreax.set_ylabel('Language Scores')
LangScorevsReadScoreax.grid(True)
LangScorevsReadScoreax.set_title('Language Scores vs Reading Scores')

#Save File
scatfile = 'Plots/LangScorevsReadScoreScatter.png'
print "Saving scatter as:",scatfile
LangScorevsReadScorefig.savefig(scatfile)

##################  Reading Score vs Language Score  #######################

#Creates Framework for Graph
ReadScorevsLangScorefig = plt.figure()
ReadScorevsLangScoreax = ReadScorevsLangScorefig.add_subplot(111)

#Define independent variable
x = ReadingScores

#Define dependent variable
y = LanguageScores

#Creates Scatter Plot
ReadScorevsLangScoreax.scatter(x,y,c='red') #Simpler code but no linear regression 

#Draws Trend Line
plt.plot(x,np.poly1d(np.polyfit(x,y,1))(x))

#R2
p = np.poly1d(np.polyfit(x,y,1))
ybar = np.sum(y)/len(y)
ssreg = np.sum((p(x)-ybar) ** 2)
sstot = np.sum((y-ybar) ** 2)
Rsqr = ssreg / sstot

#Plot R2
plt.text(0.8 * max(x) + 0.2 * min(x), 0.85 * np.max(y) + 0.2 * np.min(y), '$R^2 = %0.2f$' % Rsqr)

#Labels Axes
ReadScorevsLangScoreax.set_xlabel('Language Scores')
ReadScorevsLangScoreax.set_ylabel('Reading Scores')
ReadScorevsLangScoreax.grid(True)
ReadScorevsLangScoreax.set_title('Reading Scores vs Language Scores')

#Save File
scatfile = 'Plots/ReadScorevsLangScoreScatter.png'
print "Saving scatter as:",scatfile
ReadScorevsLangScorefig.savefig(scatfile)
