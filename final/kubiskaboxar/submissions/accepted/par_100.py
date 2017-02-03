import sys

def test(s,cbox):
    n=[0,0,0]
    for d in cbox:
        n[1]-=min(n[1],d[s[2]])
        n[0]-=min(n[0],d[s[1]])
        for i in range(3): n[i]+=d[s[i]]
    return sum(n)

N=int(sys.stdin.readline())
box={}
for i in range(N):
    fields=sys.stdin.readline().split()
    n=int(fields[0])
    if not n in box:
        box[n]={'R':0,'G':0,'B':0}
    box[n][fields[1]]+=1
cbox=[v for k,v in sorted(box.iteritems())]
m=N+1
for a in ["RGB","GBR","BRG","RBG","GRB","BGR"]:
    r=test(a,cbox)
    if(r<m):
        m=r
        bra=a
print "%c i %c\n%c i %c\n%d\n" % (bra[0],bra[1],bra[1],bra[2],m)
