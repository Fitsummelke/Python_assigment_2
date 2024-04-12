# this function is used to Register new students
def register_student():
    print(" Student Registration Form list ")
    try:
        number_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Please enter a correct number.")
        register_student()
        return
    
    with open("student.txt", 'a+') as file:
        for i in range(number_students):
            st_id = input(f"Enter student id : ")
            file.seek(0)  # this function Reset the file pointer to beginning which used to read from the star of the file
            for line in file:
                if st_id in line:
                    print("The ID already exists. Please enter a new ID...")
                    st_id = input("Enter student id: ")
            st_name = input("Enter student name: ")
            try:
                st_gpa = float(input("Enter student GPA: "))
            except ValueError:
                print("Invalid GPA. Please enter a valid GPA.")
                continue
            while st_gpa < 0 or st_gpa > 4:
                print("Please enter the correct GPA (between 0 and 4)...")
                try:
                    st_gpa = float(input("Enter student GPA: "))
                except ValueError:
                    print("Invalid GPA. Please enter a valid GPA.")
                    continue
            st_dep = input("Enter the department: ")
            valid_gender = False
            while not valid_gender:
                st_gen = input("Enter student gender (male/female): ").lower()
                if st_gen in ['male', 'female']:
                    valid_gender = True
                else:
                    print("Invalid gender. Please enter 'male' or 'female'.")
            file.write(f"{st_id};{st_name};{st_gen};{st_dep};{st_gpa}\n")
            print("Registered successfully.")
    print("****************************************************************")
    menu()

# this Function is used to find or search a student using there student id and display the searched student information
def search_student():
    try:
        id_search = input("Enter student ID: ")
        with open("student.txt", 'r') as file:
            found = False
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if stid == id_search:
                    print("____student found____") 
                    print(f"Name: {name}\nGender: {gender}\nGPA: {gpa}")
                    found = True
                    break
            if not found:
                print(f"Student with an id number {stid} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# this fuction used to modify or Update the name of a given student
def update_student_name():
    try:
        new_modified = False
        lines = []

        while not new_modified:
            st_id = input("Enter student ID: ")
            with open("student.txt", 'r') as file:
                for line in file:
                    stid, name , gender, dep, gpa = line.split(";")
                    if st_id == stid:
                        new_name = input(" Enter the new corrected Name: ")
                        line = f"{stid};{new_name};{gender};{dep};{gpa}\n"
                        new_modified = True
                        print(f"Data of student {st_id} updated successfully.")
                    lines.append(line)

                if not new_modified:
                    print(f"Student with ID {st_id} not found. Please enter a valid ID.")

        with open("student.txt", 'w') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()



# this function is used to Update or correct student GPA
def  update_student_gpa():
    try:
        st_id = input("Enter student ID: ")
        updated = False
        lines = []

        with open("student.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.split(";")
                if st_id == stid:
                    try:
                        new_gpa = float(input("Enter corrected New GPA: "))
                    except ValueError:
                        print("Invalid GPA. Please enter a valid GPA.")
                        return  # Return without updating if invalid GPA
                    
                    if new_gpa > 4 or new_gpa < 0:
                        print("Please enter the Correct GPA (between 0 and 4)...")
                    else:
                        line = f"{stid};{name};{gender};{dep};{new_gpa}\n"
                        updated = True
                        print(f"Data of student {name} has been updated successfully!")
                lines.append(line)

        if not updated:
            print(f"Student with ID {st_id} not found.")
        else:
            with open("student.txt", 'w') as file:
                file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()
# this function is used to count and display the number and information of the total number of students
def count_student():
    total_students = 0  # Initialize total number of students
    print("all Students information :\n")
    
    with open("student.txt", 'r') as file:
        for line in file:
            stid, name, gender, dep, gpa = line.strip().split(";")
            print(f"ID: {stid}\nName: {name}\nGender: {gender}\nDepartment: {dep}\nGPA: {gpa}\n")
            total_students += 1  # Increment total for each student

    print(f"Total number of students is : {total_students}")
    menu() 

# Function to delete a student information based on the student id
def delete_student():
    try:
        found = False
        lines = []

        while not found:
            st_id = input("Enter the student ID to delete : ")
            with open("student.txt", 'r') as file:
                for line in file:
                    stid, name, gender, dep, gpa = line.strip().split(";")
                    if st_id == stid:
                        found = True
                        print(f"Student with ID {st_id} has been deleted successfully.")
                    else:
                        lines.append(line)

            if not found:
                print(f"Student with ID {st_id} not found. Please enter a valid ID.")

        with open("student.txt", 'w') as file:
            file.writelines(lines)
    except Exception as e:
        print(f"An error occurred: {e}")
    menu()

# this fuction count the total number of male or female that are found
def count_gender():
    total = 0
    students_gender = input(" Input Student Gender male/female : ")
    with open("student.txt", 'r') as file:
        for line in file:
          stid, name, gender, dep, gpa = line.strip().split(";")
          if gender.lower() == students_gender.lower():
                total += 1
    print(f"the Total number of students who are {students_gender} is : {total}")
    menu()

# this function displays the top scoring students in the students database
def  top_scorer_department():
    with open("student.txt", "r") as file:
        st_dep = input("Enter the department: ").lower()
        max_gpa = 0
        max_name = ""
        for line in file:
            stid, name, gender, dep, gpa = line.split(";")
            dep = dep.lower()
            if dep == st_dep and float(gpa) > max_gpa:
                max_gpa = float(gpa)
                max_name = name
            
            
    print(f"the Top scoring student in {st_dep} department is : {max_name} with GPA {max_gpa}") 
    menu()

#  Function to find top scoring female student in a each department
def top_female_scorer__department():
    try:
        department = input("Enter the department: ")
        top_gpa = 0
        top_student = None

        with open("student.txt", "r") as file:
            for line in file:
                stid, name, gender, dep, gpa = line.strip().split(";")
                if dep.lower() == department and gender.lower() == "female" and float(gpa) > top_gpa:
                    top_gpa = float(gpa)
                    top_student = (stid, name, gender, dep, gpa)

        if top_student:
            stid, name, gender, dep, gpa = top_student
            print(f"Top scoring female student in {dep} deparetement is {name}, with GPA: {gpa} ")
        else:
            print(f"No top scoring female student found in {department}.")
    except Exception as e:
        print(f"An error occurred: {e}")

    menu()


# Function to searchor find and display students information based on GPA threshold
def gpa_threshold():
    try:
        threshold_gpa = float(input("Enter the GPA threshold: "))
        found_students = []

        with open("student.txt", 'r') as file:
            for line in file:
                stid, name, gender, dep, gpa = line.strip().split(";")
                if float(gpa) > threshold_gpa:
                    found_students.append((stid, name, gender, dep, gpa))

        if found_students:
            print(f"Students with GPA above {threshold_gpa}:")
            for student in found_students:
                stid, name, gender, dep, gpa = student
                print(f"Name: {name}, with GPA: {gpa}")
        else:
            print(f"No students found with GPA above {threshold_gpa}.")
    except ValueError:
        print("Invalid input. Please enter a valid GPA.")

    menu()
# function to dislay the most Frequent  student names
def frequent_names():
    name_count={}
    with open("student.txt", "r") as file:
        for line in file:
            stid, name, gender, dep, gpa = line.split(";")
            if name in name_count:
              name_count[name] += 1
            else:
               name_count[name] = 1
        for name,count in name_count.items():    
          print( f"{name} : is frquented  {count} times\n" )
    menu()
# function to display total number of students of each departement
def students_per_department():
    department_counts = {}
    
    with open("student.txt", 'r') as file:
        for line in file:
            stid, name, gender, dep, gpa = line.split(";")
        
            department_counts[dep] = department_counts.get(dep, 0) + 1
    
    print("Number of students per department:")
    for department, count in department_counts.items():
        print(f"{department}: {count}")
    
    menu()

# this is the main function and contain the menu for the required 
def menu():
    print("((((((((((((((Student Management System)))))))))))))))))")
    print("0. Register new student")
    print("1. Search Student")
    print("2. Update Student Name")
    print("3. Update Student GPA")
    print("4. Delete Student Information")
    print("5. count and display total number of students")
    print("6. count total number of male and female students")
    print("7. display  name and departement of top scored students for each departement")
    print("8. display  name and departement of top scored female students for each departement")
    print("9. list names of students who scored greater than a given gpa")
    print("10. show frequent student names")
    print("11. show total number of students of each departement")
    print("12. EXIT")
    
    choice = input("Enter your choice (0-12): ")
    
    try:
        choice = int(choice)
        if choice == 0:
            register_student()
        elif choice == 1:
            search_student()
        elif choice == 2:
            update_student_name()
        elif choice == 3:
            update_student_gpa()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            count_student()
        elif choice == 6:
            count_gender()
        elif choice == 7:
            top_scorer_department()
        elif choice == 8:
            top_female_scorer__department()
        elif choice == 9:
            gpa_threshold()
        elif choice == 10:
            frequent_names()
        elif choice == 11:
            students_per_department()
        elif choice == 12:
            exit_program()
        else:
            print("Invalid choice! Please enter a number between 0 and 12 ")
         
    except ValueError:
        print(">    Please enter a number between 0 and 12   <")
    
        
# function for exiting the program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

menu()

if __name__ == "__main__":
    menu()



