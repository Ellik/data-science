import re
f = open('../StudentsPerformance.csv')

pattern = re.compile('\d+')

readingScore = []
for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    score = pattern.search(info[6])[0]
    readingScore.append(int(score))
f.close()

middleScore = sum(readingScore) / len(readingScore)
print(middleScore)
lowerMiddle = 0

for score in readingScore:
    if score < middleScore:
        lowerMiddle += 1
print(lowerMiddle)



