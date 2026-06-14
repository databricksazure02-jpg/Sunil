"""Simple even/odd program.

Usage:
  - Run with numbers: `python sunil.py 2 3 -1`
  - Run without args to be prompted: `python sunil.py`
"""

def describe(n: int) -> str:
	return f"{n} is {'even' if n % 2 == 0 else 'odd'}"


def main(argv=None):
	import sys
	argv = argv if argv is not None else sys.argv
	if len(argv) > 1:
		for a in argv[1:]:
			try:
				n = int(a)
			except ValueError:
				print(f"{a!r} is not an integer")
				continue
			print(describe(n))
	else:
		try:
			n = int(input("Enter an integer: "))
		except Exception:
			print("Invalid input")
			return
		print(describe(n))


if __name__ == "__main__":
	main()

