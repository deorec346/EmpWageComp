import random


class Employee:

    def __init__(self, employee_name, emp_max_hr, emp_max_wage_per_hr, max_working_days):
        self.employee_name = employee_name
        self.emp_max_hour = emp_max_hr
        self.emp_wage_per_hour = emp_max_wage_per_hr
        self.max_working_days = max_working_days
        self.monthly_wage = self.calculate_wage

    def calculate_daily_wage(self, current_employee_hrs):
        return current_employee_hrs * self.emp_wage_per_hour

    @staticmethod
    def employee_attendance():
        """
            finding employee is present or not and also getting daily employee hours
        :return: employee hours
        """
        attendance = random.randint(0, 2)
        if attendance == 0:  # absent
            emp_hrs = 0
        else:
            if attendance == 2:  # Full day
                emp_hrs = 8
            else:  # Half day
                emp_hrs = 4
        return emp_hrs

    # Calculate Monthly Wages

    def calculate_wage(self):
        # global daily_wages
        total_hrs = 0
        total_days = 0
        monthly_wage = 0
        try:
            while total_hrs < self.emp_max_hour and total_days < self.max_working_days:
                emp_Hrs = Employee.employee_attendance()
                daily_wage = self.emp_wage_per_hour * emp_Hrs
                # print("\tDaily Wage :", daily_wage, "\n")
                # calculating monthly wage for an employee
                monthly_wage += daily_wage
                # calculating total working hours of a month for an employee
                total_hrs += emp_Hrs
                total_days += 1
        except Exception as e:
            print("Please do not press any button", e)
        return monthly_wage

    def __repr__(self):
        return f"Name: {self.employee_name}, emp rate {self.emp_wage_per_hour}, max hrs {self.emp_max_hour}"


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.emp_dict = {}

    def add_employee(self, employee):
        """
            Taking inputs from user and updating emp_dict dictionary
        :param employee:
        :return: none
        """
        self.emp_dict.update({employee.emp_name: employee})
        print(self.emp_dict)

    def display_employee(self, employee_name):
        print(self.emp_dict.get(employee_name))

    def get_dict(self):
        return {"Company": self.company_name, "Employees": self.emp_dict}


def add_company():
    try:
        company_name = input("Enter company name : ")
        company = Company(company_name)
        company_dict.update({company_name.upper(): company})
        print("Company added successfully")
        print("-----------------------------")
    except Exception as e:
        print("Incorrect company name ", e)


def display_company():
    print("Company")
    print("---------")
    for k in company_dict:
        print(k.upper())
    print("-----------")


def record_employee():

    try:
        company_name = input("Enter company name : ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter employee name :")
            if com_obj.emp_dict.get(emp_name) is None:  # take input here bcoz input enter by user
                emp_rate = int(input("Enter per hour wage :"))
                number_of_days = int(input("Enter total working days in month: "))
                max_hrs = int(input("Enter total working hrs in month: "))
                employee = Employee(emp_name.upper(), emp_rate, number_of_days, max_hrs)
                com_obj.emp_dict.update({employee.employee_name.upper(): employee})
                print("Employee added")
            else:
                print("Employee already exist")

    except Exception as e:
        print("Incorrect company name ", e)


def employee_wage():
    try:
        company_name = input("Enter company name to know wage  : ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            emp_name = input("Enter employee name :")
            emp_obj = com_obj.emp_dict.get(emp_name.upper())

            if emp_obj is not None:
                # print(f"Total Wage : {wage_list[len(wage_list) - 1]}")
                # monthly_wage = emp_obj.calculate_wage()
                monthly_wage = emp_obj.monthly_wage  # ← getting value of monthly wage from constructor
                print(f"\tTotal wage for {emp_obj.emp_name.upper()}:", monthly_wage)
            else:
                print(f"{company_name} has no employee with name {emp_name}")
                print()
        else:
            print(f"There is no company with name {company_name}")
            print()
    except Exception as e:
        print("Please enter correct company name → ", e)


def display_employee():
    try:
        company_name = input("Enter company name to find details: ")
        com_obj = company_dict.get(company_name.upper())
        if com_obj is not None:
            print("NAME\tRATE\tWORKING DAYS\tMAX Hrs.")
            for k, v in com_obj.emp_dict.items():
                print(f"{v.emp_name.upper()}\t\t{v.emp_rate}\t\t{v.number_of_days}\t\t{v.max_hrs}")
        else:
            print("Company does not exist!")
    except Exception as e:
        print("Incorrect Company ", e)


if __name__ == '__main__':
    company_dict = {}
    print("-Welcome to Employee Wage Program -")
    print("\nChoose the operation on the company you want to perform")
    more_choice = True
    while more_choice:
        print("1.Add company\n"
              "2.Display company\n"
              "3.Add employee\n"
              "4.Employee wages\n"
              "5.Display employees\n"
              "0.Exit employee wage system System")

        choice = {1: add_company, 2: display_company,
                  3: record_employee, 4: employee_wage, 5: display_employee}
        print()
        try:
            user_input = int(input("Enter choice: "))
            if user_input != 0:
                choice.get(user_input)()
            elif user_input == 0:
                more_choice = False
                print("Existing Employee wage system ")
                print()
        except Exception as e:
            print("Invalid input")
            print()