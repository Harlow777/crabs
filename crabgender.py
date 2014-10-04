import math
import random
import string
import csv
import random

# Jacob Harlow
# October 4, 2014
# CSC 475 Artifical Intelligence
#
# This program is a single perceptron built to learn what crabs are male 
# or female based on two attributes from the csv CW(carapace width) and 
# RW(rear width). 

# initialize weights randomly
weight1 = round(random.uniform(0.1, 10.0), 10)
weight2 = round(random.uniform(0.1, 10.0), 10)
weights = [1, weight1, weight2]	

#initialize alpha 
alpha = 0.01

Guessright = 0
Sex = []
Rw = []
Cw = []


# read from crabs csv
with open('crabs.csv') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			sex = row[2]
			Sex.append(sex)
			rw = row[5]
			Rw.append(rw)
			cw = row[6]
			Cw.append(cw)

# learning algorithm
def learn(sex, CW, RW):
	# call hypothesis 
	hypothesis = Hyp(CW, RW)
	# train it down if it correctly guesses male
	if (hypothesis and sex == 'M'):
		err = -2
	# train it up if it correctly guesses female
	elif (not hypothesis and sex == 'F'):
		err = 2
	# 0 if its wrong
	else:
		err = 0
	# adjust weights according to the error
	weights[1] = weights[1] + err * CW * alpha
	weights[2] = weights[2] + err * RW * alpha
	
	if(hypothesis):
		print "Guess = M"
	else:
		print "Guess = F"
	print "Actual sex = %s" % sex
	print "error = %s" % err
	
# hypothesis algorithm, multiply attributes by weights and sum with bias
def Hyp(CW, RW):
	h = CW*weights[1] + RW*weights[2] + weights[0]
	# return true if its positive
	return h>0

# testing algorithm, just calls hypothesis
def test(Sex, Cw, Rw):
	hypothesis = Hyp(Cw, Rw)
	if(hypothesis):
		print "Guess = F"
		Guess = 'F'
	else:
		print "Guess = M"
		Guess = 'M'
	print "Actual sex = %s" % Sex
	if(Sex == Guess):
		increment()

# increments the percentage variable
def increment():
    global Guessright
    Guessright = Guessright+1	

# training loop
for i in range(1000):
	# random crab selector
	randindex = random.randint(1, 199)
	# call learn then decrement alpha slightly
	learn(Sex[randindex], float(Cw[randindex]), float(Rw[randindex]))
	alpha = alpha/1.03
	print ""

# testing loop
for i in range(100):
	randindex2 = random.randint(1, 199)
	test(Sex[randindex2], float(Cw[randindex2]), float(Rw[randindex2]))
	print ""
	
# print percent right
print "Percent correct: %s" % Guessright

