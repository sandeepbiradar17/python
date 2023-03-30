import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
student={"rno":[1,2,3,4,5,6]}
studentsubjects={"english" :[90,34,35,67,34,50],
                  "maths" :[23,45,29,45,34,65],
                  "science" :[78,34,26,67,34,50]}

#df=pd.DataFrame(studentsubjects, index=student["rno"])


# Plot the data
#df.plot(kind="bar")

# Add labels and title
# plt.xlabel("rno")
# plt.ylabel("Marks")
# plt.title("Subject Scores for Each Student")

# print(number[student])
# print(number[studentsubjects])
# plt.show()


# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt

# # Define the student data and subject scores
# student = {"rno": [1,2,3,4,5,6,7]}
# studentsubjects = {"english": [90,34,35,67,34,50],
#                    "maths": [23,45,29,45,34,65],
#                    "science": [78,34,26,67,34,50]}

# # Create a DataFrame from the data

df = pd.DataFrame(studentsubjects, index=student["rno"])

# Plot the data
df.plot(kind="bar")

# Add labels and title
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Subject Scores for Each Student")

# Display the graph
plt.show()
print(student)
print(studentsubjects)
