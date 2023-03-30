#dt={"rno":1,"name":"ajay","qualification":"BE","percentage":90}
#print(type(dt))
#print(dt["rno"])
#print(dt["name"])

student=[{"rno":1,"name":"ajay",},{"rno":2,"name":"vjay"},{"rno":3,"name":"rajesh"},{"rno":4,"name":"sam"}]
print(type(student))
for s in student:
    print(str(s["rno"])+""+s["name"])