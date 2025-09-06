import math

def solution(progresses:list, speeds:list) -> list:
    distirb_per_day = []
    task_amount = len(progresses)
    

    # 각 task가 완료되기 까지 남은 날짜 계산
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(task_amount)]

    day_distrib = 0
    cur_max_day_left = days_left[0]

    for i in range(task_amount):
        if days_left[i] <= cur_max_day_left:
            day_distrib += 1
        else:
            distirb_per_day.append(day_distrib)
            day_distrib = 1
            cur_max_day_left = days_left[i]
    distirb_per_day.append(day_distrib)
    
    return distirb_per_day