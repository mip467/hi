class Student:
	def __init__(self, age, gender, subjects):
		self.studentAge = age
		self.studentGender = gender 
		self.studentSubs = subjects


	def birthday(self):
		self.studentAge = self.studentAge + 1
		print self.studentAge

	def study(self):
		for i in self.studentSubs:
			print i

bob = Student(10, "male", ["English", "Geograghy", "Physics"])

bob.birthday()
bob.study()	