import pandas as pd
import smtplib
import os
from dotenv import load_dotenv


# I will be implementing the student report emailer between teachers and studentss
load_dotenv()

DATA_PATH =  "./data/students.csv"
data = pd.read_csv(DATA_PATH)

# Get data from the env file
teacher_email = os.getenv(key="TEACHER_EMAIl")
password = os.getenv(key="PASSWORD")

# print(teacher_email)
# m =  data.name.to_list()
# print(m)
get_data = {(info["name"],info.email):(info.math, info.science, info.english ) for (index,info)  in data.iterrows()}



print(get_data)