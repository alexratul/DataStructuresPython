def main():
    print("hello world!")

def isUnique(word):
    # print(word)
    seenLetters = set()
    for letter in word:
        if letter in seenLetters:
            return False
        seenLetters.add(letter)       
    
    return True

if __name__ == "__main__":
    result = isUnique("Kratos")
    print(result)
