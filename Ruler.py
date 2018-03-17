# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:10:29 2018

@author: srima
"""

def ruler(a):

    second_row = "1234567890"

    indx = a

    rem = int(indx / 10)

    mod = indx%10

    string2 = ' '

    res=''

    for i in range(1,rem+1):

        string2 = str(i)

        str_len=10

        string_ruler = string2.rjust(str_len)

        res=res+("".join(str(string_ruler)))

    print(res)

    

    scale = ""

    if mod > 0:

            scale ="".join((second_row)for n in range(1,rem+1))

            scale =scale + (second_row[0:mod])

            print("".join(str(scale)),end='')

    else:

        scale =str("".join((second_row)for n in range(1,rem+1)))

        print(scale)



ruler(102)