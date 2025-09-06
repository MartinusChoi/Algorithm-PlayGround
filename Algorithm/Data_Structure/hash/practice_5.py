def solution(record:list) -> list:
    user_table = {}
    cur_msg_idx = 0
    messages = []

    for record_content in record:
        record_contents = record_content.split()
        if len(record_contents) == 2: key, user_id = record_contents[0], record_contents[1]
        else : key, user_id, name = record_contents[0], record_contents[1], record_contents[2]

        if key == 'Enter':
            if user_id in user_table:
                if user_table[user_id][0] != name: user_table[user_id][0] = name
                user_table[user_id][1].append(cur_msg_idx)
            else:
                user_table[user_id] = [name, [cur_msg_idx]]
            messages.append("{name}님이 들어왔습니다.")
            cur_msg_idx += 1
        
        elif key == 'Leave':
            user_table[user_id][1].append(cur_msg_idx)
            messages.append("{name}님이 나갔습니다.")
            cur_msg_idx += 1
        
        elif key == 'Change':
            user_table[user_id][0] = name
        
    for user_id in user_table.keys():
        for msg_idx in user_table[user_id][1]:
            messages[msg_idx] = messages[msg_idx].format(name=user_table[user_id][0])
    
    return messages