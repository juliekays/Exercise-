"""Create a function Fizz_buzz to return 'fizz','buzz','fizzBuzz', or the argument it receives ,all depending on the argument of the function, a number the is divisible by 3,5 or both  3 and 5 respectively.
What the number is not divisible by 3 or 5 the number itself should be returned."""

def Fizz_buzz(num):
	if num%3==0:
		return 'fizz'
	elif num%5==0:
		return 'buzz'
	elif num%3==0 and num%5==0:
		return 'fizzbuzz'
	else: 
		return num

print Fizz_buzz(6)
print Fizz_buzz(10)
print Fizz_buzz(15)
print Fizz_buzz(14) 					