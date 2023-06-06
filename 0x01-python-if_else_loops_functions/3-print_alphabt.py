#!/usr/bin/python3
for asciis in range(97, 123):
    if chr(asciis) is not 'q' and chr(asciis) is not 'e':
        print("{}".format(chr(asciis)), end="")
