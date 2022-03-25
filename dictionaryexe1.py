#write a program that convert the below database to grade using the below grading system

#score 91-100 grade: Outstanding
#score 81-90 grade: exeeds expectation
#score 71-80 grade: Acceptable
#score 70 or lower grade: fail


student_scores={
    "Carol":81,
    "Job":78,
    "Zeddy":99,
    "Palmer":74,
    "Kenny":62
}
#create the empty dictionary 
student_grades={}
#edit element and append into the new_dictionary
for names in student_scores:
    score=student_scores[names]
    if score>90:
        student_grades[names]="Outstanding"
    elif score>80:
        student_grades[names]="exeeds expectation"
    elif score>70:
        student_grades[names]="Acceptable"
    elif score<70:
        student_grades[names]="Fail"
for names in student_grades:
    print(f"{names} has '{student_grades[names]}' grade")



