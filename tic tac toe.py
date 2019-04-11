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
         if a[j][(len(a)-1)-j]==b:
             p=p+1  
             
    if 3 in (m,l,c,n,w,v,s,p):
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
def cpu_build(a,b):
    m=l=c=n=w=v=s=p=0
    for j in range(3):
         if a[j][j]==b:
             n=n+1

             if n==1 and 'x' not in [a[2][2],a[1][1],a[0][0]]:
                 return True,[(0,0),(1,1),(2,2)]
         if a[j][(len(a)-1)-j]==b:
             p=p+1  
             if p==1 and 'x' not in [a[0][2],a[1][1],a[2][0]] :
                 return True,[(0,2),(1,1),(2,0)]
    for j in range(3):
         if a[0][j]==b:
             c=c+1
             if c==1 and 'x' not in [a[0][0],a[0][1],a[0][2]]:
                 return 0,[0,1,2]
         if a[1][j]==b:
             v=v+1
             if v==1 and 'x' not in [a[1][0],a[1][1],a[1][2]]:
                 return 1,[0,1,2]
         if a[2][j]==b:
             w=w+1
             if w==1 and 'x' not in [a[2][0],a[2][1],a[2][2]]:
                 return 2,[0,1,2]
    for j in range(3):
         if a[j][0]==b:
             m=m+1
             if m==1 and 'x' not in [a[0][0],a[1][0],a[2][0]]:
                 return [0,1,2],0
         if a[j][1]==b:
             l=l+1
             if l==1 and 'x' not in [a[0][1],a[1][1],a[2][1]]:
                 return [0,1,2],1
         if a[j][2]==b and 'x' not in [a[0][2],a[1][2],a[2][2]]:
             s=s+1
             if s==1:
                 return [0,1,2],2


def cpu_win(a,b):
    m=l=c=n=w=v=s=p=0
    for j in range(3):
         if a[0][j]==b:
             c=c+1
             if c==2 and 'x' not in [a[0][0],a[0][1],a[0][2]]:
                 return 0,[0,1,2]
             
         if a[1][j]==b:
             v=v+1
             if v==2 and 'x' not in [a[1][0],a[1][1],a[1][2]]:
                 return 1,[0,1,2]
         if a[2][j]==b:
             w=w+1
             if w==2 and 'x' not in [a[2][0],a[2][1],a[2][2]]:
                 return 2,[0,1,2]
    for j in range(3):
         if a[j][0]==b:
             m=m+1
             if m==2 and 'x' not in [a[0][0],a[1][0],a[2][0]]:
                 return [0,1,2],0
         if a[j][1]==b:
             l=l+1
             if l==2 and 'x' not in [a[0][1],a[1][1],a[2][1]]:
                 return [0,1,2],1
         if a[j][2]==b and 'x' not in [a[0][2],a[1][2],a[2][2]]:
             s=s+1
             if s==2:
                 return [0,1,2],2
    for j in range(3):
         if a[j][j]==b:
             n=n+1
             if n==2 and 'x' not in [a[2][2],a[1][1],a[0][0]]:
                 return True,[(0,0),(1,1),(2,2)]
         if a[j][(len(a)-1)-j]==b:
             p=p+1  
             if p==2 and 'x' not in [a[0][2],a[1][1],a[2][0]] :
                 return True,[(0,2),(1,1),(2,0)]

def cpu_play(a,b):
    m=l=c=n=w=v=s=p=0
    for j in range(3):
         if a[0][j]==b:
             c=c+1
             if c==2 and 'o' not in [a[0][0],a[0][1],a[0][2]]:
                 return 0,[0,1,2]
             
         if a[1][j]==b:
             v=v+1
             if v==2 and 'o' not in [a[1][0],a[1][1],a[1][2]]:
                 return 1,[0,1,2]
         if a[2][j]==b:
             w=w+1
             if w==2 and 'o' not in [a[2][0],a[2][1],a[2][2]]:
                 return 2,[0,1,2]
    for j in range(3):
         if a[j][0]==b:
             m=m+1
             if m==2 and 'o' not in [a[0][0],a[1][0],a[2][0]]:
                 return [0,1,2],0
         if a[j][1]==b:
             l=l+1
             if l==2 and 'o' not in [a[0][1],a[1][1],a[2][1]]:
                 return [0,1,2],1
         if a[j][2]==b and 'o' not in [a[0][2],a[1][2],a[2][2]]:
             s=s+1
             if s==2:
                 return [0,1,2],2
    for j in range(3):
         if a[j][j]==b:
             n=n+1
             if n==2 and 'o' not in [a[2][2],a[1][1],a[0][0]]:
                 return True,[(0,0),(1,1),(2,2)]
         if a[j][(len(a)-1)-j]==b:
             p=p+1  
             if p==2 and 'o' not in [a[0][2],a[1][1],a[2][0]] :
                 return True,[(0,2),(1,1),(2,0)]


abc={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
a=[['_' for j in range(3)]for i in range(3)]
mm=[]
nn=[]
mode=input('enter mode(single/double)   ')
display()
number=0

'''if mode!='double':
    toss=input('heads/tails    ')
    print()
    if toss==random.choice(['head','tails']):
        print('player1 won the toss   ')
        number=0
    else:
        print('computer won the toss   ')
        number=1'''

play=1
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
          print('You cant go there')
          print()
          continue
      else:
       play+=1
     
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
           print('You cant go there')
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
   if len(nn)!=9:   
     print('computer')
     print()
   for i in range(100):
    if cpu_win(a,'o')!=None:
      v,j=cpu_win(a,'o')
      if str(j).isnumeric():
        vvv={0:v[0],1:v[1],2:v[2]}
        v=vvv[i]
      elif str(v).isnumeric():
          jjj={0:j[0],1:j[1],2:j[2]}
          j=jjj[i]
      else:
          jjv={0:j[0],1:j[1],2:j[2]}
          v,j=jjv[i]
    elif cpu_play(a,'x')!=None:
      v,j=cpu_play(a,'x')
      if str(j).isnumeric():
        vvv={0:v[0],2:v[1],1:v[2]}
        v=vvv[i]
      elif str(v).isnumeric():
          jjj={0:j[0],2:j[1],1:j[2]}
          j=jjj[i]
      else:
          jjv={0:j[0],2:j[1],1:j[2]}
          v,j=jjv[i]
    elif cpu_build(a,'o')!=None:
      v,j=cpu_build(a,'o')
      if str(j).isnumeric():
        vvv={0:v[0],2:v[1],1:v[2]}
        v=vvv[i]
      elif str(v).isnumeric():
          jjj={0:j[0],2:j[1],1:j[2]}
          j=jjj[i]
      else:
          jjv={0:j[0],2:j[1],1:j[2]}
          v,j=jjv[i]
    elif '_' in [a[0][0],a[0][2],a[2][0],a[2][2],a[1][1]]:
        vjj={0:(1,1),1:(0,2),2:(2,0),3:(2,2),4:(0,0)}
        v,j=vjj[i]

    else:
        v=random.choice([0,1,2])
        j=random.choice([0,1,2])
    mm.append(v)
    mm.append(j) 
    if mm in nn:
          mm.clear()
          continue
    else:
       play+=1
       nn.append(mm[:])
       mm.clear()
       a[v][j]='o'
       display()
       break
   if check(a,'o'):
         print('computer wins!')
         break
   if len(nn)==9:
      print('game over')
      break

