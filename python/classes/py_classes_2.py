from datetime import datetime


class Person:
    def __init__(self, name, email, dob, gender, fav_team):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = fav_team

    def print_details(self):
        print(self.name)
        print(self.gender)
        print("-----TEAMS-----")
        for team in self.teams:
            print(team)
        print("---------------")
        # 10-09-2001

    def calc_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365, "Years Old")


p1 = Person("Michael", "orina@gmail.com", "04-12-2001", "Male", ["City", "Bayern", "Spurs"])
p1.print_details()
p1.calc_age()
