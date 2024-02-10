from itertools import chain


def avg_array(arrs):
    result = []
    for i in range(len(arrs[0])):
        s = 0
        for j in range(len(arrs)):
            s += arrs[j][i]
        result.append(s/len(arrs))
    return result


def avg_array1(arrs):
    return [sum(a)/len(a) for a in zip(*arrs)]


print(avg_array1([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3],
                  [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]))
