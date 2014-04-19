def para_fun(text):
	paras=text.split('\n\n')
	return paras
def tokens_sentence(raw_txt):
    tokenize=raw_txt.split(".")
    #tokenize=raw_txt.split("? ")
    #tokenize=raw_txt.split("! ")
    return tokenize
def tokens(sentence):
	tokenize=sentence.split(" ")
        return tokenize
def pgm1():
	f_in=open('newsfinal.txt','r')
	f_out=open("output0.txt",'w')
	f_out1=open("output1.txt",'w')
	context=f_in.read()
	para=para_fun(context)
	for p in para:
		sentence=tokens_sentence(p)
	###print sentence
		for item in sentence:
			k = tokens(item)
			for item1 in k:
				f_out1.write(item1+"\n")
			f_out.write(item+"\n")
	f_out.close()
	f_out1.close()

