def is_rotated(a,b):
    if  b in a:
        return False

    if a == "" and b == "":
        return True

    if a == "" or b == "":
        return False

    dictionary = set()

    for letter in a:
        dictionary.add(letter)
    
    for letter in b:
        if not letter in dictionary:
            return False

    return True

if __name__ == "__main__":
    # print(is_rotated("aabcccccaaa",""))
    # print(is_rotated("result",""))
    print(is_rotated("r","lol")) 
    print(is_rotated("erbottlewat","waterbottle"))
    print(is_rotated("terbottlewa","waterbottle"))  