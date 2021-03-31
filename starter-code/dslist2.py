#q1
import random
# this method will automatically fill out the values in a list
# total number of elements in a list also changes randomly.
def generate_data(ls):
	count = random.randint(5,10) 	
	for i in range(count):
		ls.append(random.randint(1,100)) 	
def reverse_data(ls):
	# add logic to reverse the list here.
	pass
def findMid(ls):
	result = 0
	# add your logic here to iterate through the list 
	# and compute the value in the list that is located in the mid point. 
	# divide the total number of elements by 2 to get the mid point. 
	# convert the mid point to an integer. 
	# for example, if there are 9 elements the mid point is 4 and there will be three elements on either side of the mid point.
	# note: if the total number of elements in the list is an odd number then the forward and reverse mid point will be same. 
	# note: if the total number of elements in the list is an even number then the forward and reverse mid point will be different. 
	return result
def evenNos(ls):
	result = 0
	# add your logic here to iterate through the list 
	# and compute the total number of even numbers in the list. 
	return result
def oddNos(ls):
	result = 0
	# add your logic here to iterate through the list 
	# and compute the total number of odd numbers in the list. 
	return result

ls = []
generate_data(ls)
print(f"input list: {ls}")
print(f"forward mid point: {findMid(ls)}")
reverse_data(ls)
print(f"reverse mid point: {findMid(ls)}")
print(f"count of odd nos: {oddNos(ls)}")
print(f"count of even nos: {evenNos(ls)}")
ls = []
