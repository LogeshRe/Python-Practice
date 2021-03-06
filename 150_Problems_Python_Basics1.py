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
		num = int(input('Enter the Number : '))
		if(num <= 17):
			print('The difference is ',17 - num)
		else:
			print('The Output is ',(num - 17)*2)

	def problem17():
		num = int(input('Enter the Number: '))
		if((abs(1000-num)<=100)or(abs(2000-num)<=100)):
			print(True)
		else:
			print(False)

	def problem18():
		a = int(input('Enter the Number 1 : '))
		b = int(input('Enter the Number 2 : '))
		c = int(input('Enter the Number 3 : '))
		if((a == b)and(b == c)):
			print(3*(a+b+c))
		else:
			print(a+b+c)

	def problem19():
		string = input('Enter the string : ')
		if(string[:2] == 'Is'):
			print(string)
		else:
			print('Is'+string)

	def problem20():
		string = input('Enter the String : ')
		num = int(input('Enter number of copies : '))
		print(string*num)

	def problem21():
		num = int(input('Enter the Number : '))
		if((num == 0) or (num % 2 == 0)):
			print('Even')
		else:
			print('Odd')

	def problem22():
		#Give Comma separated values
		num = input('Enter the values in list Comma Separated : ').split(',')
		print(num.count('4'))

	def problem23():
		string = input('Enter the string : ')
		n = int(input('Enter the Number of reputations : '))
		if(len(string)<2):
			print(string*n)
		else:
			print(string[:2]*n)
	
	def problem24():
		letter = input('Enter the Alphabet : ')
		vowels = ['a','e','i','o','u','A','E','I','O','U']
		if letter in vowels:
			print('It\'s a vowel')
		else:
			print('It\'s not a vowel')

	def problem25():
		list1 = [1,2,3,4]
		num = int(input('Enter the number: '))
		if num in list1:
			print(True)
		else:
			print(False)

	def problem26():
		list1 = [7,5,4,2,4]
		for num in list1:
			print('*'*num)

	def problem27():
		list1 = ["I","Love","being","fit"]
		string = " ".join(list1)
		print(string)

	def problem28():
		numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
				    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
				    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
				    958,743, 527]
		for num in numbers:
			if(num%2 == 0):
				print(num)
			if(num == 237):
				break

	def problem29():
		color_list_1 = set(["White", "Black", "Red"]) 
		color_list_2 = set(["Red", "Green"])
		color_set = color_list_1 - color_list_2
		print(color_set)

	def problem30():
		base = int(input('Enter the Base : '))
		height = int(input('Enter the Height: '))
		Area = (base * height)/2
		print(Area)

	def problem31():
		num1 = int(input('Enter the Number 1 : '))
		num2 = int(input('Enter the Number 2 : '))		
		def gcds(num1,num2):
			num = num2
			while True:
				if(num1 % num == 0 and num2 % num == 0):
					print(num," is the GCD")
					break
				while True:
					num = num-1
					if(num2 % num == 0):
						break
		if(num1 == num2):
			print(num1, " is the GCD")
			return
		else:
			if(num1 > num2):
				gcds(num1,num2)
			else:
				gcds(num2,num1)

	def problem32():
		def LCM(num1,num2):
			pass
			
	def problem33():
		num = (input('Enter the Number')).split(',')
		if((int(num[0]) == int(num[1])) or (int(num[1]) == int(num[2])) or (int(num[0]) == int(num[2]))):
			print(0)
		else:
			print(int(num[0])+int(num[1])+int(num[2]))

	def problem34():
		num1 = int(input('Enter the Number 1 : '))
		num2 = int(input('Enter the Number 2 : '))
		sum = num1 + num2
		if(sum > 15 and sum < 20):
			print(20)
		else:
			print(sum)

	def problem35():
		num1 = int(input('Enter the Number 1 : '))
		num2 = int(input('Enter the Number 2 : '))
		if(num1 == num2 or (abs(num1 - num2) == 5) or (num1 + num2) == 5):
			print(True)
		else:
			print(False)

	def problem36():
		def ifint(num,num1):
			if(isinstance(num,int) and isinstance(num1,int)):
				print(num+num1)
			else:
				print("Enter Integers")

		ifint(2,0)

	def problem37():
		name , age , address = 'Logesh', 24, 'Accenture, Pune, India'
		print('Name: {}\nAge: {}\nAddress: {}'.format(name,age,address))

	def problem38():
		num1 = 3
		num2 = 4
		result = (num1+num2)**2
		print("({} + {})^2)={}".format(num1,num2,result))

	def problem39():
		amt = 10000
		inst = 3.5
		years = 7
		fv = amt *((1 + (0.01*inst))**years)
		print(round(fv,2))

	def problem40():
		import math
		x1, y1 = 4,0
		x2, y2 = 6,6
		distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
		print(distance)

	def problem41():
		from os import path
		if(path.exists('C:\Logesh.mp3')):
			print('Present')
		else:
			print('Not Present')

	def problem42():
		import platform
		val = platform.architecture()
		print(val[0])

	def problem43():
		import os, platform
		print(os.name)
		print(platform.system())
		print(platform.release())

	def problem44():
		pass

	def problem45():
		import os
		print(os.system('echo Logesh'))

	def problem46():
		import os
		print(os.path.realpath(__file__))

	def problem47():
		pass

	def problem48():
		val = ('12','1.3','24.0','qb')
		try:
			for a in val:
				if '.' in a:
					print(float(a))
				else:
					print(int(a))

		except ValueError:
			print('The value {} is not a numnber'.format(a))


	def problem49():
		from os import listdir
		from os.path import isfile, join
		mypath = r'C:\Users\Logesh\Desktop'
		file = [f for f in listdir(mypath) if isfile(join(mypath,f))]
		for filename in file:
			print(filename)

	def problem50():
		for i in range(0,11):
			print(i, end='')

	def problem51():
		import cProfile
		print(cProfile.run('pythonpractice.problem48()'))

	def problem52():
		def eprint(*args,**kwargs):
			print(*args,**kwargs)

		eprint('a','b','c','d', sep ='--')

	def problem53():
		from os import environ
		print(environ)
		print(environ['PATH'])

	def problem54():
		import getpass
		print(getpass.getuser())

	def problem55():
		pass
		
	def problem56():
		pass
		
	def problem57():
		import time
		start_time = time.time()
		pythonpractice.problem49()
		end_time = time.time()
		total_time = end_time - start_time
		print(total_time)

	def problem58():
		try:
			num = int(input('Enter the Number: '))
			print(num*(num+1)/2)
		except ValueError:
			print('Please Enter Number Only')

	def problem59():
		Ht_Ft = int(input('Enter your Height in Feet: '))
		Ht_In = int(input('Enter your Height in Inches: '))
		Ht_In = (Ht_Ft*12)+Ht_In
		Ht_cm = round(Ht_In*2.54,1)
		print('The height is %d cm'%Ht_cm)

	def problem60():
		from math import sqrt
		print('Enter the sides of the triangle')
		a = float(input('a : '))
		b = float(input('b : '))
		c = sqrt(a**2 + b**2)
		print('Hypotenuse is %f'%c)

	def problem61():
		ft = int(input('Enter the number of fts'))
		yd = ft/3
		ml = ft/5280
		In = ft*12
		print('%d ft in Inches is %f Inches'%(ft,In))
		print('%d ft in Yards is %.2f Yards'%(ft,yd))
		print('%d ft in Miles is %.2f miles'%(ft,ml))

def main():
	pythonpractice.problem61()

if __name__ == "__main__":
	main()

