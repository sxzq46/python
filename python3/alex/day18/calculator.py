# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/14
import re

def format(s):
    s = s.replace(' ', '')
    s = s.replace('++', '+')
    s = s.replace('-+', '-')
    s = s.replace('+-', '-')
    s = s.replace('--', '+')
    s = s.replace('*+', '*')
    s = s.replace('/+', '/')
    # 例：格式化01为1
    a_format = re.sub('^0\d+','\d+',s)
    return a_format

def check(s):
    s = format(s)
    flag = True
    # 检查是否有除数字、小括号、+-*/.以外的字符
    illegal_character = re.findall('[^\d()+\\-*/.]', s)
    # 检查是否存在+|-后面接*|/,或者*|/后面接/
    illegal_operator = re.findall('([+|\\-/]+[*|/])|([*|/]+/)', s)
    # 检查(后面直接接*/.或者+-*/后面直接接)或者直接出现()或者)(或者)数字(
    illegal_parentheses = re.findall('((\([*/.]+|[+\\-*/.]+\))|(\(\)))|((\)\d+|\d+\()|(\)\())', s)
    # 检查左右括号数量是否一致
    left_parentheses = len(re.findall('\(', s))
    right_parentheses = len(re.findall('\)', s))
    if illegal_character or illegal_operator or illegal_parentheses or left_parentheses != right_parentheses :
        flag = False
    return flag

def mul_div(s):
    s = format(s)
    # 数字类型需考虑小数点的情况，例：8.888
    ret1 = re.search('\d+\.?\d*[*/]\-?\d+\.?\d*',s).group()
    x,y = re.split('[*/]',ret1)
    if "*" in ret1:
        ret2 = str(float(x)*float(y))
    else:
        ret2 = str(float(x)/float(y))
    # 将计算结果替换掉公式
    s = s.replace(ret1,ret2)
    s = re.sub('[()]','',s)
    return s

def add_sub(s):
    s = format(s)
    ret1 = re.search('\-?\d+\.?\d*[+\\-]\d+\.?\d*', s).group()
    # 加减计算公式需要考虑到类似 -1+2 负数开头的情况
    if re.search('^\-',ret1):
        x = re.search('^\-\d+\.?\d*', ret1).group()
        ret = re.sub('^\-', '', ret1)
        z, y = re.split('[+\\-]', ret)
    else:
        x, y = re.split('[+\\-]', ret1)
    if "+" in ret1:
        ret2 = str(float(x)+float(y))
    else:
        ret2 = str(float(x)-float(y))
    s = s.replace(ret1,ret2)
    return s

if __name__ == '__main__':
    a = input('请输入你的表达式或输入q退出:')
    while not check(a):
        if a == 'q':
            break
        else:
            a = input('错误表达式，请重新输入或输入q退出：')
    else:
        a_format = format(a)
        # 判断公式中是否出现括号
        while re.search('\(',a_format):
            #l1 搜索到括号中不带括号的公式。即最先计算公式
            l1 = re.compile('\([^()]+\)')
            for i in l1.finditer(a_format):
                i = i.group()
                replace_i = i
                # 搜索乘除，即括号最里面的先计算乘除，后计算加减
                while re.search('[*/]',i):
                    i = mul_div(i)
                else:
                    while re.search('[+\\-]',i):
                        if re.findall('^-\d+\.*\d*$',i):
                            break
                        i = add_sub(i)
                    #讲括号里计算完成的内容替换原有的公式中
                    a_format = a_format.replace(replace_i,i)
        else:
            while re.search('[*/]',a_format):
                a_format = mul_div(a_format)
            else:
                while re.search('[+\\-]', a_format):
                    if re.findall('^-\d+\.*\d*$', a_format):
                        break
                    a_format = add_sub(a_format)

    print(a_format)
