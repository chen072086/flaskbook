#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

# coding:utf-8
def num_div(num1,num2):
    assert isinstance(num1,int)
    assert isinstance(num2,int)
    print(num1/num2)

if __name__=='__main__':
    #num_div("a","b")
    num_div(10,3)
