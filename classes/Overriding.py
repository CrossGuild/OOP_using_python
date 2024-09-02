class Employee:
    company_name = "Mark Inc"

    def mark_attendance(self):
        print("attendance for {}.".format(self.company_name))

class Programmer(Employee):
    def __init__(self, bonus_percentage):
        self.bonus_percentage = bonus_percentage

    def cal_bonus(self):
        print("Bonus cal done - Bonus : {}, Company name : {}".format(self.bonus_percentage, self.company_name))

    # Override
    def mark_attendance(self):
        print("M attendance for Programmer")
        super().mark_attendance()

if __name__ == '__main__':
    j_programmer = Programmer(10)
    j_programmer.mark_attendance()