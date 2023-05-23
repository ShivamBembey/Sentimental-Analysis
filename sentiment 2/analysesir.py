import nltk
from tkinter import *
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from textblob import TextBlob
import matplotlib.pyplot as plt
from tkinter import messagebox

happyc=0
sadc=0
angryc=0
surprisec=0
def tokenisation(line):# it will extract characters only, from the sentence 
	#string1='Nam1ing me myselfed Password c password evening is am the has have gmail c gmailed mobile Abhi nav 123a,123b,abcd@gmail.com,abcd@gmail.com,1234567890 jatin khanna,123456,123456,xyz@gmail.com,xyz@gmail.com,7894561230'
	lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	string1=line.replace(',',' ')
	string=string1.split()
	listb=[]
	c=0
	for i in string:
		chk=False
		for j in i:
			length=len(i)
			if j in lista:
				listb.append(j)		
		listb.append(" ")
	listb="".join(str(i) for i in listb)
	#print(listb)
	return listb

def stopwordRemoval(line):# This will remove the, then etc from the sentence
	st_line=[]
	line1=line.split()
	a=stopwords.words('english')
	for i in line1:
		if i not in a:
			st_line.append(i)
	return " ".join(str(i) for i in st_line)

def stemming(line): #this will removes ing ,ed suffixes from the words
	lista=[]
	stemmer=LancasterStemmer()
	for word in line.split():
		word=stemmer.stem(word)
		lista.append(word)
	return " ".join(str(i) for i in lista)

def space_removal(line): #it will remove extra space form the sentence
	while "  " in line:
		line=line.replace("  "," ")
	return line

def main(line):
	line=tokenisation(line)
	line=stopwordRemoval(line)
	line=stemming(line)
	line=space_removal(line)
	return line

def check_emotion(f_line):  #count happy words sad words etc.
	global happyc
	global sadc
	global angryc
	global surprisec
	happyc=0
	sadc=0
	angryc=0
	surprisec=0
	h=open("Data\Happy.txt","r")
	happy=stemming(h.read()).split()
	s=open("Data\Sad.txt","r")
	sad=stemming(s.read()).split()
	a=open("Data\Angry.txt","r")
	angry=stemming(a.read()).split()
	sur=open("Data\Surprise.txt","r")
	surprise=stemming(sur.read()).split()
	for i in f_line.split():
		if i in happy:
			happyc=happyc+1
		if i in sad:
			sadc=sadc+1
		if i in angry:
			angryc=angryc+1
		if i in surprise:
			surprisec=surprisec+1
	emotionlist=[happyc,sadc,angryc,surprisec]
	return emotionlist

def plot():
	global happyc
	global sadc
	global angryc
	global surprisec
	if happyc==0 and sadc==0 and angryc==0 and surprisec==0:
		messagebox.showinfo(title="Plotting problem",message="Unable to plot the Graph.. Check Text Again.. ")
	else:
		y=[happyc ,sadc ,angryc ,surprisec ]
		x=[1, 2 , 3, 4]

		LABELS=["happy","sad","angry","surprise"]
		plt.bar(x,y,label="sentiments",color='b')
		plt.xticks(x,LABELS)# this will replace the 1 2 3 4 with names given
		plt.xlabel("sentiments")
		plt.ylabel("frequency")
		plt.title("Sentiment analysis")
		plt.legend()
		plt.show()
	return
def polarity(line):
	analyse=TextBlob(line)
	value=analyse.sentiment.polarity
	print(value)
	if value>0:
		return "positive"
	elif value==0:
		return "neutral"
	else:
		return "negative"
def maxpolarity():
	if happyc==0 and sadc==0 and angryc==0 and surprisec==0:
		return 0
	else:
		data=(happyc,sadc,angryc,surprisec) #this is tuple
		LABELS=["happy","sad","angry","surprise"]
		return LABELS[data.index(max(data))]

