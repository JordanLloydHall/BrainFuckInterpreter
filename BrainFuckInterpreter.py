import time
import sys

def error(e):
	print("Error raised", e)
	quit()

def parse(text):
	pointer = 0
	states = [0]
	i = 0
	returns = []

	while i < len(text):
		char = text[i]
		#print(i)
		#print(states)

		if char == "<":
			if pointer == 0:
				error("Less than current state")
			else:
				pointer -= 1
		elif char == ">":
			pointer += 1
			if pointer > len(states)-1:
				states.append(0)
		elif char == "+":
			if states[pointer] == 255:
				states[pointer] = 0
			else:
				states[pointer] += 1
		elif char == "-":
			if states[pointer] == 0:
				states[pointer] = 255
			else:
				states[pointer] -= 1
		elif char == ".":
			print(chr(states[pointer]), end="")
		elif char == ",":
			states[pointer] = ord(input("> "))
		elif char == "[":
			returns.append(i)
		elif char == "]":
			if states[pointer] != 0:
				i = returns[-1]
			else:
				returns.pop()

		i += 1
	print()


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please parse 1 file name argument when running this program.")
		quit()
	text = open(sys.argv[1],"r").read()
	parse(text)