# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

nato = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT GOLF HOTEL INDIA JULIETT KILO LIMA MIKE NOVEMBER OSCAR PAPA QUEBEC ROMEO SIERRA TANGO UNIFORM VICTOR WHISKEY X-RAY YANKEE ZULU".split()
morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
alph = "abcdefghijklmnopqrstuvwxyz"
scrab_scores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
scrab_counts = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]

def counts(s):
    c = {}
    for u in set(s):
        c[u] = len([x for x in s if x==u])
    for u in sorted(list(c.keys()),key=lambda x:c[x]):
        print(u+" "+str(c[u]))

def score(w,scores=scrab_scores,a=alph):
    s = {}
    for l,n in zip(a,scores):
        s[l]=n
    return sum([s.get(l.lower(),0) for l in w])
    
def transliterate(s,p,c):
    t = {}
    for x,y in zip(p,c):
        t[y] = x
    return "".join([t.get(l,".") for l in s])
    
def subtract_string(x,y,a=alph):
    rets = ""
    if len(x)<len(y):
        print("ping")
        x = x + "a"*(len(y)-len(x))
    elif len(y)<len(x):
        y = y + "a"*(len(x)-len(y))
    for k,l in zip(x,y):
        if k not in a:
            if l not in a:
                rets += "="
            else: 
                rets += "-"
        elif l not in a:
            rets += "_"
        else:
            rets += a[(score(k,range(len(a)),a)-score(l,range(len(a)),a)) % len(a)]
    return rets
    
def add_string(x,y,a=alph):
    rets = ""
    if len(x)<len(y):
        print("ping")
        x = x + "a"*(len(y)-len(x))
    elif len(y)<len(x):
        y = y + "a"*(len(x)-len(y))
    for k,l in zip(x,y):
        if k not in a:
            if l not in a:
                rets += "="
            rets += "-"
        elif l not in a:
            rets += "_"
        else:
            rets += a[(score(k,range(len(a)),a)+score(l,range(len(a)),a)) % len(a)]
    return rets