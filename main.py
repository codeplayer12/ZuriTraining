class Student:
    # [assignment] Skeleton class. Add your code here
	def __init__(self,name="Jena",age=int(25),tracks=['JN','PT'],score=26.9):
		self.name = name
		self.age = age
		self.tracks = tracks
		self.score = score
	
	def __repr__(self):
		return f'Name: {self.name}\n Age: {self.age}\n Tracks: {self.tracks}\n Score: {self.score}'
 
	def change_name(self,name):
		self.name = name
		return self.name

	def change_age(self,age):
		if type(int(age)) == int and int(age)>0:
			self.age =age
			return age
		else:
			return self.age


	def add_track(self,track):
		new = self.tracks
		new.append(track)
		return new

	def get_score(self):
		return self.score

	


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age('-34')
Bob.add_track("UI/UX")
Bob.get_score()
