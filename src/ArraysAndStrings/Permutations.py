def main():
    print("hello world!")

def is_a_Permutation(word1,word2):
    seenLetters = set()
    #Add letter from word 1 on a set or hashset for further use
    for letter in word2:
        seenLetters.add(letter)
    # Check if the letter on word2 are 
    for letter in word1:
        if letter not in seenLetters:
            return False
    return True            


if __name__ == "__main__":
    result = is_a_Permutation("atosx","Kratos") 
    print(result)   