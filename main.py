"""Copyright (c) 2017 * Keith Cestaro
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


def userInput():
    print("Please enter which cipher you would like to use: (CAESAR, ATBASH, \
MORSE)")
    cipherChoice = str(input()).upper()
    if cipherChoice == "CAESAR":
        print("Please type the phrase you want converted: ")
        phrase = input()
        print("Please enter how many numbers you want your phrase shifted (0-26): ")
        shift = int(input())
        if shift > 26 or shift < 0:
            print("Please input a valid shift")
        else:
            caesar(phrase, shift)
    elif cipherChoice == "ATBASH":
        print("Please type the phrase you want converted: ")
        phrase = input()
        atbash(phrase)
    elif cipherChoice == "MORSE":
        print("Please type the phrase you want converted: ")
        phrase = input()
        morse(phrase)


def morse(phrase):
    morsePhrase = []
    phrase.lower()
    i = 0
    while i < len(phrase):
        if phrase[i] == "a":
            morsePhrase.append(".-")
        elif phrase[i] == "b":
            morsePhrase.append("-...")
        elif phrase[i] == "c":
            morsePhrase.append("-.-.")
        elif phrase[i] == "d":
            morsePhrase.append("-..")
        elif phrase[i] == "e":
            morsePhrase.append(".")
        elif phrase[i] == "f":
            morsePhrase.append("..-.")
        elif phrase[i] == "g":
            morsePhrase.append("--.")
        elif phrase[i] == "h":
            morsePhrase.append("....")
        elif phrase[i] == "i":
            morsePhrase.append("..")
        elif phrase[i] == "j":
            morsePhrase.append(".---")
        elif phrase[i] == "k":
            morsePhrase.append("-.-")
        elif phrase[i] == "l":
            morsePhrase.append(".-..")
        elif phrase[i] == "m":
            morsePhrase.append("--")
        elif phrase[i] == "n":
            morsePhrase.append("-.")
        elif phrase[i] == "o":
            morsePhrase.append("---")
        elif phrase[i] == "p":
            morsePhrase.append(".--.")
        elif phrase[i] == "q":
            morsePhrase.append("--.-")
        elif phrase[i] == "r":
            morsePhrase.append(".-.")
        elif phrase[i] == "s":
            morsePhrase.append("...")
        elif phrase[i] == "t":
            morsePhrase.append("-")
        elif phrase[i] == "u":
            morsePhrase.append("..-")
        elif phrase[i] == "v":
            morsePhrase.append("...-")
        elif phrase[i] == "w":
            morsePhrase.append(".--")
        elif phrase[i] == "x":
            morsePhrase.append("-..-")
        elif phrase[i] == "y":
            morsePhrase.append("-.--")
        elif phrase[i] == "z":
            morsePhrase.append("--..")
        i += 1
    print(" ".join(morsePhrase))


def atbash(phrase):
    atbashPhrase = []
    phrase.lower()
    i = 0
    while i < len(phrase):
        if phrase[i] == "a":
            atbashPhrase.append("z")
        elif phrase[i] == "b":
            atbashPhrase.append("y")
        elif phrase[i] == "c":
            atbashPhrase.append("x")
        elif phrase[i] == "d":
            atbashPhrase.append("w")
        elif phrase[i] == "e":
            atbashPhrase.append("v")
        elif phrase[i] == "f":
            atbashPhrase.append("u")
        elif phrase[i] == "g":
            atbashPhrase.append("t")
        elif phrase[i] == "h":
            atbashPhrase.append("s")
        elif phrase[i] == "i":
            atbashPhrase.append("r")
        elif phrase[i] == "j":
            atbashPhrase.append("q")
        elif phrase[i] == "k":
            atbashPhrase.append("p")
        elif phrase[i] == "l":
            atbashPhrase.append("o")
        elif phrase[i] == "m":
            atbashPhrase.append("n")
        elif phrase[i] == "n":
            atbashPhrase.append("m")
        elif phrase[i] == "o":
            atbashPhrase.append("l")
        elif phrase[i] == "p":
            atbashPhrase.append("k")
        elif phrase[i] == "q":
            atbashPhrase.append("j")
        elif phrase[i] == "r":
            atbashPhrase.append("i")
        elif phrase[i] == "s":
            atbashPhrase.append("h")
        elif phrase[i] == "t":
            atbashPhrase.append("g")
        elif phrase[i] == "u":
            atbashPhrase.append("f")
        elif phrase[i] == "v":
            atbashPhrase.append("e")
        elif phrase[i] == "w":
            atbashPhrase.append("d")
        elif phrase[i] == "x":
            atbashPhrase.append("c")
        elif phrase[i] == "y":
            atbashPhrase.append("b")
        elif phrase[i] == "z":
            atbashPhrase.append("a")
        i += 1
    print("".join(atbashPhrase))


def caesar(phrase, shift):
    caesarPhrase = []
    phrase.lower()
    i = 0
    while i < len(phrase):
        if phrase[i] == "a":
            if 1 + shift > 26:
                caesarPhrase.append(str((1 + shift) - 26))
            else:
                caesarPhrase.append(str(1 + shift))
        elif phrase[i] == "b":
            if 2 + shift > 26:
                caesarPhrase.append(str((2 + shift) - 26))
            else:
                caesarPhrase.append(str(2 + shift))
        elif phrase[i] == "c":
            if 3 + shift > 26:
                caesarPhrase.append(str((3 + shift) - 26))
            else:
                caesarPhrase.append(str(3 + shift))
        elif phrase[i] == "d":
            if 4 + shift > 26:
                caesarPhrase.append(str((4 + shift) - 26))
            else:
                caesarPhrase.append(str(4 + shift))
        elif phrase[i] == "e":
            if 5 + shift > 26:
                caesarPhrase.append(str((5 + shift) - 26))
            else:
                caesarPhrase.append(str(5 + shift))
        elif phrase[i] == "f":
            if 6 + shift > 26:
                caesarPhrase.append(str((6 + shift) - 26))
            else:
                caesarPhrase.append(str(6 + shift))
        elif phrase[i] == "g":
            if 7 + shift > 26:
                caesarPhrase.append(str((7 + shift) - 26))
            else:
                caesarPhrase.append(str(7 + shift))
        elif phrase[i] == "h":
            if 8 + shift > 26:
                caesarPhrase.append(str((8 + shift) - 26))
            else:
                caesarPhrase.append(str(8 + shift))
        elif phrase[i] == "i":
            if 9 + shift > 26:
                caesarPhrase.append(str((9 + shift) - 26))
            else:
                caesarPhrase.append(str(9 + shift))
        elif phrase[i] == "j":
            if 10 + shift > 26:
                caesarPhrase.append(str((10 + shift) - 26))
            else:
                caesarPhrase.append(str(10 + shift))
        elif phrase[i] == "k":
            if 11 + shift > 26:
                caesarPhrase.append(str((11 + shift) - 26))
            else:
                caesarPhrase.append(str(11 + shift))
        elif phrase[i] == "l":
            if 12 + shift > 26:
                caesarPhrase.append(str((12 + shift) - 26))
            else:
                caesarPhrase.append(str(12 + shift))
        elif phrase[i] == "m":
            if 13 + shift > 26:
                caesarPhrase.append(str((13 + shift) - 26))
            else:
                caesarPhrase.append(str(13 + shift))
        elif phrase[i] == "n":
            if 14 + shift > 26:
                caesarPhrase.append(str((14 + shift) - 26))
            else:
                caesarPhrase.append(str(14 + shift))
        elif phrase[i] == "o":
            if 15 + shift > 26:
                caesarPhrase.append(str((15 + shift) - 26))
            else:
                caesarPhrase.append(str(15 + shift))
        elif phrase[i] == "p":
            if 16 + shift > 26:
                caesarPhrase.append(str((16 + shift) - 26))
            else:
                caesarPhrase.append(str(16 + shift))
        elif phrase[i] == "q":
            if 17 + shift > 26:
                caesarPhrase.append(str((17 + shift) - 26))
            else:
                caesarPhrase.append(str(17 + shift))
        elif phrase[i] == "r":
            if 18 + shift > 26:
                caesarPhrase.append(str((18 + shift) - 26))
            else:
                caesarPhrase.append(str(18 + shift))
        elif phrase[i] == "s":
            if 19 + shift > 26:
                caesarPhrase.append(str((19 + shift) - 26))
            else:
                caesarPhrase.append(str(19 + shift))
        elif phrase[i] == "t":
            if 20 + shift > 26:
                caesarPhrase.append(str((20 + shift) - 26))
            else:
                caesarPhrase.append(str(20 + shift))
        elif phrase[i] == "u":
            if 21 + shift > 26:
                caesarPhrase.append(str((21 + shift) - 26))
            else:
                caesarPhrase.append(str(21 + shift))
        elif phrase[i] == "v":
            if 22 + shift > 26:
                caesarPhrase.append(str((22 + shift) - 26))
            else:
                caesarPhrase.append(str(22 + shift))
        elif phrase[i] == "w":
            if 23 + shift > 26:
                caesarPhrase.append(str((23 + shift) - 26))
            else:
                caesarPhrase.append(str(23 + shift))
        elif phrase[i] == "x":
            if 24 + shift > 26:
                caesarPhrase.append(str((24 + shift) - 26))
            else:
                caesarPhrase.append(str(24 + shift))
        elif phrase[i] == "y":
            if 25 + shift > 26:
                caesarPhrase.append(str((25 + shift) - 26))
            else:
                caesarPhrase.append(str(25 + shift))
        elif phrase[i] == "z":
            if 26 + shift > 26:
                caesarPhrase.append(str((26 + shift) - 26))
            else:
                caesarPhrase.append(str(26 + shift))
        elif phrase[i] == " ":
            caesarPhrase.append(phrase[i])
        i += 1
    i = 0
    while i < len(caesarPhrase):
        if caesarPhrase[i] == "1":
            caesarPhrase[i] = "a"
        elif caesarPhrase[i] == "2":
            caesarPhrase[i] = "b"
        elif caesarPhrase[i] == "3":
            caesarPhrase[i] = "c"
        elif caesarPhrase[i] == "4":
            caesarPhrase[i] = "d"
        elif caesarPhrase[i] == "5":
            caesarPhrase[i] = "e"
        elif caesarPhrase[i] == "6":
            caesarPhrase[i] = "f"
        elif caesarPhrase[i] == "7":
            caesarPhrase[i] = "g"
        elif caesarPhrase[i] == "8":
            caesarPhrase[i] = "h"
        elif caesarPhrase[i] == "9":
            caesarPhrase[i] = "i"
        elif caesarPhrase[i] == "10":
            caesarPhrase[i] = "j"
        elif caesarPhrase[i] == "11":
            caesarPhrase[i] = "k"
        elif caesarPhrase[i] == "12":
            caesarPhrase[i] = "l"
        elif caesarPhrase[i] == "13":
            caesarPhrase[i] = "m"
        elif caesarPhrase[i] == "14":
            caesarPhrase[i] = "n"
        elif caesarPhrase[i] == "15":
            caesarPhrase[i] = "o"
        elif caesarPhrase[i] == "16":
            caesarPhrase[i] = "p"
        elif caesarPhrase[i] == "17":
            caesarPhrase[i] = "q"
        elif caesarPhrase[i] == "18":
            caesarPhrase[i] = "r"
        elif caesarPhrase[i] == "19":
            caesarPhrase[i] = "s"
        elif caesarPhrase[i] == "20":
            caesarPhrase[i] = "t"
        elif caesarPhrase[i] == "21":
            caesarPhrase[i] = "u"
        elif caesarPhrase[i] == "22":
            caesarPhrase[i] = "v"
        elif caesarPhrase[i] == "23":
            caesarPhrase[i] = "w"
        elif caesarPhrase[i] == "24":
            caesarPhrase[i] = "x"
        elif caesarPhrase[i] == "25":
            caesarPhrase[i] = "y"
        elif caesarPhrase[i] == "26":
            caesarPhrase[i] = "z"
        i += 1
    print("".join(caesarPhrase))

userInput()
