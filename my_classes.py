#Source tutorial: https://youtu.be/apACNr7DC_s

class User:
    pass

user1 = User()
user1.first_name= "Bob"
user1.last_name = "Smith"

print(user1.first_name)
print(user1.last_name)

user1.age = 38

##############

import datetime

#method
#init
#help text
class User:
    #pass
    """
    what the fuck
    """
    def __init__(self, full_name, bday):
        self.name = full_name
        self.birthday = bday  ##yyyymmdd
        
        #extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1] #used index -1 to get last name

    def age(self):
        """get the age of user"""
        today = datetime.datetime.now()
        
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        
        delta_days = (today.date() - dob).days
        delta_years = delta_days/365
        return(delta_years)
#        
user = User("Bob Smith", "19881212")
user.age()

user.thought = 12
