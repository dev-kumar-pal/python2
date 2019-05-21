f = open('Sample','r')
'''print(f)
#print(f.read())
print(f.readable())
#print(f.readline())
print(f.readline(),end="")
print(f.readline())'''

f1 = open('Demo','w')
#f.write("Hello")

#for data in f:
 #   f1.write(data)
file = open('Sample','r')
data = file.readlines()
for line in data:
        word = line.split()
        print (word)

