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
    print("Please type the phrase you want converted: ")
    phrase = input()
    print("Please enter how many numbers you want your phrase shifted: ")
    shift = int(input())
    caesar(phrase, shift)


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
        i += 1
    print(" ".join(caesarPhrase))

userInput()
