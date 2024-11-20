
s  = "AGGCCGGTATATGCGATCTG"
s2 = "CGAAGTCCTCGGACTATGAA"
s3 = "CTTGGATAGAATCCATCCAC"
s4 = "GCGGTAATACTCAAGGTTCA"

l = len(s)
l2 = len(s2)
l3 =  len(s3)
l4 =  len(s4)

GCcont  = 0
GCcont2 = 0
GCcont3 = 0
GCcont4 = 0


for i in s:
    if i == "C":
        GCcont = GCcont + 1
    if i == "G":
        GCcont = GCcont + 1

for i in s2:
    if i == "C":
        GCcont2 = GCcont2 + 1
    if i == "G":
        GCcont2 = GCcont2 + 1

for i in s3:
    if i == "C":
        GCcont3 = GCcont3 + 1
    if i == "G":
        GCcont3 = GCcont3 + 1

for i in s4:
    if i == "C":
        GCcont4 = GCcont4 + 1
    if i == "G":
        GCcont4 = GCcont4 + 1

print(l, l2, l3, l4)
print(GCcont / l, GCcont2 / l2, GCcont3 / l3, GCcont4 / l4)
print(max(GCcont/l, GCcont2/l, GCcont3/l, GCcont4/l))