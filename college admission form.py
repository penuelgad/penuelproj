users = {}


courses = {
    'multimedia systems': {'seats': 50, 'applicants': []},
    'python programming': {'seats': 40, 'applicants': []},
    'discrete mathematics': {'seats': 30, 'applicants': []}
}


def register():
    print("=== Register for College Admission ===")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return
    password = input("Enter password: ")
    users[username] = {'password': password, 'admission_status': 'you are admitted', 'course_preference': ''}
    print("Registration successful.")


def login():
    print("=== Login to College Admission System ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None


def view_admission_status(username):
    print("=== Admission Status ===")
    if username in users:
        print("Your admission status: ", users[username]['admission_status'])
    else:
        print("User not found.")


def display_courses():
    print("=== Available Courses ===")
    for course, details in courses.items():
        print(f"{course}: Seats Available - {details['seats']}")


def select_course(username):
    display_courses()
    choice = input("Enter your preferred course: ")
    if choice in courses:
        users[username]['course_preference'] = choice
        courses[choice]['applicants'].append(username)
        print("Course selection successful.")
    else:
        print("Invalid course choice.")


def main():
    while True:
        print("\n===== College Admission System =====")
        print("1. Register")
        print("2. Login")
        print("3. View Admission Status")
        print("4. Select Course Preference")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                view_admission_status(username)
        elif choice == '3':
            username = input("Enter your username: ")
            view_admission_status(username)
        elif choice == '4':
            username = input("Enter your username: ")
            select_course(username)
       
     
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()