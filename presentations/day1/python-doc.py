#Exp1
# Easy to read and understand to anyone
print('Interest Calculator:')

amount = float(input('Principal amount ?'))
roi = float(input('Rate of Interest ?'))
yrs = int(input('Duration (no. of years) ?'))

total = (amount * pow(1 + (roi/100), yrs))
interest = total - amount
print('\nInterest = %0.2f' %interest)
#EExp1
#Exp2
>> File 1 
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n - 1) + fib(n - 2)
>> File 2 
import fibonacci
fibonacci.fib(30)
832040
#EExp2
#Exp3 
- None
types.NoneType: The null object None
- Numbers:
int: Integer
long: Arbitrary - precision integer
float: Floating point
complex: Complex number
bool: Boolean(True or False)
- Sequences:
Character string: str
Unicode character string: unicode
Abstract base type for all strings: basestring
list: List
tuple: Tuple
Returned by xrange(): xrange
- Mapping:
dict: Dictionary
Sets: set
Mutable set: frozenset
... AND MUCH-MUCH MORE!!1
#EExp3
#Exp4
python test.py
#EExp4