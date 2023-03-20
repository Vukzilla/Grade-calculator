import math

count = 0
total2 = 0
totalscore = 0 

with open("grades.txt", "rt") as f:
    text = f.read()

    for line in text.split("\n"):
        period, grades_text = line.split(" - ")
        grades_list = [int(g) for g in grades_text.split(",")]
        print(f"{period}: {grades_list}")
        count = 0 + len(grades_list)
        total = sum(grades_list)
        total2 += 1
        score = round(total / count, 2)
        rounded_score = round(score)

        if(score == 1.5 or score == 2.5 or score == 3.5 or score == 4.5):
            rounded_score = rounded_score + 1

        totalscore += rounded_score
        print(score, rounded_score)

tt = round(totalscore / total2, 2)
print("total grade count is: ", tt)