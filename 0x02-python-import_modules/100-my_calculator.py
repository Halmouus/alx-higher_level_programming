#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    args = len(argv)
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if not (argv[1] in "+-*/"):
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
    if argv[1] == "+":
        result = add(int(argv[0]), int(argv[2]))
    if argv[1] == "-":
        result = sub(int(argv[0]), int(argv[2]))
    if argv[1] == "*":
        result = mul(int(argv[0]), int(argv[2]))
    if argv[1] == "/":
        result = div(int(argv[0]), int(argv[2]))
    print("{} {} {} = {}".format(argv[0], argv[1], argv[2], str(result)))
