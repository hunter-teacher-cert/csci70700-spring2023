import random


a = [1,2,3,4,5]
b = ['a','b','c','d','e']

squares=[]
for i in range(20):
    squares.append(i*i)

print(squares)
print(squares[0],squares[-1])
print(squares[5:10])
print(squares[:7])
print(squares[10:])

randolist=[]
for i in range(20):
    randolist.append(random.randrange(0,100))


board=[ [0,0,0], [0,0,0], [0,0,0]]
print(board)
print()
board[1][1]=1
board[0][1]=1
board[2][1]=1
print(board)

larger_board=[]

for row in range(3):
    larger_board.append([0,0,0,0])

print(larger_board)


lawrence = {'name':'Johnny',
        'dojo':'Cobra Kai',
        'catchphrase':'QUIET!!'}
print(lawrence['dojo'])
lawrence['dojo']='Eagle Fang!'
print(lawrence['dojo'])

dict={}

dict['one']=23
dict['two']="hello world"
dict[3] = 55.3
dict[0] = [1,2,3,4,5]
dict['jl']=lawrence

print(dict)

print(dict[0])
print(dict[0][3])
print(dict.keys())
print(dict.values())

for k in dict.keys():
    print(k,dict[k])


# also reading a file:
f = open("data.dat")
for line in f.readlines():
    line = line.strip()
    print(line)


line = "this is a sentence"
for word in line.split(): # split splits a string on whitespace (or other if you pass a parameter)
    print(word)
