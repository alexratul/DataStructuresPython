
def palindrome_permutation(word):
    dictionary = {}

    for letter in word:
        if letter == ' ':
            continue

        letter = letter.lower()
        
        if not letter in dictionary and letter.isalpha():
            dictionary[letter] = 1
        else:
            dictionary[letter] = dictionary[letter] + 1    

    count_odd = 0
    for letter in dictionary:
        if dictionary[letter] % 2:
           count_odd = count_odd + 1  

    return count_odd <= 1          

def palindrome_permutation_mid_road(word): 
    alpha_chars_only = [x for x in word.lower() if x.isalpha()]
    from collections import Counter 
    counts = Counter(alpha_chars_only)

    count_odd = 0
    for letter in counts:
        if counts[letter] % 2:
           count_odd = count_odd + 1  

    return count_odd <= 1  


def palindrome_permutation_python_way(word):
    alpha_chars_only = [x for x in word.lower() if x.isalpha()]
    from collections import Counter 
    counts = Counter(alpha_chars_only)
    number_of_odd = sum(1 for letter, cnt in counts.items() if cnt%2)
    return number_of_odd <= 1    


if __name__ == "__main__":
    print(palindrome_permutation("test"))
    print(palindrome_permutation("tact coa"))