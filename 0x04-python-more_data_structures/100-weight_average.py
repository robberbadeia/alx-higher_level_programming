def weight_average(my_list=[]):
    t1, t2 = zip(*my_list)
    _sum, _mul = 0, 0
    for i in t2:
        _sum += i
    for j in range(len(t1)):
        _mul = _mul + (t1[j] * t2[j])
    return(_mul / _sum)
