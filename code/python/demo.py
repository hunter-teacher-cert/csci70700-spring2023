print("Python Demo")

a=2
if a > 3:
    print("a is greater than 3")
    print("in fact it's",a)
elif a == 2:  #java has else if, in Python it's a special keyword
    print("it's 2")
else:
    pass # pass is a "null" statement - a placeholder if you don't have code yet
    
i = 0
while i < 10:
    print(i)
    i=i+1

for letter in "hello world":
    print(letter)

for item in ['a','b','c']:
    print(item)
print()
for value in range(5,15):
    print(value)

