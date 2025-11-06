# 🧮 Sorting Algorithms in Python

A simple and educational project that demonstrates **classic sorting algorithms** —  
including **Bubble Sort**, **Insertion Sort**, and **Selection Sort** — implemented in Python.  

This repository is designed for **learning, benchmarking, and visualizing** how these algorithms work and perform under different conditions.

---

## 🚀 Features

✅ Clean, minimal implementations of 3 core sorting algorithms  
✅ Type-annotated and easy to read  
✅ Ready-to-run Jupyter Notebook for testing and comparison  
✅ Utility functions for timing, testing, and random list generation  
✅ Great for beginners learning algorithm design and time complexity

---

## 📁 Project Structure

sorting-algorithms/ │ ├── bubble_sort.py # BubbleSort

implementation ├── insertion_sort.py # InsertionSort 

implementation ├── selection_sort.py # SelectionSort 

implementation ├── utils.py # Helper utilities (generate data, timer, validator) └── run.ipynb # Jupyter 

notebook to run and compare algorithms


---

## ⚙️ Installation & Setup

You can clone this repository and run it locally using **Python 3.8+**.

```bash
# Clone this repository
git clone https://github.com/yourusername/sorting-algorithms.git
cd sorting-algorithms

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

# Install required packages
pip install jupyter matplotlib
```

Then open the Jupyter notebook:
```
jupyter notebook run.ipynb
```
## 🧩 Algorithms Overview

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Description |
|------------------|------------|---------------|-------------|---------|----------|--------------|
| **Bubble Sort** | O(n²) | O(n²) | O(n²) | O(1) | ✅ Yes | Repeatedly swaps adjacent elements |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ No | Selects the smallest element each pass |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes | Inserts elements into correct position |

## 🧠 Example Usage

You can import and test the sorting functions directly:

```
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

data = [5, 2, 9, 1, 5, 6]

print("Bubble Sort:", bubble_sort(data.copy()))
print("Insertion Sort:", insertion_sort(data.copy()))
print("Selection Sort:", selection_sort(data.copy()))
```
Output:
```
Bubble Sort: [1, 2, 5, 5, 6, 9]
Insertion Sort: [1, 2, 5, 5, 6, 9]
Selection Sort: [1, 2, 5, 5, 6, 9]
```

## 📊 Comparing Performance

Using the notebook run.ipynb, you can generate random lists and compare execution times:
```
from utils import generate_random_list, time_function
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

data = generate_random_list(1000, 0, 10000)

for sort_fn in [bubble_sort, insertion_sort, selection_sort]:
    elapsed, sorted_data = time_function(sort_fn, data.copy())
    print(f"{sort_fn.__name__}: {elapsed:.4f} seconds")
```
Example Output:
```
bubble_sort: 0.4256 seconds
insertion_sort: 0.1382 seconds
selection_sort: 0.2899 seconds
```
(Results vary by system and input size)

## 🧰 Utilities (utils.py)

Typical helper functions include:
```
def generate_random_list(size=10, min_val=0, max_val=100):
    """Generates a random list of integers."""
    ...

def time_function(func, data):
    """Times the execution of a function."""
    ...
```
These help with performance benchmarking and automated testing.


## 🧪 Testing

Each sorting script includes a simple built-in test:
```
if __name__ == "__main__":
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
```
For more comprehensive tests, you can use pytest:
```
pip install pytest
pytest
```

## 📈 Optional Visualization

You can extend this project with Matplotlib to visualize sorting performance.
```
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 2000]
bubble_times, insertion_times, selection_times = [], [], []

for n in sizes:
    data = generate_random_list(n, 0, 10000)
    bubble_times.append(time_function(bubble_sort, data.copy())[0])
    insertion_times.append(time_function(insertion_sort, data.copy())[0])
    selection_times.append(time_function(selection_sort, data.copy())[0])

plt.plot(sizes, bubble_times, label="Bubble Sort")
plt.plot(sizes, insertion_times, label="Insertion Sort")
plt.plot(sizes, selection_times, label="Selection Sort")
plt.xlabel("List Size")
plt.ylabel("Time (s)")
plt.legend()
plt.show()
```

## 🧭 Learning Goals

Understand algorithmic complexity (Big O notation)

Learn how nested loops affect runtime

Practice timing and benchmarking Python functions

Compare performance visually and numerically

## 👨‍💻 Author

Developed with ❤️ by [Maede]

📧 Email: maedekhajekhalili@gmaoil.com

🐙 GitHub: @Maede_81







