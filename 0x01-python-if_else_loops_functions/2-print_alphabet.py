#!/usr/bin/python3
start = ord('a')
end = ord('z') + 1

for char_code in range(start, end):
    print(chr(char_code), end='')
