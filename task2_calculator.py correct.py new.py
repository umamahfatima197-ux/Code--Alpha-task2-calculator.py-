def calculate_grades():
    print("--- Student Grade Calculator ---")
    
    # 1. Enter inputs 
    # Using float so we can enter decimal marks if needed
    math = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    computer = float(input("Enter Computer Science marks: "))
    urdu = float(input("Enter Urdu marks:"))
    english = float(input("Enter English marks:"))
    pak_studies = float(input("Enter Pakistan Studies marks:"))

    # 2. Calculate Total and Percentage
    total_obtained = math + physics + computer
    total_possible =600  #Lets assume 100 marks for each subject
    percentage = (total_obtained / total_possible) * 100
    
    print(f"\nTotal Marks: {total_obtained}/{total_possible}")
    print(f"Percentage: {percentage}%")
    
    # 3. Grade Logic (The Decision Maker)
    if percentage >=90:
        grade = "A-1"
        feedback = "Excellent work! You are ready for University."
    elif percentage >=80:
        grade = "A"
        feedback = "Very good! Keep maintaining this  work ethic and you will acheive great results."
    elif percentage >=70:
        grade = "B"
        feedback = "Good effort. You can improve with more practice."
    elif percentage >=60:
        grade = "C"
        feedback = "You passed, but you need to focus more on your studies."
    elif percentage >=50:
        grade ="D"
        feedback= "Not satisfactory. You need to work hard."
    elif percentage >=40:
        grade = "E"
        feedback = "Poor performance. Consider seeking help and put more efforts into your studies."
    else:
        grade = "F"
        feedback = "Fail. Please revise your syllabus and try again."
    
    # 4. Final Output
    print(f"Grade: {grade}")
    print(f"Feedback: {feedback}")

# Start the program
calculate_grades()