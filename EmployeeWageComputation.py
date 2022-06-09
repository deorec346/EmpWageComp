# Add Part time Employee & calculate daily Wage

import random


class EmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 0
    EMP_WAGE_PER_HOUR = 20
    employeeHours = 0

    def checkEmpAttendance(self):
        attendance = random.randint(0, 2)
        if attendance == EmployeeWage.IS_FULL_TIME:
            EmployeeWage.employeeHours = 8
            return "Employee is Present for Full Time"
        elif attendance == EmployeeWage.IS_PART_TIME:
            EmployeeWage.employeeHours = 4
            return "Employee is Present for Part Time"
        else:
            return "Employee is Absent"

    def calculateDailyEmpWage(self):
        dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * EmployeeWage.employeeHours
        return "Employee Daily Wage is : " + str(dailyWage)


if __name__ == "__main__":
    employee = EmployeeWage()
    print(employee.checkEmpAttendance())
    print(employee.calculateDailyEmpWage())