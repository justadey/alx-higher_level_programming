<<<<<<< HEAD
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton Scholl 98 Battery street")
=======
#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[i]) - letter), end='')
    print()
>>>>>>> 6f67fa3ceec5840fac81923d9cb643e7b057411d
