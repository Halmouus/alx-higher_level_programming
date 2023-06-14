#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    sum_w = sum(weight for score, weight in my_list)
    sum_s = sum(score * weight for score, weight in my_list)
    return sum_s / sum_w if sum_w != 0 else 0
