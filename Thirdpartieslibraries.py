#Third party libraries
#Python has a rich ecosystem of third-party libraries.
#You can install them using pip, Python's package manager.
#Here are some popular libraries:

#External modules/packages created by the community to extend Python's functionality.
# - **Installation**: Use `pip` to install libraries, e.g., `pip install library_name`.
# - **Examples**:
#   - **NumPy**: Numerical computations.
#   - **Pandas**: Data manipulation.
#   - **Matplotlib/Seaborn**: Data visualization.
#   - **Requests**: HTTP requests.
#   - **Flask/Django**: Web development.
#   - **BeautifulSoup**: Web scraping.
#   - **TensorFlow/PyTorch**: Machine learning.
# - **Usage**: Import and use in your code, e.g., `import requests`.
# - **Virtual Environments**: Use `venv` to isolate dependencies for projects.
# - **Documentation**: Refer to official docs for installation and usage.

# Example 1: Using the Requests library for HTTP requests
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

# Example 2: Using NumPy for numerical computations
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)
print("Array Mean:", np.mean(array))

# Example 3: Using Pandas for data manipulation
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Example 4: Using Matplotlib for data visualization
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, marker='o')
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()