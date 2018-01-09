def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def multiply(a,b):
	return a * b

def divide(a,b):
	return a / b

def square(a):
	return a ** 2

def cube(a):
	return a ** 3

def square_n_times(a,n):
	return a ** n

print "I'm going to use the calculator functions to multiply 5 and 6"
x = multiply(5,6)
print x


print "Square of 5 is:"
y = square(5)
print y

print "Cube of 5 is:"
z = cube(5)
print z

print "2^4 is:"
f = square_n_times(2,4)
print f
