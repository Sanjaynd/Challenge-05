# challenge-03
class student:

    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setrollnumber(self,rollnumber):
        self.rollnumber=rollnumber
    def getrollnumber(self):
        return self.rollnumber
s1=student()
s1.setname("sanjay")
s1.setrollnumber("1RR18ME044")
name=s1.getname()
rollnumber=s1.getrollnumber()
print(name)
print(rollnumber)