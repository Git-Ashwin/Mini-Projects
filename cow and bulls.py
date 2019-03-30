import random
print('                              lets play')
print()
print('Note: you have to guess a correct number in 5 chance')
print()
print('bulls = No of matching digits in their right positions')
print('cows  = No matching digits in different positions')
print()
n=int(input('select your difficulty ie.number of digits.........'))
print()
a=[]  
for i in range(n):
    m=random.choice([str(i) for i in range(1,10)])
    a.append(m)

for i in range(5):
      a2=a[:]
      v2=0
      l2=0
      v=0
      cow=0
      bull=0
      b=[]
      b2=input('guess the correct number.....')
      print()
      for i in b2:
          b.append(i)
      print()
      if len(b)!=n:
          print('ERROR : restart the game')
          break
      else:
         for i in a:
              l=0
              v=v+1
              for j in b:
                  l=l+1
                  if j==i:
                      if l==v:
                          bull=bull+1
         for i in b:
             if i in a2:
                 cow=cow+1
                 a2.remove(i)
      print('bulls=',bull,'   ','cows=',cow-bull)
      print()
      if bull==n:
          print('congrats you found the number!')
          break
      elif cow==n:
          print('you almost reach')
          print()
else:
    print('game over')
    print('the number is',''.join(a))
                      
