import pandas as pd
import psycopg2

# الاتصال بقاعدة البيانات
conn = psycopg2.connect(
    host="localhost",
    database="hospital",
    user="postgres",
    password="2072013"
)

# قراءة البيانات النضيفة
clean_data = pd.read_csv("clean_patients.csv")

# إدخال البيانات
cursor = conn.cursor()

for index, row in clean_data.iterrows():
    cursor.execute("""
        INSERT INTO patients (name, age, phone, diagnosis)
        VALUES (%s, %s, %s, %s)
    """, (row["Name"], row["Age"], row["Phone"], row["Diagnosis"]))

conn.commit()
print("تم تحميل البيانات بنجاح!")