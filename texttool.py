#!/usr/bin/env python3

"""
Outil de traitement de texte.
Permet de calculer la longueur, les mots ou le préfixe.
"""


def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()

    if command == 'prefix':
        print(text[:10])

    if command == 'length':
        print(len(text))


    return "Unknown command " + cmd



def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
