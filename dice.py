import random
print('                                lets play')
print()
print('The game will exit when the dice turns up 7')
print()
print('your betting amount will reduce when the dice turns up 2,3,4')
print()
print('Your betting amount will double when the dice turns up same number for two spins')
print()
money=0
won=[11]
def check(pair):
  global money
  if pair in [2,3,12]:
     money=money-bet
  elif pair in won:
     money=money+bet
  else:
     won.clear()
     won.append(pair)
  print('your balance is.................................',money,'$')
  print()
a='spin'
pair=0
for j in range(5):
           try:
              bet=int(input('enter your betting amount   $'))
              print()
           except:
               print()
               print('please give the proper value')
               print()
           else:
             break
while a=='spin':
         print()
         a1=random.choice([i for i in range(1,7)])
         a2=random.choice([i for i in range(1,7)])
         pair=a1+a2
         if pair==7:
              print('the dice pair is','[',a1,']','[',a2,']')
              break
         else:
              print('the dice pair is','[',a1,']','[',a2,']')
              print()
              check(pair)
              for i in range(5):
                  a=input('Enter spin to roll again......')
                  print()
                  if a=='spin':
                    break
                  else:
                    print('please enter a spin')
                    print()
print()
print('you won',money,'$')
print()
  
       
 
