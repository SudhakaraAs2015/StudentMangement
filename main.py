student1={
    "math":65,
    "social":80,
    "science":75,
    "name":"Rohith"
}
student2={
    "math":78,
    "social":40,
    "science":100,
    "name":"sunil"
}
student3={
    "math":85,
    "social":78,
    "science":71,
    "name":"Sooraj"
}

student_list = [student1,student2,student3]



def display(student_list):
    math_score = 0
    math_scorer = ""

    for student in student_list:
        if(student.get('math')>math_score):
            math_score = student.get('math')
            math_scorer = student.get("name")
    print(f"Highest score in maths is {math_scorer} and score is {math_score}")

display(student_list)





