import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Python)

# Plot
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Programming Language Popularity')
plt.axis('equal')  # Equal aspect ratio ensures the pie is a circle
plt.show()


