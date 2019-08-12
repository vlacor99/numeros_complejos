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
    else: resp = "{}-{}i".format(pr,pi)
    return resp
def separar(q):
    s = q[0]
    band = True
    pr,o,pi = "","",""
    cont = 0
    while band:
        if s not in ["+","-","*","/"] :
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
    prz,piz = separar(z)
    prw,piw = separar(w)
    print("sumar",sumar(prz,piz,prw,piw))
    print("restar",restar(prz,piz,prw,piw))
    print("producto",producto(prz,piz,prw,piw))
main()
