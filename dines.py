from collections import defaultdict
def get_var(eq, var):
    neg = eq['+']
    pos = eq['-']
    return -neg[var] if var in neg else pos[var] if var in pos else 0


def ensure_var(eq, var):
    if var in eq['+']: return
    if var in eq['-']: return
    eq['+'][var]=0

#Modify target_eq with source_eq per the Dines alogirhtm
def merge(source_eq, target_eq):
    new_eq = {}
#    for key, _ in source_eq['+'].items():
#        ensure_var(target_eq, key)
#    for key, _ in source_eq['-'].items():
#        ensure_var(target_eq, key)
    #Book keeping to make sure that source_eq knows about variables in target_eq
    for key, _ in target_eq['+'].items():
        ensure_var(source_eq, key)
    for key, _ in target_eq['-'].items():
        ensure_var(source_eq, key)
    
    for vari, coefficienti in source_eq['+'].items():
        for varj, coefficientj in source_eq['-'].items():
            coefficientj = -coefficientj
            target_coefficienti = get_var(target_eq, vari)
            target_coefficientj = get_var(target_eq, varj)
            #Find the new coefficient per Dines algorithm
            new_coefficient = ((coefficienti * target_coefficientj) - (coefficientj*target_coefficienti))
            #Create a new variable to track this
            key = vari + varj if vari<varj else varj+vari
            if key in new_eq:
                new_eq[key]+= new_coefficient
            else:
                new_eq[key] = new_coefficient

    new_eq_final = {'+':{}, '-':{}}
    for var, coefficient in new_eq.items():
        if coefficient == 0: continue
        sign = '+' if coefficient >=0 else '-'
        new_eq_final[sign][var] = abs(coefficient)

    return new_eq_final


#Does this equation have a solution?
def ok(eq):
    return len(eq['+'])>0 and len(eq['-'])>0

#Does this system of equations have a solution?
#NOTE this is currently inefficient
def has_positive_solution(es):
    while len(es)>1:
        #If there are equations that don't have positive and negative vars
        #then we're done
        if any(not ok(e) for e in es):
            return False
        #Pop off the top and merge it with the rest of the system
        rep = es.pop()
        for i, e in enumerate(es):
            es[i] = merge(rep, e)
    return all(ok(e) for e in es)

d1 = {'+':{'a':1},'-':{'b':1}}
d2 = {'+':{'c':1}, '-':{'d':1}}


print(has_positive_solution([d1,d2]))



#TODO unfinished
def make_eq(eq_str):
    eq_str = eq_str.replace(' ','')
    components = eq_str.split('+')
    for component in components:
        var_start = 0


eq1 = {'+': {"x1":1,"x3":1,"x4":1,"x5":1},
       '-': {"x2":1,"x6":1,"x7":1,"x8":1}}

eq2 = {'+': {"x1":1, "x2":2, "x4":2,"x6":2},
       "-": {"x3":1,"x5":1,"x7":1,"x8":2}}

eq3 = {'+': {'x1':1, 'x2':2, 'x3':3, 'x7':7},
       '-': {'x4':4, 'x5':5, 'x6':6, 'x8':8}}

#Examples
#print(merge(eq1, eq3))



t1 = {'+':{'x':1}, '-':{'y':1, 'z':1}}
t2 = {'+':{'x':2}, '-':{'y':1}}


#print(merge(t1,t2))


d1 = {'+':{'a':1},'-':{'b':1}}
d2 = {'+':{'c':1}, '-':{'d':1}}

#print(merge(d1,d2))


e1 = {'+': {'a':1,'b':1,'c':1,'f':1,'j':1},
      '-': {'d':1,'e':1,'g':1,'h':1,'i':1}}

e2 = {'+': {'l':1}, '-':{'k':1}}

e3 = {'+': {'n':1}, '-':{'m':1}}

e4 = {'+': {'o':1}, '-':{'g':1}}

e5 = {'+': {'q':1}, '-':{'p':1}}

e6 = {'+': {'s':1}, '-':{'r':1}}

e7 = {'+': {'u':1}, '-':{'t':1}}

e8 = {'+': {'b':1}, '-':{'d':1}}

e9={'+':{'d':1,'e':1,'g':1,'h':1},
    '-': {'a':1,'b':1,'c':1,'f':1}}

e10 = {'+':{'w':1}, '-':{'v':1}}

e11 = {'+':{'y':1}, '-':{'x':1}}

es = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11]




