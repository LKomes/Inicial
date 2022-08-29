if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    qnt = len(student_marks[query_name])
    todas = student_marks[query_name]
    soma = 0
    for i in todas:
        soma += i
    media = float (soma/qnt)
    print ("%.2f"%media)
