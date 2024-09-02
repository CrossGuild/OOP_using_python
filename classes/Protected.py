class Employee:
    _company_name = "M Inc"

    def m_attendance(self):
        print("attendance for {}.".format(self._company_name))

    @staticmethod
    def stsurvey(name, age):
        if age > 30:
            print("{} is fired.".format(name))
        else:
            print("{} is not fired yet.".format(name))

class Administrator:
    # コンストラクタ
    # 基本宣言のコンストラクタ
    def __init__(self, _admin_name = "Sandworm"):
        self._admin_name = _admin_name

    def print_admin(self):
        print(self._admin_name)

#シングルインヘリタンス
#マルチインヘリタンス
class Programmer(Employee, Administrator): # Child Class (Parent Class)
    def __init__(self, bonus_percentage, _admin_name):
        self.bonus_percentage = bonus_percentage
        self._admin_name = _admin_name

    def calculate_bonuses(self):
        print("Bonus cal done - Bonus : {}, company name : {}".format(self.bonus_percentage, self._company_name))
        print(self._admin_name)

# マルチレベルインヘリタンス
class JuniorProgrammer(Programmer):
    def __init__(self, bonus_percentage, _admin_name):
        self.bonus_percentage = bonus_percentage
        self._admin_name = _admin_name

    def print_jr_programmer(self):
        print("Bonus cal done - Bonus : {}, company name : {}".format(self.bonus_percentage, self._company_name))


if __name__ == "__main__":
    Jr = JuniorProgrammer(211, "Nickson")
    Jr.m_attendance()
    Jr.stsurvey("<Kumazo>", 21)
    Jr.calculate_bonuses()
    Jr.print_jr_programmer()


