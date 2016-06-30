import re
from nltk import tokenize

f = open('tainb.txt', 'r')

text = f.read()

f.close()

text_wo_lb = re.sub('(?!.)\n(?=.)', ' ', text)

f = open('tain_out.txt','w')

f.write(text_wo_lb)

f.close()

f = open('tain_out.txt', 'r')

text_arr = f.readlines()

f.close()


def subdivide(tw):

	if len(tw) < 140:
		return tw
	short_tw = tw[:140]
	
	if ';' in short_tw:
		ind = short_tw.rfind(';')
		
	if ',' in short_tw:
                ind = short_tw.rfind(',')

	result = [short_tw[:ind]]
	result.extend(subdivide(tw[ind+1:]))
	return [short_tw[:ind]] + [subdivide(tw[ind+1:])]
			


def sub_tweets(line):

	subs = tokenize.sent_tokenize(line)	 

	out_sub = []
	for poss_tw in subs:

		if len(poss_tw) < 140:
			out_sub.append(poss_tw)
			
		else:
			out_sub.extend(subdivide(poss_tw))


	return out_sub
			

tweet_arr = []
for line in text_arr:
	
	line = re.sub('\n', '', line)
	line = re.sub(' +', ' ', line)
	line = re.sub('^ ', '', line)
	
	if len(line) > 0 and len(line) < 140:
		tweet_arr.append(line) 
		continue
	
	#subs = sub_tweets(line)


		


