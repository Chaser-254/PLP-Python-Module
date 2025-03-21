#matplotlib is a library for creating static, animated, and interactive visualizations in Python.
#It can be used to generate plots, histograms, bar charts, scatterplots, and more.
#It is often used in data analysis and visualization tasks.
#To use matplotlib, you need to import it in your Python script or Jupyter notebook.
#The most common way to import matplotlib is as follows:
# import matplotlib.pyplot as plt
#This imports the library and allows you to refer to it as plt in your code.
#You can then use plt to create plots and visualizations.
#Here's an example of creating a simple plot using matplotlib:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, marker='o')
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#color and style
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
