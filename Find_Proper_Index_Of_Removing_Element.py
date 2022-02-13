# a= "himansu suryavanshi"
# a.split()
# print(len(a))
clause_token = [1,2,3,4,5,6,7,8,9,10]
remove_index = [2,4,5,7]
a = 0
for i in remove_index:
    print(i)
    print(a)
    
    num = i+a
    print(num)
    clause_token.pop(num)
    print(clause_token)
    a-=1

print(clause_token)