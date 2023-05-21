import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv("Employee_Salary_Dataset.csv")
df2=pd.read_csv("Department_Dataset.csv")

df=pd.merge(df1,df2)

#group by department
dept_grp=df.groupby("Dept_name")["Salary"].sum()
print(dept_grp)

#count
emp_count=df.groupby("Dept_name")["Salary"].count()
print(emp_count)

#average salary in different departments
mean_of_departments=df.groupby("Dept_name").Salary.mean()

print("Average salary of different departments:")
print(mean_of_departments)

x=['Finance','HR','Tech']
plt.plot(x, mean_of_departments)
plt.show()

