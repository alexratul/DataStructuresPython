def compressor(word):
    if(len(word) == 1):
        return word

    #main logic 
    result =""
    counter = 1
    index = 1
    current_letter = word[0]

    while(index < len(word)):
        
        if(word[index] == current_letter):
            counter = counter + 1
        else:
            result = result + current_letter + str(counter)
            counter = 1
            current_letter = word[index]     

        index = index + 1

    if(counter > 1):
       result = result + current_letter + str(counter)         

    #case of compression is larger than original word
    if (len(result) > len(word)):
        return word
    
    return result

if __name__ == "__main__":
    print(compressor("aabcccccaaa"))
    print(compressor("result"))
    print(compressor("r"))      