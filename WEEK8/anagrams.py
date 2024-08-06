# sorting-- sorted(list),, if decreasing sort then sorted(l,reverse=True)
#sorted(dic)-- sorts on basis of keys.. 
'''
l=['cccc','bb','aaa','d']
#sort on basis of string length 
print(sorted(l,key=len))        '''

s1=input("enter frst string ")
s2=input("enter 2md string ")
if(sorted(s1)==sorted(s2)):
    print("yes these r anagrams")
else:
    print("not anagrams")