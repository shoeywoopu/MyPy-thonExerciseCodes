import os
import time
import random

# 在屏幕上显示跑马灯文字
def MarqueeText():
    content = '好想吃达美乐啊啊啊..'
    while True:
        print(content)
        os.system('cls')
        time.sleep(0.2)
        content = content[1:]+content[0]

# 产生指定长度的验证码
def Generate_Code(lens):
    '''

    :param lens: 指定的验证码长度
    :return: 由大小写英文字母和数字构成的随机验证码
    '''
    all_codes = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_codes)-1
    res = ''
    for _ in range(lens):
        index = random.randint(0, last_pos)
        res += all_codes[index]
    return res

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def printTriangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
    return




if __name__ == '__main__':

    print(Generate_Code(6))
    print(which_day(2002, 8, 10))
    printTriangle()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
