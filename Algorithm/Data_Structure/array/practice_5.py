def solution(arr1, arr2):
    result_mat = []

    for m in range(0, len(arr1)):
        sub_mat = []

        for k in range(0, len(arr2[0])):
            value = 0
            for n in range(0, len(arr1[0])):
                value += (arr1[m][n] * arr2[n][k])
            sub_mat.append(value)
        
        result_mat.append(sub_mat)
    
    return result_mat