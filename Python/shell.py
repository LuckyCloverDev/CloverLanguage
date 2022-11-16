import clover as clover

# file_name = "text.txt"
# file = open(file_name, "r")
# text = file.read()

# result, error = clover.run(file_name, text)

# if error:
# 	print(error.as_string())
# elif result:
# 	print(result)

while True:
	text = input("Clover > ")
	if text.strip() == "quit":
		break
	elif text.strip() == "":
		continue
	result, error = clover.run("<stdin>", text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			#print(repr(result.elements[0]))
			pass
		else:
			#print(repr(result))
			pass