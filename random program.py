import random

n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist1=["jadeja","dhoni","virat","shami","ashwin"]  #list
mylist2={"jadeja","dhoni","virat","shami","ashwin"}  #set
mylist3={"name":"abc" , "number":123}  #dict
print(random.choice(mylist1))

#print(random.choice(mylist1)) #will not work with set
print(random.choice(list(mylist2)))
#print(random.choice(mylist3)) #will not work with dict
print(random.choice(list(mylist3)))  #so change dict to list
random.shuffle(mylist1)

print(mylist1)