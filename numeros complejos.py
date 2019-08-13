from sys import stdin

def sumar(a,b,c,d):
    pr = a+c
    pi = b+d
    if pi>0: resp = "{}+{}i".format(pr,pi)
    else: resp = "{}-{}i".format(pr,pi)
    return resp
def restar(a,b,c,d):
    pr = a-c
    pi = b-d
    if pi>0: resp = "{}+{}i".format(pr,pi)
    else: resp = "{}-{}i".format(pr,pi)
    return resp
def producto(a,b,c,d):
    pp = a*c
    pq = b*d
    px = a*d
    pz = b*c
    pr = pp-pq
    pi = px+pz
    if pi>0: resp = "{}+{}i".format(pr,pi)
    else: resp = "{}{}i".format(pr,pi)
    return resp
def division(a,b,c,d):
    pp = a*c
    px = a*-d
    pz = b*c
    pq = b*-d
    pa = pp-pq
    pb = px+pz
    pc = (c*c)-(d*-d)
    if pb/pc>0: resp = "{}+{}i".format(pa/pc,pb/pc)
    else: resp = "{}{}i".format(pa/pc,pb/pc)
    return resp
    
def separar(q,w):
    s = q[0]
    band = True
    pr,o,pi = "","",""
    cont = 0
    while band:
        if s not in ["+","-","*","/"] or cont == 0 :
            pr+=s
            s = q[cont+1]
            cont+=1
        else:
            band =False
    for x in range(cont,len(q)-2):
        pi+=q[x]
    return int(pr),int(pi)
    
def main():
    z = [x for x in stdin.readline()]
    w = [y for y in stdin.readline()]
    prz,piz = separar(z,0)
    prw,piw = separar(w,0)
    print("sumar = ",sumar(prz,piz,prw,piw))
    print("restar = ",restar(prz,piz,prw,piw))
    print("producto = ",producto(prz,piz,prw,piw))
    print("division = ",division(prz,piz,prw,piw))
    
main()
