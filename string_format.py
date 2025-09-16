# # a= "Good night, Priya. Have a good bad night!"

# user_input = input("what is your name?")
# a = "Good night, {}. Have a Good Bad nigh t.{} Have you done your homework?".format(user_input, user)
# print(a)


age = 25
fname= "Pabitra"
mname= "Kumar"
lname= "Biswas"
#long Process
txt= "Hi, i am {fname} {mname} {lname}. I am {age} years old.".format(mname=mname, fname=fname, lname=lname, age=age)

#short technique
txt2= f"Hello, {fname} {mname} {lname}. i am {age}. have a Good bad night"
print(txt)
print(txt2)