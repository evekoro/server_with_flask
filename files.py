with open('myfile.txt', 'a', encoding='utf-8') as myfile:
	myfile.write("\tHi all!\n")

with open('myfile.txt', 'r', encoding='utf-8') as myfile:
	for ln in myfile:
		ln = ln.upper()
		ln = ln.replace("\n","")
		print(ln)