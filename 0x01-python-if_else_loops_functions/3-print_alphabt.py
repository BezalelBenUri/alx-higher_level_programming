#!/usr/bin/python3
for asciis in range(97, 123):
    if chr(asciis) != 'q' and chr(asciis) != 'e':
        print("{}".format(chr(asciis)), end="")
