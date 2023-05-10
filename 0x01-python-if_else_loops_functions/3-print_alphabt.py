#!/usr/bin/python3
<<<<<<< HEAD
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print("{:s}".format(chr(i)), end="")
=======
for char in range(26):
    if char != 4 and char != 16:
        print("{:s}".format(chr(char + ord("a"))), end="")
>>>>>>> 6f67fa3ceec5840fac81923d9cb643e7b057411d
