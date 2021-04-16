

import sys
import random

def main():
	size = sys.argv[1]
	size = int(size)
	password = ""
	for x in range(size):
		num = random.randint(0,10)
		character = str(num)



if __name__ == '__main__':
	main()
