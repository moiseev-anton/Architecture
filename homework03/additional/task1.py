# Переписать код в соответствии с Single Responsibility Principle:

class Employee:
    def init(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

# выносим метод calculateNetSalary() в отдельный класс
class SalaryCalculator:
    @staticmethod
    def calculate_net_salary(employee):
        tax = int(employee.base_salary * 0.25)
        return employee.base_salary - tax
