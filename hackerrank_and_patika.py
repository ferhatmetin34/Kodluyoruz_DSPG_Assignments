# Lists Bölümündeki HackerRank Çözümüm
#=========================================================================
N = int(input())
l=[]
for i in range(0,N):
    inp=input()
    if inp.startswith('insert'):
        l.insert(int(inp.split()[1]),int(inp.split()[2]))
    elif inp.startswith('print'):
        print(l)
    elif inp.startswith('remove'):
        l.remove(int(inp.split()[1]))
    elif inp.startswith('append'):
        l.append(int(inp.split()[1]))
    elif inp.startswith('sort'):
        l.sort()
    elif inp.startswith('pop'):
        l.pop()
    elif inp.startswith('reverse'):
        l.reverse()
#=========================================================================
# Print Function HackerRank Çözümüm

n = int(input())
print("".join([str(i) for i in range(1,n+1)]))

#=========================================================================
# Write a Function HackerRank Çözümüm

def is_leap(year):
    
    leap = False
    if year % 4 == 0 :
        leap=True
        if year % 100 == 0:
            leap=False
            if year % 400 ==0:
                leap=True

    
    return leap

#=========================================================================
# Input() Bölümündeki HackerRank Çözümüm

'''
inp=input().split()
x=int(inp[0])
k=int(inp[1])
sm=0


for t in [x**i for i in range(1,k+1)]:
    sm+=t
if sm==k:
    print(True)
else:
    print(False)
'''
# Burada bir testte hata almıştım galiba

inp=input().split()
x=int(inp[0])
k=int(inp[1])

p = input()
print(k==eval(p))

#=========================================================================
# String Split and Join HackerRank Çözümüm
def split_and_join(line):
    
    line=line.split(" ")
    line="-".join(line)
    return line

#=========================================================================
inp=input().split()
x=int(inp[0])
k=int(inp[1])
sm=0


for t in [x**i for i in range(1,k+1)]:
    sm+=t
if sm==k:
    print(True)
else:
    print(False)

#=========================================================================

x = int(input())
y = int(input())
z = int(input())
n = int(input())

for a in range(x+1):
    for b in range(y+10):
        for c in range(z+1):
            if a+b+c!=n:
                print(list([a,b,c]))
#=========================================================================
# Patika Proje Bölümündeki Sorular için Çözümüm

def reverse_list(lst):
    
    lst.reverse()
    
    for i in lst:
        i.reverse()
    
    return lst
    
print(reverse_list([[1, 2], [3, 4], [5, 6, 7]]))

#--------------------------------------------------------------------------

lst=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list=[]
def flatten_list(data):
    
    for element in data:
      
        if type(element) == list:
            
            flatten_list(element)
        else:
            flat_list.append(element)
    return flat_list
print(flatten_list(lst))

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------