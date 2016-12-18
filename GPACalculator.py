import numpy as np

grade_converter = { "A" : 4.0 , "B" : 3.0 , "C" : 2.0 , "D" : 1.0 , "F" : 0.0, 
"a" : 4.0 , "b" : 3.0 , "c" : 2.0 , "d" : 1.0 , "f" : 0.0}

letterGrades = raw_input("Enter your letter grades SEPARATED BY A COMMA: ")
numberGrades = []
badInput = []

counter = 0
for item in letterGrades:
	str(letterGrades).replace(' ','') #trying to remove spaces if they are inputted NOT WORKING!!
	if item in grade_converter:
		numberGrades.append(grade_converter[item])
	elif item != ',':
		counter = counter + 1
		print "At least one of your inputs is not a valid letter grade.\nGet rid of any spaces and make sure you enter A,B,C,D or F only."
		break

if counter == 0:
	GPA = np.mean(numberGrades)

if len(numberGrades) > 0 and counter == 0 and GPA >= 3:
	print "A %.2f!?!?! Great job!!" % GPA
elif len(numberGrades) > 0 and counter == 0 and GPA < 3:
	print "A %.2f!?!?! You should hit the books!" % GPA


