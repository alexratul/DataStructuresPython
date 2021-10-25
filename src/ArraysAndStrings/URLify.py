def main():
    print("hello world!")

def url_ify(word):
    result = ""
    index = 0
    max_index = len(word)
    while (index < max_index):
        letter = word[index]
        if letter.isspace(): 
            result = f"{result}{'%20'}"
            while(word[index].isspace()):
                index = index + 1
        else:
            result = f"{result}{letter}"
            index = index + 1

    return result   

if __name__ == "__main__":
    print(url_ify("Mr John Smith"))   