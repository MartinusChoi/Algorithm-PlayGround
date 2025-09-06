import math

def hash(string:str)->int:
    p=31
    m=1000000007
    char_to_int = {char:(i+1) for i, char in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                                                        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                                                        'u', 'v', 'w', 'x', 'y', 'z'])}
    return sum([char_to_int[string[i]] * int(math.pow(p, i)) for i in range(len(string))]) % m

def get_hash_table(string_list:list, query_list:list)->dict:
    omega = set(string_list+query_list)
    hash_table = {hash(string):0 for string in omega}
    for string in string_list: hash_table[hash(string)] += 1
    return hash_table

def solution(string_list:list, query_list:list)->list:
    hash_table = get_hash_table(string_list, query_list)
    is_exists = []

    for query in query_list:
        if hash_table[hash(query)] == 1 : is_exists.append(True)
        else: is_exists.append(False)
    
    return is_exists