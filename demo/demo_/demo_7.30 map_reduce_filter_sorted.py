from functools import reduce, cmp_to_key
from math import sqrt

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.items()]
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')

print("======================================================")
def add(x,y,f):
    return f(x)+f(y)
print(add(4,-8,abs))

def add(x,y,f):
    return f(x)+f(y)
print(add(4,9,sqrt))

print("======================================================")
def f(s):
  return s[0].upper() + s[1:].lower()
print (list(map(f, ['adam','LISA','barT'])))

print("======================================================")
def f(a,b):
  return a*b
print(reduce(f,[2,4,5,7,12]))

print("======================================================")
a='  123 '
b='aabbcc'
print(a.strip())
print(b.strip('a'))

def is_not_empty(s):
  return s and len(s.strip())>0
s=list(filter(is_not_empty,['test',None,'','strq','END ']))
print(s)

print("======================================================")
def is_int(x):
  return sqrt(x).is_integer()
s=list(filter(is_int,range(1,101)))
print(s)

print("======================================================")
def f_cmp(x):
  return x.upper()
print(sorted(['bob','about','Zoo','Credit'],key=f_cmp))

print("======================================================")
def f_cmp(x,y):
    if x[0].lower()<y[0].lower():
        return -1
    if x[0].lower()>y[0].lower():
        return 1
    return 0
#from functools import  cmp_to_key
print(sorted(['bob','about','Zoo','Credit'],key=cmp_to_key(f_cmp)))