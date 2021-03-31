#q1
import random
def generate_data(ls):
	count = random.randint(5,10) 	
	for i in range(count):
		ls.append(random.randint(1,100)) 	
def evenNos(ls):
	result = 0
	# add your logic here to iterate through the list 
	# and compute the total number of even numbers in the list.
	# final output of this method should be returned using the variable result
	return result
def oddNos(ls):
	result = 0
	# add your logic here to iterate through the list 
	# and compute the total number of odd numbers in the list. 
	# final output of this method should be returned using the variable result
	return result

ls = []
generate_data(ls)
print(f"input list: {ls}")
print(f"count of odd nos: {oddNos(ls)}")
print(f"count of even nos: {evenNos(ls)}")
ls = []
