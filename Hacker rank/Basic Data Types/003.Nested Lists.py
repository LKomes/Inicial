#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    list_scores = []
    list_names = []
    lst = []
    dicti = {}
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        dicti[name] = score
        list_scores.append (score)
        list_names.append (name)
minimo = 100
for a in list_scores:
    if minimo>a:
        minimo=a
b=min(i for i in list_scores if i != min(list_scores))

for g in list_names:
    if dicti[g] == b:
        lst.append(g)
for s in sorted(lst):
    print s   
