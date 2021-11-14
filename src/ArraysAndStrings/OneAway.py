def one_away(str_a, str_b):
    size_of_a = len(str_a)
    size_of_b = len(str_b)
    size_dif = abs(size_of_a - size_of_b)
    
    if(size_dif <= 1):
        if size_of_a > size_of_b: 
            return check_for_difference_on_words_different_size(str_a,str_b,size_of_a,size_of_b)
        elif size_of_a == size_of_b:
            return check_for_difference_on_words_same_size(str_a,str_b,size_of_a)
        else: 
            return check_for_difference_on_words_different_size(str_b,str_a,size_of_b,size_of_a)  
 
    return False  

def check_for_difference_on_words_different_size(a_word, b_word, size_of_a, size_of_b):
    current_index_of_a = 0
    current_index_of_b = 0
    number_of_differences = 0

    while(current_index_of_a != size_of_a and current_index_of_b != size_of_b):
        
        if(number_of_differences > 1):
            return False

        elif a_word[current_index_of_a] != b_word[current_index_of_b]:
            number_of_differences = number_of_differences + 1
            current_index_of_a = current_index_of_a + 1    
            
        else: 
            current_index_of_a = current_index_of_a + 1
            current_index_of_b = current_index_of_b + 1

    return True  


def check_for_difference_on_words_same_size(a_word, b_word, size):
    current_index = 0
    number_of_differences = 0

    while(current_index != size):
        
        if(number_of_differences > 1):
            return False

        if a_word[current_index] != b_word[current_index]:
            number_of_differences = number_of_differences + 1 
            
        current_index = current_index + 1

    return True


if __name__ == "__main__":
    print(one_away("pale","ple"))
    print(one_away("pales","pale")) 
    print(one_away("pale","bale")) 
    print(one_away("pale","bake"))   