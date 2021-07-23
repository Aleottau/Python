import math
from math import ceil
zonas = int(input()) 
av = 16600
a = 50600
b = 19200
c = 36900
d = 40500
e = 34200
i = 0
total_a = 0
prop_a=0
prop_b=0
prop_c=0
prop_d=0
prop_e=0
if zonas > 0 :
    while (i < zonas)  :
        area = float(input()) 
        cant = int(input()) 
        tip = input() 
        if (tip.lower() == "a"  and  cant >= 0) :
            ta = ceil((area - (av*cant))/a)
            if ta >= 0 :
                total_a += ta
                prop_a += ta
            else : 
                ta = 0
                total_a += ta
                prop_a += ta   
        elif (tip.lower() == "b"  and  cant >= 0) :
            tb = ceil((area - (av*cant))/b)
            if tb >= 0 :
                total_a += tb
                prop_b += tb
            else : 
                tb = 0
                total_a += tb
                prop_b += tb
        elif (tip.lower() == "c"  and  cant >= 0) :
            tc = ceil((area - (av*cant))/c)
            if tc >= 0 :
                total_a += tc
                prop_c += tc
            else : 
                tc = 0
                total_a += tc
                prop_c += tc
        elif (tip.lower() == "d"  and  cant >= 0) :
            td = ceil((area - (av*cant))/d)
            if td >= 0 :
                total_a += td
                prop_d += td
            else : 
                td = 0
                total_a += td
                prop_d += td
        elif (tip.lower() == "e"  and  cant >= 0) :
            te = ceil((area - (av*cant))/e)
            if te >= 0 :
                total_a += te
                prop_e += te
            else : 
                te = 0
                total_a += te
                prop_e += te 
        else :
            total_a += 0
        i += 1

    ra = (prop_a/total_a)* 100
    rb = (prop_b/total_a)* 100
    rc = (prop_c/total_a)* 100
    rd = (prop_d/total_a)* 100
    re = (prop_e/total_a)* 100
    print(ceil(total_a))
    print(f"a {format(ra,'0.2f')}%")
    print(f"b {format(rb,'0.2f')}%")
    print(f"c {format(rc,'0.2f')}%")
    print(f"d {format(rd,'0.2f')}%")
    print(f"e {format(re,'0.2f')}%")
else :

    ra = 0
    rb = 0
    rc = 0
    rd = 0
    re = 0
    print(ceil(total_a))
    print(f"a {format(ra,'0.2f')}%")
    print(f"b {format(rb,'0.2f')}%")
    print(f"c {format(rc,'0.2f')}%")
    print(f"d {format(rd,'0.2f')}%")
    print(f"e {format(re,'0.2f')}%")