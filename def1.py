class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"name - {self.name} and age - {self.age}.")

p1=person("steve",316)
p1.greet()
