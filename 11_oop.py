"""Practice object-oriented programming with classes and methods."""


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student: {self.name} | Grade: {self.grade}")

    def is_passing(self):
        return self.grade >= 50


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduce(self):
        print(f"Teacher {self.name} teaches {self.subject}.")


def main():
    student1 = Student("Ranjay", 82)
    student2 = Student("Sita", 45)
    student1.display()
    student2.display()
    print(f"{student1.name} passed: {student1.is_passing()}")
    print(f"{student2.name} passed: {student2.is_passing()}")

    teacher = Teacher("Mr. Sharma", "Python")
    teacher.introduce()


if __name__ == "__main__":
    main()
