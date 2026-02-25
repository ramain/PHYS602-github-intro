import sys
def add(a, b):
    return 1 + 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: 'python addition.py a b' ")
        exit
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    result = add(a,b)
    print(a, "+", b, "=", result)