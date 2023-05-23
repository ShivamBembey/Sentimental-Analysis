import nltk
nltk.download()
from nltk.corpus import stopwords
a=(stopwords.words('english'))

'''

import matplotlib.pyplot as plt
x= [20, 40, 10, 50, 100]
y= ['A', 'B', 'C', 'D', 'E']
LABELS=["happycount","sadcount","surprisecount","angrycount"]
plt.bar(x,y,label="sentiments",color='b')
plt.xticks(x,LABELS)
plt.xlabel("sentiments")
plt.ylabel("frequency")
plt.title("Sentiment analysis")
plt.legend()
plt.show()
'''
'''
from textblob import TextBlob
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
print(polarity("i don't know"))
'''
