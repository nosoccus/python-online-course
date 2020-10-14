import math as m


a = 4.5
b = 5.9
c = 9
p = (a + b + c)/2
area = m.sqrt(p*(p-a)*(p-b)*(p-c))
print(round(area, 2))
