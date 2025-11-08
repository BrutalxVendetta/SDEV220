#Name: Nathaniel Gutshall
#File: Deans_List_Honor_roll
#Description
#   This app uses students first and last name and GPA to test weather the student Qualifies for the deans list or Honor roll.
#
#   The program stops when "ZZZ" is entered as the last name



while True:
    last_name = input("Enter The Student's Last Name:  ")
    if last_name.upper () == "ZZZ":
        print("Exiting program. Goodbye.")
        break
    

    first_name = input("Enter The Student's First Name:  ")


    try:
        gpa=float(input("Enter The student's GPA:  "))
    except ValueError:
        print("Invalid Input. GPA Must be a number. ")
        continue
    

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!\n")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll! \n")
    else:
        print(f"{first_name} {last_name} Did not qualify this term. \n")