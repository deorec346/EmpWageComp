#UC1 checking employee is present r not

import random


class Employee:
    @staticmethod
    def check_attendance():
        is_present = (random.randint(0, 1))
        if is_present == 1:
            print("Employee is present")
        else:
            print("Employee is Absent")


if __name__ == '__main__':
    print("Welcome To Employee Wage Management System !!\n")
    Employee.check_attendance()
