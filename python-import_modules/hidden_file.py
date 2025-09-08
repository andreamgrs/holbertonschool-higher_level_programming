#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    cont = 0
    for cont in range(0, len(names)):
        if names[cont][0] != "_" and names[cont][1] != "_":
            print(names[cont])