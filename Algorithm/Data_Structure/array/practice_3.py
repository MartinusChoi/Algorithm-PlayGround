def solution(arr):
    result = []

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            value = arr[i] + arr[j]
            if value not in result: result.append(value)
    
    result.sort()

    return result