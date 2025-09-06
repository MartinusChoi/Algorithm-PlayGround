from collections import Counter

def get_reportusers_per_user(report:list) -> dict:
    result = {}
    
    for report_content in report:
        user_id, reported_id = report_content.split(" ")
        if user_id in result: result[user_id].add(reported_id)
        else: result[user_id] = {reported_id}
    
    return result

def get_reportnum_per_user(reportusers_per_user:dict) -> dict:
    report_pool = []

    for reportuser_set in reportusers_per_user.values():
        report_pool.extend(list(reportuser_set))
    
    return Counter(report_pool)

def get_banned_users(reportnum_per_user:dict, k:int) -> set:
    banned_users = set()

    for user_id, report_num in reportnum_per_user.items():
        if report_num >= k : banned_users.add(user_id)
    
    return banned_users

def solution(id_list:list, report:list, k:int) -> list:
    reportusers_per_user = get_reportusers_per_user(report)
    reportnum_per_user = get_reportnum_per_user(reportusers_per_user)
    banned_users = get_banned_users(reportnum_per_user, k)

    mail_nums = []
    for user_id in id_list:
        if user_id in reportusers_per_user:
            mail_nums.append(len(reportusers_per_user[user_id] & banned_users))
        else:
            mail_nums.append(0)

    return mail_nums