def solution(arr:list[int]) -> list:
    arr = list(set(arr))
    arr.sort(reverse=True)

    return arr