from pyspark import SparkContext
import csv
import re
import sys
import itertools

def create_pairs(line):		
	line = line.split(" ");
	array = list(itertools.combinations(line,2))
	return array	

def preprocess(line):
	m = re.search('\\<(.*?)\\>', line)
	if m:
		loc = m.group(1)
	parts=line.split(">")
	if(len(parts)==2):
		line=line.split(">")[1]
		if("\t" in line):
			line=line.replace("\t","")
		else:
			line=line.replace("  "," ")
		
		line=line.replace("v","u")
		line=line.replace("j","i")
		line = re.sub('[^a-zA-Z0-9\\s]',"",line)
		return loc,line
	else:
		return "",""		
	

def get_combinations(pair,loc):
	A=[]
	B=[]
	a=pair[0]
	b=pair[1]
	if(lemmas.has_key(a)==True):
		A=lemmas.get(a)
	else:	
		A.append(a)
	if(lemmas.has_key(b)==True):
		B=lemmas.get(b)
	else:	
		B.append(b)

	out= list(itertools.product(A,B))
	output =[]
	
	for i in out:
		if i[0]!="" and i[1]!="":
			temp = i[0]+","+i[1]+"$"+loc
			output.append(temp)
			
	return output
	
	
			
def Mapper(line):
	temp=[]
	loc,line=preprocess(line)
	pairs=create_pairs(line)
	for i in range(0,len(pairs)):
		x= pairs[i][0]+","+pairs[i][1]+"$"+loc
		temp.append(x)
		combinations = get_combinations(pairs[i],loc)
		temp.extend(combinations)
	return temp
         
          	



print"2-gram"
logFile = "vergil.aeneid.tess"  # Should be some file on your system
sc = SparkContext("local", "2gram")
text_file = sc.textFile(logFile).cache()
text_file = text_file.map(lambda x: x.encode("ascii", "ignore"))
 
lemmas=dict()
with open('new_lemmatizer.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		key=row[0]
		value=[]
		for i in range(1,len(row)):
			value.append(row[i])
		lemmas[key]=value	


sentences=text_file.map(lambda line:line)
sentences = sentences.filter(lambda x: ">" in x)
mapoutput=sentences.flatMap(Mapper)
mapoutput=mapoutput.filter(lambda x:"$" in x)
mapoutput=mapoutput.filter(lambda x:len(x.split("$"))==2)
mapoutput=mapoutput.map(lambda x:(x.split("$")[0],x.split("$")[1]))
#mapoutput.saveAsTextFile(sys.argv[1])
reduceoutput=mapoutput.reduceByKey(lambda x,y : x + "," + y)
reduceoutput.saveAsTextFile(sys.argv[1])




