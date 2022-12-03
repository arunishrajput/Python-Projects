# Decimal to Binary Converter

decimal = int(input('Enter value in decimal : '))

def DTB(decimal):
	
	if decimal >= 1:
		DTB(decimal // 2) # new value of decimal after dividing by 2
	print(decimal % 2, end = '') # print all the remainder one by one because it is in a loop
	
DTB(decimal)