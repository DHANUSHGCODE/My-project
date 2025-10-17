"""Simple addition utility.

Provides an `add` function and a small CLI to add two numbers passed as
command-line arguments. If run without arguments it will prompt the user.
"""

import sys
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
	"""Return the sum of a and b.

	Accepts ints or floats. Will raise a TypeError if values cannot be added.
	"""
	return a + b


def _to_number(s: str) -> Union[int, float]:
	"""Convert string to int if possible, otherwise to float.

	Raises ValueError if conversion fails.
	"""
	try:
		return int(s)
	except ValueError:
		return float(s)


def main(argv=None) -> int:
	"""CLI entry point. Returns exit code 0 on success, 2 on user error."""
	if argv is None:
		argv = sys.argv[1:]

	if len(argv) >= 2:
		s1, s2 = argv[0], argv[1]
	else:
		# prompt the user when arguments are missing
		try:
			s1 = input("Enter first number: ")
			s2 = input("Enter second number: ")
		except EOFError:
			print("No input provided", file=sys.stderr)
			return 2

	try:
		n1 = _to_number(s1)
		n2 = _to_number(s2)
	except ValueError:
		print("Invalid number input", file=sys.stderr)
		return 2

	result = add(n1, n2)
	print(result)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
