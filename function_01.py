def menu():
    print("1. Add new student id and name")
    print("2. Update student name")
    print("3. Delete student")
    print("4. show all students")
    print("0. Quit")

if __name__ == "__main__":
    students = {}
    while True:
        menu()
        choice = input("Enter choice: ")
        if 0 <= int(choice) <= 4:
            if choice == '0':
                exit()
            elif choice == '1':
                id, name = input("Enter student id and name (use ; to separate): ").split(';')
                students[id] = name
            elif choice == '2':
                id, newName = input("Enter student id and NEW name (use ; to separate): ").split(';')
                students[id] = newName
            elif choice == '3':
                id = input("Enter student id: ")
                del students[id]
            elif choice == '4':
                print( f"{'ID':12s}{'Name':20s}" )
                print( "--" * 16 )
                for id, name in students.items():
                    print( f"{id:12s}{name:20s}" )
            print()
        else:
            print("Invalid choice")

'''
test sample data:
D1234567;John Doe
D2345678;Jane Doe
D3456789;Tom Smith
D4567890;Jerry Smith
'''

