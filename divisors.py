
import sys

def main():
	number = sys.argv[1]
	number = int(number)
	num = number
	while num != 0:
		answer = number % num
		if answer == 0:
			print(num)
		num = num - 1


if __name__ == '__main__':
	main()
	
