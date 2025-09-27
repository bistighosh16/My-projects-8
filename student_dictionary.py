import matplotlib.pyplot as plt
students = {
    "A": [85, 90, 78],
    "B": [88, 76, 92],
    "C": [90, 85, 87],
    "D": [70, 75, 80],
    "E": [95, 98, 99]
}
student_names = list(students.keys())  
average_marks = [sum(marks) / len(marks) for marks in students.values()] 
plt.figure(figsize=(8, 5))  
plt.bar(student_names, average_marks, color='skyblue')  
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks Chart")
plt.xticks(rotation=30)  
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.show()
