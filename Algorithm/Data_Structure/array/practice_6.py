def solution(N, stages):
    stages.sort()

    fail_rates = []
    result = []

    for stage in range(N):
        if (stage+1) in stages:
            fail_rate = (stages.count(stage+1)) / (len(stages[stages.index(stage+1):]))
        else:
            fail_rate = 0
        
        fail_rates.append(fail_rate)
    
    fail_rate_dict = {}
    for idx, fail_rate in enumerate(fail_rates):
        if fail_rate in fail_rate_dict.keys():
            fail_rate_dict[fail_rate].append(idx+1)
        else:
            fail_rate_dict[fail_rate] = [idx+1]
    
    sorted_unique_fail_rates = sorted(fail_rate_dict.keys(), reverse=True)
    for fail_rate in sorted_unique_fail_rates:
        result.extend(fail_rate_dict[fail_rate])
    
    return result