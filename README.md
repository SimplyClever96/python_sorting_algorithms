# Python Sorting Algorithms

A collection of classic sorting algorithms implemented in Python.  
This repository provides clean, well‑structured, and easy‑to‑understand implementations of fundamental sorting techniques.  
It is designed for learning, teaching, benchmarking, and integration into other Python projects.

---

## 🚀 Included Algorithms (initial release)

### **Bubble Sort**
A simple comparison‑based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if needed.  
Great for educational purposes and understanding the basics of sorting logic.

### **Quick Sort**
A highly efficient divide‑and‑conquer algorithm.  
Uses partitioning to recursively sort sub‑arrays and offers excellent average‑case performance.

### **Merge Sort**
A stable and predictable O(n log n) algorithm.  
Splits the list into halves, recursively sorts them, and merges the results into a fully sorted list.

---

## 📦 Project Goals

- Provide clear and readable reference implementations  
- Offer a modular structure so each algorithm can be imported independently  
- Serve as a foundation for further algorithms, visualizations, or performance benchmarks  
- Support students, educators, and developers exploring algorithmic fundamentals  

---

## 📁 Project Structure

sorting-algorithms/
- __init__.py
- sort.py
- README.md
- LICENSE

---

## 🧪 Usage Example

```python
from sorting_algorithms import bubble_sort, quick_sort, merge_sort

data = [5, 2, 9, 1, 5, 6]

print(bubble_sort(data.copy()))
print(quick_sort(data.copy()))
print(merge_sort(data.copy()))
```

--- 
📜 License
This project is licensed under the MIT License, allowing free use, modification, and distribution while requiring attribution to the original author.

---
🤝 Contributing
Contributions are welcome.
Feel free to open issues, submit pull requests, or suggest new algorithms to include in future versions.

⭐ Future Additions
tbd

---
Happy coding!
