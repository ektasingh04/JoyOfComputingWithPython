 #dictionary -> key - unique identifier ... value- details abt any item
#creating a dic
convfac={} #curly braces for dic empty dic
print(convfac)

convfac['dollar']=60     #name sq brackets key and then value
convfac['euro']=80
convfac['yen']=56
print(convfac)

#access a  value
convfac['dollar']
#list of all keys
convfac.keys()
#if list format needed for keys and values
list(convfac.keys())
list(convfac.values())
#all items in dic
convfac.items()
### to know other functionalties ----->>> convfac,tab .. a list will be shown of all functions
# if want to study abt one of function use convfac.pop?
x=convfac.pop('yen',[convfac])
print(x)

convfac['dollar']=65
print(convfac)

# pop deletes key and returns its value while del delete the whole 
del convfac['dollar']
print(convfac)
#euro rs
euro=30
e=30
r=e*convfac['euro']
print(r)
print(convfac)
