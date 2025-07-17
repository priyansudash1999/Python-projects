# Chapters :-

- Chapter 1 :- Basic of numpy
- Chapter 2 :- Array Properties and Operations

## Chapter 1 :- Basic of numpy

### When numpy is not there...

- When we handle large amount of dataset in python there python is very slow.

  - Example:- medical data, stock market and many more

  - Analogy:- A scientist need to research on weather data on all over the world then if he use lists for save the temperature then the list willm be very vast.

  ```python
  temperatures = [32.3, 21.8, 12.0, 21.3]
  totaL_temp = 0
  for i in temperatures:
    total_temp += i

  avg_temp = total_temp // len(tempertures)
  # if there are millions of temperture then for loop will be very slow and time consuming. so here numpy comes into picture.
  ```

### History of numpy:-

- Travis Oliphant created library numpy for handling large dataset using arrays on 2005.
- It introduces special arrays which is superfast
- Ex:-

  ```python
  import numpy as np
  temperatures = np.array([32.3, 21.8, 12.0, 21.3])
  avg = np.mean(temperatures)
  print(avg)
  ```

- Numpy advantages:-

  - speed
  - less memory
  - Easy math operation
  - Used in AI field, data science and data analytics

- Numpy uses:-

  - Data science
  - Machine learning and AI
  - Stock market and finance
  - Medical research
  - Image processing

- Why numpy is better than python list ?

  - Python list is slower than numpy arrays
  - Python list used higher memory than numpy arrays
  - Python list loops for calculation but numpy does not need loops

  > For small data python list is better.

### Creation of array using numpy:-

- np.array() — Create arrays from Python lists or tuples.

  ```python
    import numpy as np
    arr = np.array([1,2,3])
    arr2d = np.array([[1,2,3], [4, 5, 6]])
    print(arr)
  ```

- np.arange() — Generate arrays with regularly spaced values (like Python's range).

  - Syntax :- np.arange(start, end, step)
  - Example :-

  ```python
    odd_arr = np.arange(1, 10, 1)
    print(odd_arr)

    # array in sequence
    seq_arr = np.arange(10)
    print(seq_arr) # [1 2 3 4 5 6 7 8 9 10]
  ```

- np.linspace() — Create arrays with a specified number of evenly spaced values over a range.

  - Example:-

  ```python
  import numpy as np

  # Create 5 evenly spaced numbers between 0 and 1 (inclusive)
  arr1 = np.linspace(0, 1, 5)
  print(arr1)  # Output: [0.   0.25 0.5  0.75 1.  ]

  # Create 4 points between 10 and 20 (inclusive)
  arr2 = np.linspace(10, 20, 4)
  print(arr2)  # Output: [10.  13.33333333 16.66666667 20. ]

  # Return both the values and the step size
  arr3, step = np.linspace(0, 1, 5, retstep=True)
  print(arr3)   # Output: [0.   0.25 0.5  0.75 1.  ]
  print(step)   # Output: 0.25

  # Specify that endpoint is not included
  arr4 = np.linspace(0, 1, 5, endpoint=False)
  print(arr4)   # Output: [0.  0.2 0.4 0.6 0.8]

  ```

- np.zeros() — Create arrays filled with zeros.

  - Syntax = arr.zeros(shape=3)
  - Example:-

  ```python
  arr2 = np.zeros(shape=3)
  print(arr2)
  ```

- np.ones() — Create arrays filled with ones.

  - Syntax :- arr.ones(shape=3)
  - Example:-

  ```python
  arr2 = np.ones(shape=3)
  print(arr2)
  ```

- np.eye() — Generate identity matrices.

  - Syntax:- np.eye(size)
  - Example:-

  ```python
  arr2 = np.eyes(3)
  print(arr2) # [[1 1 1] [1 1 1] [1 1 1]]
  ```

- np.random.rand(), np.random.randint() — Create arrays with random values.

  - Syntax:- np.random.rand(2)

  ```python
  arr_rand = np.random.rand(2)
  print(arr_rand) # [0.58654528 0.3001118 ]
  ```

  - Syntax:- np.random.randint(low, high, size)

  ```python
  arr_rand = np.random.randint(0, 10, size=(2, 4))
  print(arr_rand) # [[4, 7, 2, 9], [5, 1, 3, 8]]
  ```
