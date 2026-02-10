import pandas as pd
import smtplib
import os
import statistics
from dotenv import load_dotenv


# I will be implementing the student report emailer between teachers and studentss
load_dotenv()

HOST = "smpt.gmail.com"
PORT = 587
DATA_PATH =  "./data/students.csv"
data = pd.read_csv(DATA_PATH)

# Get data from the env file
teacher_email = os.getenv(key="TEACHER_EMAIl")
password = os.getenv(key="PASSWORD")

# print(teacher_email)
# m =  data.name.to_list()
# print(m)
get_data = {(info["name"],info.email):(info.math, info.science, info.english ) for (index,info)  in data.iterrows()}

# loop through that and get average

for student, marks in get_data.items():
    name, email =student
    # math, science, english = marks
    average = float(f"{statistics.mean(marks):.2f}")

    txt = None
    grade = None
    if average > 70:
        txt = "./emails/a_student.txt"
        grade = "A"

    elif average > 50:
        txt = "./emails/b_student.txt"
        grade = "B"
    else:
        txt = "./emails/c_student.txt"
        grade = "C"


    # now send the email :

    with open(txt, mode="r") as file:
        file = file.readlines()

        standard = []

        for line in file:
            line = line.replace("[Name]",name).replace("[Score]", str(average)).replace("[grade]", grade)
            standard.append(line)

    
    with smtplib.SMTP(host=HOST, port=PORT) as connection:
        connection.starttls()
        connection.login(user=, password)

    
    

# print(get_data)