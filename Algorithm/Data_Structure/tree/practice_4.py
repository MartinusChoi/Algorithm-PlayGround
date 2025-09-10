"""
핵심 아이디어:
    - 반드시 부모의 이름이 먼저 나오고, 부모-자식의 관계를 매핑할 수 있음
    - 직접 트리를 구축하는 것이 아닌, dict에 자식->부모의 관계만 매핑
    - seller와 amount를 순회하면서 해당 seller부터 부모로 타고 올라가면서 수익의 10%를 분배

주의
    - 직접 구축할 시 올바르게 계산해도 시간초과 발생 
        -> 입력되는 enroll과 seller의 길이를 고려했을 떄, 특정 노드를 탐색하고 그 위로 올라가는 과정이 복잡함
    - dictionary로 부모-자식 관계만 매핑하고, 올라가는 것이 효율적

학습 결과
    - 트리의 하위에서 올라가는 연산을 수행해야할 떄에는, 단순히 부모-자식 관계만 매핑하서 타고 올라가는 것이 효율적임
"""

from typing import List

def solution(
    enroll:List[str],
    referall:List[str],
    seller:List[str],
    amount:List[int]
):
    child_to_parent = dict(zip(enroll, referall))
    profit_dict = {name:0 for name in enroll}

    for seller_name, sell_amount in zip(seller, amount):
        cur_node = seller_name
        profit = sell_amount * 100
        loyalty = profit // 10
        profit -= loyalty

        profit_dict[cur_node] += profit

        while (loyalty > 0) and (child_to_parent[cur_node] != "-"):
            profit_dict[child_to_parent[cur_node]] += (loyalty - loyalty // 10)
            loyalty //= 10
            cur_node = child_to_parent[cur_node]
        
    result = []
    for name in enroll:
        result.append(profit_dict[name])
    
    return result

        

if __name__ == "__main__":
    enroll = [
        "john",
        "mary",
        "edward",
        "sam",
        "emily",
        "jaimie",
        "tod",
        "young"
    ]
    referall = [
        "-",
        "-",
        "mary",
        "edward",
        "mary",
        "mary",
        "jaimie",
        "edward"
    ]
    seller = [
        "young",
        "john",
        "tod",
        "emily",
        "mary"
    ]
    amount = [
        12,
        4,
        2,
        5,
        10
    ]
    solution(enroll, referall, seller, amount)
    result = solution(enroll, referall, seller, amount)

    print(result)