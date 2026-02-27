import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: 'python addition.py a b' ")
        exit
    a = sys.argv[1]
    b = sys.argv[2]
    result = add(a,b)
    print(a, "+", b, "=", result)
