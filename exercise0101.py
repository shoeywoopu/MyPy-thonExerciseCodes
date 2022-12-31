# This is a sample Python script.

"""
2023/1/1 python练习
"""

# 获得斐波那契数列前20个数
def getFibonacci():
    num1 = 1
    num2 = 1
    number = [1, 1]
    for n in range(0, 18):
        number.append(num1+num2)
        tep = num1
        num1 = num2
        num2 = num2 + tep
    return number

# 找10000内的所有完备数
def findPerfect():
    numb = [1]
    for n in range(2, 10001):
        num = 0
        for i in range(1, n-1):
            if n % i == 0:
                num += i
        if num == n:
            numb.append(n)
    return numb

# 找100以内所有的素数
def getPrime():
    numb = [2]
    for n in range(3, 101):
        isPrime = True
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
        if isPrime:
            numb.append(n)
    return numb


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nnum = getPrime()
    print(nnum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
