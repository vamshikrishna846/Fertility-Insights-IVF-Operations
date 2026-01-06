# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 12:41:32 2025

@author: vamshi krishna
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
appointments = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_appointments.csv");
equipment = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_equipment.csv")
costs = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_operational_costs.csv")
wait_times = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_patient_wait_times.csv")
kpis = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_performance_kpis.csv")
rooms = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_room_utilization.csv")
staff = pd.read_csv(r"C:\Users\vamshi krishna\OneDrive\Documents\PDF X\fertlity project\project data set\ivf_staff.csv")

appointments.info()
equipment.info()
costs.info()
kpis.info()
#missing values of file
appointments.isnull().sum()
equipment.isnull().sum()
costs.isnull().sum()
wait_times.isnull().sum()
#finding mssing values and getting replaced
appointments.fillna(appointments.mean(numeric_only=True), inplace=True)
equipment.fillna(equipment.mean(numeric_only=True), inplace=True)
costs.fillna(costs.mean(numeric_only=True), inplace=True)
wait_times.fillna(wait_times.mean(numeric_only=True), inplace=True)
kpis.fillna(kpis.mean(numeric_only=True), inplace=True)
rooms.fillna(rooms.mean(numeric_only=True), inplace=True)
staff.fillna(staff.mean(numeric_only=True), inplace=True)

#removing dupilcates from files
appointments.drop_duplicates(inplace=True)
equipment.drop_duplicates(inplace=True)
costs.drop_duplicates(inplace=True)
wait_times.drop_duplicates(inplace=True)
kpis.drop_duplicates(inplace=True)
rooms.drop_duplicates(inplace=True)
staff.drop_duplicates(inplace=True)

mean_wait = wait_times["wait_time_minutes"].mean()
median_wait = wait_times["wait_time_minutes"].median()
mode_wait = wait_times["wait_time_minutes"].mode()[0]

print("Mean:", mean_wait)
print("Median:", median_wait)
print("Mode:", mode_wait)
#histogram
plt.hist(wait_times["wait_time_minutes"])
plt.xlabel("Wait Time (Minutes)")
plt.ylabel("Frequency")
plt.title("Distribution of Patient Wait Times")
plt.show()
#kpi distribution
kpis.hist(figsize=(10,8))
plt.show()
#box plot
plt.boxplot(wait_times["wait_time_minutes"])
plt.title("Outliers in Patient Wait Time")
plt.show()
#bivaraint analysis
sns.scatterplot(
    x=appointments["appointment_id"],
    y=wait_times["wait_time_minutes"]
)
plt.title("Appointments vs Patient Wait Time")
plt.show()
#staff id vs wait time
sns.scatterplot(
    x=staff["staff_id"],
    y=wait_times["wait_time_minutes"]
)
plt.title("Staff Availability vs Patient Wait Time")
plt.show()
#coorelation error
merged = pd.concat([
    appointments.select_dtypes(include=np.number),
    wait_times.select_dtypes(include=np.number),
    staff.select_dtypes(include=np.number)
], axis=1)
sns.heatmap(merged.corr(), annot=True)
plt.title("Correlation Heatmap – IVF Operations")
plt.show()
