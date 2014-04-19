# -*- coding: utf-8 -*-
import numpy
from numpy import *
import am as am1
import leven as le
def LD_split(b):
	#print "...........",b,len(b)
	out=[]
	f_in=open('in.txt','r')
	inp=f_in.read().split('\n')
	c= b.decode('UTF-8')
	end_bound = len(c)
	start_bound = 0
	e=0	    	
	s =""
	i=0
	cont=0
	while(i<=end_bound): 
		flag=0
		s=c[i:i+1]
		t=c[i+1:i+2]
		u=c[i+2:i+3]
		#print ">",s,"+++",t
		#print "..........",t
		chandra=inp[0].decode('UTF-8')
		if (s==u and t==chandra):
				s=s+t+u
				#print "///",s
				i=i+2
				t=c[i+1:i+2]
		for q in inp :
			comp=q.decode('UTF-8')
			if (t==comp and t!=''):
				#print "???",t
				cont+=1
				flag=1
				lettr=s+t
				i=i+1
				t=c[i+1:i+2]
				for r in inp:
					comp2=r.decode('UTF-8')
					if(t==comp2):
						lettr=lettr+t
				#print lettr
				out.append(lettr)
				i=i+2
				break	
		
		if flag!=1:
			out.append(s)
			i=i+1
	#print "****",len(out),cont
	#print "lllllllllll",out	
	return out


def comp(s1,s2):
	
	first=s1.split('\n')
	#print "here......",s1
	second=s2.split('\n')
	same=0
	flag=0
	string1=""
	for word in first:
		for word2 in second:
			if word == word2:
				same+= 1
				flag=1
		if (flag!=1):
			string1+=word
		flag=0
	return string1



def summary():

	perc=int(raw_input('\nEnter the percentage of summary to be generated:'))


	file = open('output3.txt', 'r')
	text = file.read()
	file.close()
	f_out=open("sent.txt","w")
	sent_list={}
	sent_list=text.split("\n\n")
	no_of_sentences=len(sent_list)


	#print sent_list[no_of_sentences-1]

	#n=len(sent_list)
	#print sent_list[n-1]
	for sent in sent_list:
		f_out.write(sent+"\n\n")

	#print sent_list[0]
	#print sent_list
	word_list = text.split()
	l=len(word_list)
	#print l
	word_freq = {}
	for word in word_list:
		word_freq[word] = word_freq.get(word, 0) + 1
		#print word

	#print n


	###### to find affinity weight.................####################
	affinity_weight={}
	for word in word_list:
		affinity_weight[word]= float(word_freq[word])/float(l)
		#print word,word_freq[word],affinity_weight[word]




	######## To find sentence weight.............############
	sent_weight={}
	w={}
	for sent in sent_list:
		w=sent.split("\n")
		nof_words=len(w)
		s=0.0
		str1=""
		for word in w:
			#print affinity_weight[word]
			if (word is str1):
				continue
			else:
				s=s+affinity_weight[word]	
		sent_weight[sent]=float(s)/float(nof_words)
		#print sent_weight[sent]
	






	#f_out2.close()

	f_out.close()




	###### To find levenshetein distance ######

	length={}
	for sent in sent_list:
		z=am1.splitletter(sent)
		length[sent]=len(z)
		#print len(z)

	lsw_matrix = numpy.zeros((no_of_sentences,no_of_sentences))
	i=0
	for s1 in sent_list:
		j=0
		for s2 in sent_list:
			strng=""
			source1=comp(s1,s2)
			dest1=comp(s2,s1)
			source2=LD_split(source1)
			dest2=LD_split(dest1)
			ld=le.levenshtein_distance(source2,dest2)
			#print ld
			#print "//////",length[s2]
			lsw_matrix[i,j]=float(max(length[s1],length[s2])-ld)/float(max(length[s1],length[s2]))
			j+=1
			#print "======",max(length[s1],length[s2])
		i+=1

	print lsw_matrix



	###### To find Vertex Weight ######
	q=0
	vertexwt={}
	i=0
	for sent in sent_list:
		j=0
		while(j<no_of_sentences):
			if(lsw_matrix[i,j]!=1):
				q+=lsw_matrix[i,j]
			j=j+1
		vertexwt[sent]=float(q)/float(no_of_sentences)
		i=i+1
		#print "\n",vwt
			


	#######  To find Sentence rank  #######
		
	rank={}	
	for sent in sent_list:
		rank[sent]=float(sent_weight[sent]+vertexwt[sent])/2.0
		p=sent_weight[sent]
		x=vertexwt[sent]
		#print p,x,rank[sent]




	##########......For printing the summary............... ####################
	f_in2=open("newsfinal.txt",'r')
	f_out1=open("insum.txt",'w+')
	f_out2=open("summary.txt",'w+')
	context=f_in2.read()
	item=context.split('.')
	s=[]
	s.append(0)
	out=sent_list[0]
	#print out
	f_out1.write(out+"\n\n")
	out2=item[0]
	#f_out2.write(out2+". ")
	var=0
	i=0
	j=0
	n=(perc*no_of_sentences)/100
	temp=0
	while(i<n-1):
			j=0	
			for sent in sent_list:
				if(rank[sent]>temp):
					if(s.count(j)==0):
						#print "ans",colsum[j]
						temp=rank[sent]	
						var=j
				j+=1
			#m=temp
			s.append(var)
			temp=0
			i+=1
			out=sent_list[var]
			out2=item[var]
			f_out1.write(out+"\n\n")
			#f_out2.write(out2+". ")
			#array.append(out)
			#print "\n",sent_list[var]
			#print "For summary....",item[var]
			#print  "answer",s.count(var)
	

	n=len(s)
	output = []

	while s:
	    smallest = min(s)
	    index = s.index(smallest)
	    output.append(s.pop(index))

	#print(output)
	i=0
	while (i<n):
		pos=int(output[i])
		#print item[pos]
		i=i+1
		out2=item[pos]
		f_out2.write(out2+". ")

	f_out2.close()
	f_out1.close()



















