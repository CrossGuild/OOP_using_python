class Employee:
    __company_name = "M Inc"

    def m_attendance(self):
        print("attendance for {}.".format(self.__company_name))

    @staticmethod
    def stsurvey(name, age):
        if age > 30:
            print("{} is fired.".format(name))
        else:
            print("{} is not fired yet.".format(name))

class Administrator:
    # コンストラクタ
    # 基本宣言のコンストラクタ
    def __init__(self, __admin_name = "Sandworm"):
        self.__admin_name = __admin_name

    def print_admin(self):
        print(self.__admin_name)

#シングルインヘリタンス
#マルチインヘリタンス
class Programmer(Employee, Administrator): # Child Class (Parent Class)
    def __init__(self, bonus_percentage, __admin_name):
        self.bonus_percentage = bonus_percentage
        self.__admin_name = __admin_name

    def calculate_bonuses(self):
        print("Bonus cal done - Bonus : {}, company name : {}".format(self.bonus_percentage, self.__company_name))
        print(self.__admin_name)

# マルチレベルインヘリタンス
class JuniorProgrammer(Programmer):
    def __init__(self, bonus_percentage, __admin_name):
        self.bonus_percentage = bonus_percentage
        self.__admin_name = __admin_name

    def print_jr_programmer(self):
        print("Bonus cal done - Bonus : {}, company name : {}".format(self.bonus_percentage, self.__company_name))


if __name__ == "__main__":
    Jr = JuniorProgrammer(211, "Nickson")
    Jr.m_attendance()
    Jr.stsurvey("<Kumazo>", 21)
    Jr.calculate_bonuses()
    Jr.print_jr_programmer()


