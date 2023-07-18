name="mohsin,aijaz"
#if i need only mohsin 
print(name[0:6]) #including 0 but not 6
#for aijaz
print(name[7:12])
print(name[:6]) #python puts 0 automatically
print(name[0:-3]) # name -3
print(name[0:len(name)-3]) #same as line 7
print(name[-4:len(name)-1]) # 8:11

#for finding lengths in string
print(len(name))

#quick quiz
nm="harry"
print(nm[-4:-2]) #ar will come (including 0 but not last one)