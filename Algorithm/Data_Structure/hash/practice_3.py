def get_hash_table(participant, completion):
    hash_table = {name:0 for name in set(participant)}

    for name in participant: hash_table[name] += 1
    for name in completion: hash_table[name] -= 1

    return hash_table

def solution(participant, completion):
    hash_table = get_hash_table(participant, completion)

    for name in participant:
        if hash_table[name] > 0 : return name