print("Welcome to the Student Grading Program!")

while True:
    student_name = input("Enter the student's name (type 'exit' to quit): ")

    if student_name.lower() == 'exit':
        print("Exiting the Student Grading Program. Goodbye!")
        break

    valid_marks = False
    while not valid_marks:
        try:
            marks = float(input("Enter the marks obtained by the student: "))
            if 0 <= marks <= 100:
                valid_marks = True
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")

    if marks >= 90:
        grade = 'A+'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'Fail'

    print(f"Grade for {student_name}: {grade}\n")
