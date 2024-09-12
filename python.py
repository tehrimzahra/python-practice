def manage_student_database():
    student_list = []  # List to hold student tuples (ID, name)
    student_id = 1     # Start ID numbering from 1
    student_names = set()  # Set to track names and prevent duplicates

    while True:
        name = input("Enter student name (or type 'stop' to finish): ").strip()
        
        if name.lower() == 'stop':
            break
        
        if name in student_names:
            print(f"Duplicate found: {name} is already in the list.")
            continue
        
        student_list.append((student_id, name))  # Append the tuple (ID, name)
        student_names.add(name)  # Add name to set to track duplicates
        student_id += 1

    # Display all students as tuples
    print("\nStudent List (ID, Name):")
    for student in student_list:
        print(student)

    # Display each student's ID and Name
    print("\nStudent Details:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Total number of students
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")

    # Calculate total length of all student names
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {total_name_length}")

    # Find the student with the longest name
    if student_list:
        longest_name_student = max(student_list, key=lambda x: len(x[1]))
        print(f"Student with the longest name: {longest_name_student[1]} (ID: {longest_name_student[0]})")

        # Find the student with the shortest name
        shortest_name_student = min(student_list, key=lambda x: len(x[1]))
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")

# Call the function to run the student database manager
manage_student_database()




