'''
student.csv
1,Dipesh,18,123456,12,70
2,Ayush,18,8765314,13,80
3,Jeenal,19,546465,11,70
4,Harshita,20,897954,16,70
5,Hinal,19,32654,17,95
'''





# make a students marks table pie chart
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time,student_name,age,contact,study_hour,marks


#reading data from a cvs file
df=pd.read_csv('student.csv')
df.info()

df.student_name

# store data in perticular variables
student_name = df.student_name
marks=df.marks
age=df.age
study_hours = df.study_hour
contact = df.contact

# pie chart between students marks 
exp=[0,0,0,0,0.1]
plt.pie(marks,labels=student_name,explode=exp,shadow=True,autopct='%1.1f%%')
plt.grid(color='green')
plt.show()

# pie chart between students age
exp=[0,0,0,0.2,0.1]
plt.pie(age,labels=student_name,explode=exp,shadow=True,autopct='%1.1f%%')
plt.grid(color='green')
plt.show()

# pie chart between students study hours
exp=[0,0,0,0,0.1]
plt.pie(study_hours,labels=student_name,explode=exp,shadow=True,autopct='%1.1f%%')
plt.grid(color='green')
plt.show()
