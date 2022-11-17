import parser as parser

while True:
	text = input("Clover > ")
	if text.strip() == "quit":
		break
	elif text.strip() == "":
		continue

	result, error = parser.parse("<stdin>", text)