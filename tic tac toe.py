import random
print('                              lets play')
print()
def check(a,b):
    m=l=c=n=w=v=s=p=0
    for j in range(3):
         if a[0][j]==b:
             c=c+1
         if a[1][j]==b:
             v=v+1
         if a[2][j]==b:
             w=w+1
    for j in range(3):
         if a[j][0]==b:
             m=m+1
         if a[j][1]==b:
             l=l+1
         if a[j][2]==b:
             s=s+1
    for j in range(3):
         if a[j][j]==b:
             n=n+1
    if a[0][2]==a[1][1]==a[2][0]==b:  
          p=3
    if n==3 or s==3 or l==3 or m==3 or w==3 or v==3 or p==3 or c==3:
              return 1
    else:
              return 0

#display........

def display():
      for l in range(3):
              for m in range(3):
                 print(a[l][m],end=' ')
              print()
      print()

abc={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
a=[['_' for j in range(3)]for i in range(3)]
mm=[]
nn=[]
mode=input('enter mode(single/double)   ')
display()

while True:
 #player 1.............
  for k in range(10):
      xx=0
      get=int(input('enter a location(player1)   '))
      l=abc[get][0]
      m=abc[get][1]
      print()
      mm.append(l)
      mm.append(m) 
      if mm in nn:
          mm.clear()
          print('dont try to over write')
          print()
          continue
      else:
     
       nn.append(mm[:])
       mm.clear()
       a[l][m]='x'
       display()
       break
  if check(a,'x'):
          print('player1 wins!')
          break


  if mode=='double':
    for i in range(10):
        #player 2..........
        xx=0
        get=int(input('enter a location(player2)   '))
        v=abc[get][0]
        j=abc[get][1]
        print()
        mm.append(v)
        mm.append(j) 
        if mm in nn:
           mm.clear()
           print('dont try to over write')
           print()
           continue
        else:
      
           nn.append(mm[:])
           mm.clear()
           a[v][j]='o'
           
           display()
           break
    if check(a,'o'):
          print('player2 wins!')
          break
    if len(nn)==9:
      print('game over')
      break
    
         
  else:
   print('computer')
   print()
   for i in range(10):
      v=random.choice([0,1,2])
      j=random.choice([0,1,2])
      mm.append(v)
      mm.append(j) 
      if mm in nn:
          mm.clear()
          continue
      else:
      
       nn.append(mm[:])
       mm.clear()
       a[v][j]='o'
       display()
       break
   if check(a,'o'):
         print('compuer wins!')
         break
   if len(nn)==9:
      print('game over')
      break

