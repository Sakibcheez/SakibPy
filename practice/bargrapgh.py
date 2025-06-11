import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript']
popularity = [40, 30, 20, 10]

# Create bar graph
plt.bar(languages, popularity, color='skyblue')
plt.title('Programming Language Popularity')
plt.xlabel('Languages')
plt.ylabel('Popularity (%)')
plt.show()
