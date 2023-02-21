import sys

for i in range(1,len(sys.argv[:])):
    filename =sys.argv[i]
    with open(f"{filename}", "r") as f:
        print(f.read(), end="")
        f.close()