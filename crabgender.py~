import math
import random
import string
import csv
import random

Sex = []
Rw = []
Cl = []

# read from crabs csv
with open('crabs.csv') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			sex = row[2]
			Sex.append(sex)
			rw = row[5]
			Rw.append(rw)
			cl = row[6]
			Cl.append(cl)


# sigmoid and its derivative
def sigmoid(x):
	return math.tanh(x)
  
def derivativesig(y):
	return 1 - y**2
    
# initialize weights randomly
weights = [2, 4, 6, 8]
randweight = random.randint(0, 3)
currweight = weights[randweight]

# vector?  
randdirection = random.randint(-10, 10)

# random crab
randindex = random.randint(1, 190)

SEX = Sex[randindex]
RW = float(Rw[randindex])
CL = float(Cl[randindex])
  
print "Crab Number = %s" % randindex
print "RW = %s" % RW
print "CL = %s" % CL

# guess the gender  
function = ((RW*randweight + CL*randweight) * randdirection)
Output = sigmoid(function)
  
if Output < 1:
  print "Actual sex = %s" % SEX
  print "Estimated Sex = F" 
else:
  print "Actual sex = %s" % SEX
  print "Estimated Sex = M"

	  

#initialize learning rate
#n=0.1	
	  
#forward
#  def forward:
#	  w(0) = 1;#assign random w(0)
#	  i=0
#	  for i in 1000
#		w(i+1) = w(i) - n upsidedowndeltae(w(0))
		
