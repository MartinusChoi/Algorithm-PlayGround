from typing import List

def solution(nums:List[int]) -> int:
    select_elements = len(nums) // 2
    unique_species = len(list(set(nums)))
    return min(select_elements, unique_species)

if __name__ == "__main__":
    nums = [3,1,2,3]

    print(solution(nums))