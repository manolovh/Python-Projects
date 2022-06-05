class MusicSchool:
    students = {"Gino": [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric": [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue

# Add your methods below this line
    def print_students_data(self):
        for name in self.students:
            self.print_student(name)

    def print_student(self, name):
        print(f"Student: {name} who is {self.students[name][0]} years old and is taking {self.students[name][2]}")

    def add_student(self, name, data):
        self.students[name] = data

    # Add the students to a .txt file
    def save_students(self):
        with open("students.txt", "w") as students_file:
            for student in self.students:
                students_file.write(f"{student}\n")


# Create the instance
school = MusicSchool(8, 15000)

# Call the methods
school.print_students_data()
school.print_student("Gino")
school.add_student("Harry", [19, "993-224-211", ["Drums", "Guitar"]])

school.save_students()
