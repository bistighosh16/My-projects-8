import matplotlib.pyplot as plt
students = {
    "A": [85, 88, 90, 92, 95],
    "B": [78, 74, 80, 83, 79],
    "C": [90, 85, 88, 92, 89],
    "D": [70, 75, 72, 74, 76],
    "E": [95, 97, 96, 94, 98]
}
marks_list = list(students.values())
student_names = list(students.keys())
plt.figure(figsize=(8, 5))  
plt.boxplot(marks_list, labels=student_names, patch_artist=True)
plt.title("Students' Marks Distribution 📊", fontsize=14)
plt.xlabel("Students", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.grid(axis='y', linestyle="--", alpha=0.7) 
plt.show()
