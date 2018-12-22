#Questions for Problems at https://www.w3resource.com/python-exercises/python-basic-exercises.php
#To check the solution please type pythonpractice.problem**YourProblemNumer**() in the Main() function and run the program

class pythonpractice:
	def __init__(self,input1,input2):
		self.input1 = input1
		self.input2 = input2

	def problem1():
		print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')

	def problem2():
		import platform
		import sys
		print(sys.version)
		print(sys.version_info)
		print(platform.python_version())

	def problem3():
		import datetime
		x = datetime.datetime.now()
		print(x.strftime("%Y-%m-%d %H:%M:%S")) 

	def problem4():
		from math import pi
		r = float(input("Enter the radius : "))
		print((pi)*(r**2))

	def problem5():
		lst = input("Enter your Name :").split(' ')
		print('Hello '+lst[1]+' '+lst[0])

	def problem6():
		lst = input("Enter the numbers : ").split(',')
		tup = tuple(lst)
		print('List : ',lst)
		print('Tuple : ',tup)

	def problem7():
		name = input("Enter the String : ")
		print(name[-(len(name) - name.rfind('.') -1):])

	def problem7_2():
		name = input("Enter the String:")
		name = name.split('.')
		print(name[-1])

	def problem8():
		color_list = ["Red","Green","White" ,"Black"]
		print(color_list[0]," ",color_list[-1])
		
	def problem9():
		exam_st_date = (11, 12, 2014)
		print(exam_st_date[0],"/",exam_st_date[1],"/",exam_st_date[2])

	def problem10():
		n = input("Enter your number : ")
		print('Result is : '+ str(int(n) + int(n + n) + int(n+n+n)))

	def problem11():
		#Need Proper Solution
		fname = input("Enter the name of your function : ")
		print(fname.__doc__)

	def problem12():
		import calendar
		year = int(input('Enter the Year : '))
		month = int(input('Enter the Month : '))       
		print(calendar.month(year,month))

	def problem13():
		print('a string that you "don\'t" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example')	

	def problem14():
		from datetime import date
		date1 = date(2014,7,12)
		date2 = date(2014,7,5)
		print((date2 - date1).days)

	def problem15():
		from math import pi
		radius = int(input('Enter the radius of the sphere : '))
		print(f'The volume of sphere of radius {radius} is : ',(4/3)*pi*(radius**3))
		print('The volume of sphere of radius {} is : '.format(radius),(4/3)*pi*(radius**3))
		print('The volume of sphere of radius %d is : '%radius,(4/3)*pi*(radius**3))

	def problem16():

def main():
	pythonpractice.problem15()



if __name__ == "__main__":
	main()

