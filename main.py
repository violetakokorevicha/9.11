n = int(input('Your grades:'))
k = 0
sum = 0
for i in range(n):
    m = int(input())
    k +=1
    sum += m
    formula = sum/k
if round(formula) in range(1,4):
  print('nesekmigs') 
if round(formula) in range(4, 9):
  print('viduveji')
if round(formula) in range(8, 11):
  print('teicamnieki')
print('Their arhimetic mean is =', formula)
  

