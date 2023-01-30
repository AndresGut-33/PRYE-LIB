def media(list = []):
    return sum(list) / len(list)
def mediana(list = []):
    data = len(list)
    if data % 2 == 0:
        return (list[(data // 2) - 1] + list[(data // 2) ]) / 2
    else:
        return list[data // 2]
    return False
def media_recortada(list, percent):
    delData = round(len(list) * percent)
    while delData > 0:
        list.pop()
        list.pop(0)
        delData = delData - 1
    return media(list)
def varianza(list):
    n = len(list)
    media_ = media(list)
    s2 = 0
    for i in range(n):
        s2 += (list[i]-media_) ** 2
    return s2/(n-1)
def desviacion(list):
    return varianza(list) ** (1/2)
def main():
    print("Exercise 1.1, 1.7")
    list = [2.5, 2.8, 2.8, 2.9, 3.0, 3.3,3.4,3.6,3.7,4.0,4.4,4.8,4.8,5.2,5.6]
    list.sort()
    print(len(list), list)
    print(media(list))
    print(mediana(list))
    print(media_recortada(list, 0.2))
    print(varianza(list))
    print(desviacion(list))
    print("------------")
    print("Exercise 1.2, 1.8")
    list2=[18.71, 21.41, 20.72, 21.81, 19.29, 22.42, 20.17, 23.71, 19.44, 20.50, 18.92, 20.33, 23.00, 22.85, 19.25, 21.77, 22.11, 19.77, 18.04, 21.12]
    list2.sort()
    print(len(list2), list2)
    print(media(list2))
    print(mediana(list2))
    print(media_recortada(list2, 0.1))
    print(varianza(list2))
    print(desviacion(list2))


main()
