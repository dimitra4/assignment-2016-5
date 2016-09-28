import argparse #eisagoume thn bibliothhkh argsparse
parser = argparse.ArgumentParser()
parser.add_argument('hello_world', help = 'message')
args = parser.parse_args()

def diabasma_arxeiou(hello_world):
    with open(hello_world) as myfile:
        string=myfile.read().replace('\n','')

    return string
d = diabasma_arxeiou(args.hello_world)
print(d)
print (len(d))

dicti = {} #vriskontai t grammata kai oi syxnothtes
for letter in set(d):
    fre = d.count(letter, 0, len(d))
    dicti[letter] = fre
print (dicti)
