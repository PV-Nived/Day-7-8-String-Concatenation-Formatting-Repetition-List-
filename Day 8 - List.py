Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
Team=['csk','mumbai indians','rcb','srh','dc']

#Append
Team.append('kkr')
Team
['csk', 'mumbai indians', 'rcb', 'srh', 'dc', 'kkr']

#count
Team.count('csk')
1
Team.count('rcb')
1

#Insert
Team.insert(3,'punjab kings')
Team
['csk', 'mumbai indians', 'rcb', 'punjab kings', 'srh', 'dc', 'kkr']

#Indexing
Team.index('rcb')
2
Team.index('kkr')
6

#slicing
Team[1:4]
['mumbai indians', 'rcb', 'punjab kings']
Team[4:6]
['srh', 'dc']

#ranging
Team[::-2]
['kkr', 'srh', 'rcb', 'csk']
Team[::-1]
['kkr', 'dc', 'srh', 'punjab kings', 'rcb', 'mumbai indians', 'csk']

#pop
Team.pop()
'kkr'
Team.pop(2)
'rcb'
Team
['csk', 'mumbai indians', 'punjab kings', 'srh', 'dc']

#Remove
Team.remove()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Team.remove()
TypeError: list.remove() takes exactly one argument (0 given)
Team.remove('csk')
Team
['mumbai indians', 'punjab kings', 'srh', 'dc']

#Reverse
Team.reverse()
Team
['dc', 'srh', 'punjab kings', 'mumbai indians']

#Extend
name= ['Dhoni','raina','sachin','dravid']
Team.extend(name)
Team
['dc', 'srh', 'punjab kings', 'mumbai indians', 'Dhoni', 'raina', 'sachin', 'dravid']

#sort
Team.sort()
Team
['Dhoni', 'dc', 'dravid', 'mumbai indians', 'punjab kings', 'raina', 'sachin', 'srh']

#copy
name=Team.copy()
name
['Dhoni', 'dc', 'dravid', 'mumbai indians', 'punjab kings', 'raina', 'sachin', 'srh']
>>> Team
['Dhoni', 'dc', 'dravid', 'mumbai indians', 'punjab kings', 'raina', 'sachin', 'srh']
>>> 
>>> #Clear
>>> Team.clear()
>>> Team
[]
>>> name.clear()
>>> name
[]
>>> 
>>> #Deep copy
>>> Bike=['RE','Tvs','Passion','Honda','Ather']
>>> Car=['Bmw','Benz','Mustag','ferrai','RR','Ford']
>>> Bike=Car
>>> Car.pop()
'Ford'
>>> Bike
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR']
>>> Car
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR']
>>> 
>>> #Shallow copy
>>> Bike=['RE','Tvs','Passion','Honda','Ather']
>>> Car=['Bmw','Benz','Mustag','ferrai','RR','Ford']
>>> Bike=Car.copy()
>>> Bike
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR', 'Ford']
>>> Car
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR', 'Ford']
Car.pop()
'Ford'
Bike
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR', 'Ford']
Car
['Bmw', 'Benz', 'Mustag', 'ferrai', 'RR']
