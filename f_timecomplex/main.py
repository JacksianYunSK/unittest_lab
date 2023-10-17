
def all_combinations(lst):

    if len(lst) == 0:
        return [[]]

    combinations = all_combinations(lst[:-1])
    next_elem = lst[-1]
    return combinations + [item + [next_elem] for item in combinations]


if __name__ == '__main__' : 
    ret = all_combinations([1,2,3])
    print(ret)