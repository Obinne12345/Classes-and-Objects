class Student:

 def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

#method for changing object name
 def change_name(self, new_name):
        self.name = new_name
        return

#method for changing object age as integer
 def change_age(self, new_age):
        new_age= int(new_age)
        self.age = new_age
        return

#method for adding new track to object
 def add_track (self, new_track):
        self.tracks = self.tracks.append(new_track)

#method for changing object score
 def change_score(self, new_score):
        self.score = new_score
        return

#method for getting object score
 def get_score (self):
        print (self.score)

#Creating an object "Betty" with the class "Student"
Betty = Student(name="Betty", age=22, tracks=["Fullstack","Blockchain"], score=29.5)



Betty.change_name("Stella")
print(Betty.name)



Betty.change_age(25)
print (Betty.age)



Betty.change_score(76.3)
Betty.get_score()



Betty.add_track("UI/UX")