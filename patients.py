import pandas as pd

# قراءة الملف
data = pd.read_csv("patients.csv")

# إيجاد الخانات الفارغة
print("=== خانات فارغة ===")
print(data.isnull().sum())

# إيجاد الأعمار الغير منطقية
print("\n=== أعمار غير منطقية ===")
weird_ages = data[data["Age"] > 120]
print(weird_ages)

# إيجاد الأسماء الناقصة
print("\n=== أسماء قصيرة جداً ===")
short_names = data[data["Name"].str.len() < 5]
print(data["Name"].str.len())
print(short_names)


# البيانات الغلط
bad_data = data[data["Age"] > 120]

# البيانات النضيفة
clean_data = data[(data["Age"] <= 120) & (data["Name"].str.len() >= 5) & (data["Diagnosis"].notnull())]

# حفظهم في ملفات
bad_data.to_csv("quarantine.csv", index=False)
clean_data.to_csv("clean_patients.csv", index=False)



