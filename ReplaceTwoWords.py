# a = 2.3
# a = a.round()
# print(a)


name = ["himanshu suryavanshi","rahul mishra", "sidharth kumar","kiren kumar mishra"]

index_remove = []

for i in range(0,len(name)-1):
    a = i+1
#for i in name:   # finding nouns chunks 
    word = str(name[i]+" "+name[a])
    if word == "himanshu suryavanshi rahul mishra":
        
        name[a] = "himanshu suryavanshi_rahul mishra"
        index_remove.append(i)

    
        # print(name.replace(name[a], "himanshu suryavanshi_rahul mishra"))
print(name)
for i in index_remove:
    name.pop(i)
print(name)



    #Sprint(string.replace("e", "a"))
    # res = len(re.findall(r'\w+', test_string))
    # if len(chunk)== 2:
    #     print(chunk)

    # chunk = chunk.replace(" ", "_")
    # chunks.append(chunk)