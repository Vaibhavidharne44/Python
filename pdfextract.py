import PyPDF2
import string
import json
import re
    
Reader = PyPDF2.PdfFileReader("Head First Python.pdf") 
    
print(Reader.numPages) 
     
print(Reader.getPage(2).extractText()) 
    

strr=""
for i in range (1,624):
    strr+=Reader.getPage(i).extractText()

print(strr)

with open("pdffile.txt","w",encoding="utf-8") as f:
          f.write(strr)
          
     
#remove punctuations
for i in string.punctuation:
    strr=strr.replace(i,"")
print(strr)

with open("pdffile.txt","w",encoding = 'utf-8') as f:
    f.write(strr)

listdata = strr.split()
print(listdata)
    
data = json.dumps(listdata)
print(data)

with open('json_data.txt', 'w') as outfile:
    outfile.write(data)


filename = 'json_data.txt'
  

dict1 = {}
  
with open(filename,'r',encoding = 'utf-8') as fh:
    for line in fh:
        # reads each line and removes  extra the spaces 
        # and gives only the valid words
        command, description = line.strip().split(None,1)
        dict1[command] = description.strip()
  
# creating json file
out_file = open("data_json.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()




