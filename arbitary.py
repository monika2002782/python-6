#arbitrary(*,**)
def myfunction(*kids):
  print(kids[0])
myfunction("emil","bijorn","linus")


def my_function(**kid):
  print("his last name is"+kid["fname"]+kid["lname"])
my_function(fname="harish",lname="bijorn")

#workout
def my_function(country="norway"):
  print("I am from"+country)
my_function("sweden")
my_function()
my_function("india")


###sample arbitary
def my_function(fname):
  print(fname+"welcome")
  my_function("hii")
  my_function("bye")



