Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string concatenation
#'+' operator

first_name='nived'
second_name='kumar'
full_name=first_name+' '+second_name
print(full_name)
nived kumar

#multiple string with '+'

Age=str(45)
place='avadi'
sentence=full_name+ 'of'+Age + 'lives in'+place
print(sentence)
nived kumarof45lives inavadi
sentence=full_name + 'of' + Age + 'lives in' + place
print(sentence)
nived kumarof45lives inavadi
sentence = full_name + 'of' + Age + 'lives in ' + place
print(sentence)
nived kumarof45lives in avadi

sentence = full_name + ' of ' + Age + ' lives in ' + place
print(sentence)
nived kumar of 45 lives in avadi

#Concatenation using join()

Live=[' john ','lives ',' at ',' london ']
live=" ".join(live)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    live=" ".join(live)
NameError: name 'live' is not defined. Did you mean: 'Live'?
Live=" ".join(Live)
print(Live)
 john  lives   at   london 

== RESTART: C:/Users/Nived/Downloads/Day 8(scrpt).py =
Traceback (most recent call last):
  File "C:/Users/Nived/Downloads/Day 8(scrpt).py", line 7, in <module>
    Context = ('My name is {0} , my age is {1} , and I work as a {2}'.format(Name,age,work))
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> 
== RESTART: C:/Users/Nived/Downloads/Day 8(scrpt).py =
My name is maddy , my age is 25 , and I work as a mechanic
>>> 
>>> 
>>> #string formatting
>>> #manual formatting
>>> 
>>> name = 'maddy'
>>> age = 25
>>> work = 'mechanic'
>>> Context = ('My name is {0} , my age is {1} , and I work as a {2}'.format(name,age,work))
>>> print(Context)
My name is maddy , my age is 25 , and I work as a mechanic
>>> 
>>> # Automated Formatting
>>> 
>>> Context = ('My name is %s, my age is %d, and I work as a %s.'%(name,age,work))
>>> print(Context)
My name is maddy, my age is 25, and I work as a mechanic.
>>> 
>>> #General Formatting
>>> 
>>> Context = ('My name is',name, 'my age is' ,age, 'and I work as a' ,work)
>>> print(Context)
('My name is', 'maddy', 'my age is', 25, 'and I work as a', 'mechanic')
>>> 
