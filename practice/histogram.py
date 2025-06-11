import matplotlib.pyplot as plt

# Sample data
marks = [45, 67, 55, 89, 76, 45, 65, 66, 88, 95, 55, 45, 70, 60, 50]

# Create histogram
plt.hist(marks, bins=5, color='green', edgecolor='black')
plt.title('Student Marks Distribution')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()
