from sys import exit

i=1

while i<100:

	if i%3==0 and i%5==0:
                print 'FizzBuzz' 

	#prints 'FizzBuzz' for multiples of 3 and 5
	
	elif i%3==0:
		print 'Fizz' 
	
	#prints 'Fizz' for multiples of 3
	
	elif i%5==0:
		print 'Buzz' 

	#prints 'Buzz' for multiples of 5
	
	else:
		print i 
	
	#prints 'i', which will be the values that are not multiples of 3 and/or 5
	
	i=i+1

exit()
