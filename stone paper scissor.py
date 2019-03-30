import random

k='yes'
print('Note: You have to score more than computer in three round')
print()
while k=='yes':
 m=0
 c=0
 print('                           Lets play')
 print()
 for i in range(3):
        a=input('stone paper scissor     ')
        b=random.choice(['stone','paper','scissor'])
        if a!=b:
               if a=='stone' and b=='paper':
                   m=m+1
                   print('computer=',b)
                   print()
                   print('computer score = ',m)
                   print()
                   
               elif a=='paper' and b=='scissor':
                   m=m+1
                   print('computer=',b)
                   print()
                   print('computer score = ',m)
                   print()
                   
               elif a=='scissor' and b=='stone':
                   m=m+1
                   print('computer=',b)
                   print()
                   print('computer score = ',m)
                   print()
               elif b=='stone' and a=='paper':
                   c=c+1
                   print('computer=',b)
                   print()
                   print('your score = ',c)
                   print()
               elif b=='paper' and a=='scissor':
                    c=c+1
                    print('computer=',b)
                    print()
                    print('your score = ',c)
                    print()
               elif b=='scissor' and a=='stone':
                    c=c+1
                    print('computer=',b)
                    print()
                    print('your score = ',c)
                    print()
        else:
             print('computer=',a)
             print()
 else:
      if c<m:
         print('you lost')
         print()
      elif c==m:
         print('tie')
         print()
      else:
         print('you win')
         print()
 k=input('play again? (yes/no)   ')
 print()
