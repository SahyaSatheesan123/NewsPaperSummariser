import MalayalamStemmer as mal
def stem():
	f_in=open('output1.txt','r')
	words=f_in.read().split('\n')
	f_out=open('output2.txt','w')
	for item in words:
		stem=mal.findstem(item)
		f_out.write(stem+"\n")
	f_out.close()
	f_in2=open("output2.txt","r")
	inp=f_in2.read().split("\n\n")
	f_out2=open("output3.txt","w")
	s1=""
	c=0
	n=len(inp)
	#print "****",len(inp)
	for sent in inp:
		c+=1
		if(sent!=s1 and c<(n-2)):
			#print sent
			print c
			f_out2.write(sent+"\n\n")
		elif sent!=s1 and c==n-2:
			f_out2.write(sent)
		
	#print "++++++++",inp[54]
		


	
