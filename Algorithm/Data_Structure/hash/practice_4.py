def get_hash_table(want:list, number:list) -> dict:
    return {product:amount for product, amount in zip(want, number)}

def solution(want:list, number:list, discount:list):
    window_left = 0
    window_right = 10
    good_days = 0

    while window_right <= len(discount):
        hash_table = get_hash_table(want, number)
        discount_window = discount[window_left:window_right]
        completed_product = 0

        for product in discount_window:
            if product in hash_table.keys(): 
                hash_table[product] -= 1
                if hash_table[product] == 0 : completed_product += 1
        
        if completed_product == len(want) : good_days += 1

        window_left += 1
        window_right += 1
    
    return good_days