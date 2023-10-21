#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	i = 0
	for x in range(x):
		try:
			print("{}".format(my_list[x]), end='')
			i = i + 1
		except:
			break
	print("")
	return(i)

