import random


def createpass(number):
    alfanumeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
                   "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
    password_list = []
    password_word=""
    for i in range(number):
        password_list.append(random.choice(alfanumeric))
    for k in range(len(password_list)):
        password_word+=str(password_list[k])
    return password_word
