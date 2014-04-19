# -*- coding: utf-8 -*-

#a=file.read().split('\n')
#am_karam = u'\u0d02'        
def splitletter(sentence):
	out=[]
	f_in=open('in.txt','r')
	inp=f_in.read().split('\n')
	asw=open("veruthe.txt",'w+')
	a=sentence.split('\n')
	fout=open("anu.txt",'w+')


	for b in a:
		c= b.decode('UTF-8')
	    	end_bound = len(c)
		start_bound = 0
		e=0
	    	s =""
		i=0
	    	while(i<end_bound): 
			flag=0
	       		s=c[i:i+1]
			fout.write(s.encode('UTF-8')+"\n")
			t=c[i+1:i+2]
			u=c[i+2:i+3]
			fout.write(t.encode('UTF-8')+"\n")
			#print t
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
		
			if (flag!=1 and s!="\n"):
				out.append(s)
				i=i+1
	#fout1.close()
	fout.close()

	#print out
	return out
	




