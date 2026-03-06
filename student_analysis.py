import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("students.csv")
except FileNotFoundError:
    print("Error: students.csv file not found!")
    exit()

df['Total'] = df['Subject1'] + df['Subject2'] + df['Subject3']
df['Percentage'] = df['Total'] / 3

def calculate_grade(percent):
    if percent >= 75:
         return 'A'
    elif percent >= 60:
        return 'B'
    elif percent >= 40:
        return 'C'
    else:
        return 'F'

df['Grade'] = df['Percentage'].apply(calculate_grade)

print("===== Student Marks Data =====")
print(df)

plt.figure(figsize=(8,5))
sns.barplot(x='Name', y='Total', data=df, palette='viridis')
plt.title("Total Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.tight_layout()
plt.show()

grade_counts = df['Grade'].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(x=grade_counts.index, y=grade_counts.values, palette='pastel')
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.show()
