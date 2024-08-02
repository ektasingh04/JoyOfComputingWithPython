import string
dict={}
data=""
file=open("C:\\Users\\dell\\projects\\helloworld\\PYTHON\\WEEK6\\op.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)

with open("C:\\Users\\dell\\projects\\helloworld\\PYTHON\\WEEK6\\sbc.txt") as f:
    while True:
        #read file char by char and substitute a particular char acc to dic
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c] #if c present in dic then update data
        else:
            data=c # if c not prsent then it is written as it is in data i.e if anything other than upper lower case
        file.write(data)
        print(data)
file.close()

#use string called asciiletters  to substitue letters by 1 place.. initialise a dic.. 
# substitue ith of letters to i-1 of letters
# dic[ith letter]=i-1th ketter this maps a to Z b to a and so on.. keys are letters in original
#  while values are the new substitued letters
#read chr by chr if eof then break else check if prsent in file then replce else move ahead ..
#  now print string data in new file