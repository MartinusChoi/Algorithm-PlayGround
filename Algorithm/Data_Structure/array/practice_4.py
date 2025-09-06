def solution(answers):
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]

    idx = [0,0,0]
    score = [0,0,0]

    result = []

    for answer in answers:
        if student_1[idx[0]] == answer : score[0] += 1
        if student_2[idx[1]] == answer : score[1] += 1
        if student_3[idx[2]] == answer : score[2] += 1

        if idx[0] == 4 : idx[0]=0
        else : idx[0] += 1
        if idx[1] == 7 : idx[1]=0
        else : idx[1] += 1
        if idx[2] == 9 : idx[2]=0
        else : idx[2] += 1

    max_score = max(score)
    for id, val in enumerate(score):
        if val == max_score : result.append(id+1)
    
    return result
