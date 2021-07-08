import random


def insertion():
    sorted_list = [int(x) for x in range(0, 40)]
    to_insert = random.randint(0, 50)
    # to_insert = float(input('Type a natural number to insert'))
    print(sorted_list, to_insert)
    if sorted_list[-1] < to_insert:
        sorted_list.append(to_insert)
        return sorted_list
    for i in sorted_list:
        print(i)
        if to_insert <= i:
            sorted_list.insert(i, to_insert)
            return sorted_list


print(insertion())
