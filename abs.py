import argparse #eisagoume thn bibliothhkh argsparse
parser = argparse.ArgumentParser()
parser.add_argument('hello_world', help = 'message')
args = parser.parse_args()

def diabasma_arxeiou(hello_world):
    with open(hello_world) as myfile:
        string=myfile.read()

    return string
d = diabasma_arxeiou(args.hello_world)
print(d)
print (len(d))

dicti= []
for letter in set(d):
    fre = d.count(letter, 0, len(d))
    t=letter, fre
    dicti.append(t)

print (dicti)
t=('',0)
dicti.append(t)
print(dicti)
#dicti1=[]
#dicti1=dicti[:]
def make_leaf(symbol, freq):
    return (symbol, freq)
#for i in range(len(dicti)):
while len(dicti)>1 :
    l=min(dicti, key=lambda t: t[1])
    o=make_leaf(l[0],l[1])
    #print(o)
    for index, s in enumerate(dicti):
        if s==l:
            position=index
    mini_proto=dicti.pop(position)
    #dicti1.pop(position)
    o=mini_proto

    print(l)
    print(position)
    print (dicti)

    l=min(dicti, key=lambda t: t[1])
    n=make_leaf(l[0], l[1])
    for index, s in enumerate(dicti):
        if s==l:
            position=index
    mini_deutero=dicti.pop(position)
    #dicti1.pop(position)
    n=mini_deutero

    print(l)
    print(position)
    print(dicti)
    l=min(dicti, key=lambda t: t[1])
    k=make_leaf(l[0], l[1])
    for index, s in enumerate(dicti):
        if s==l:
            position=index
    mini_trito=dicti.pop(position)
    #dicti1.pop(position)
    k=mini_trito

    print(l)
    print(position)
    node=((o,n,k,[o[0],n[0],k[0]]),o[1]+n[1]+k[1])
    print (node)
    #dicti.append(node)
    dicti.append(node)
    #print(dicti1)
    #dicti.insert(i,node)
    print(dicti)
print(node[0])
