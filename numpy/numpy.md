# Chapters :-

- Chapter 1 :- Basic of numpy
- Chapter 2 :- Array Properties and Operations
- Chapter 3 :- Indexing and slicing
- Chapter 4 :- Reshaping and manipulating arrays

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

## Chapter 2:- Array Properties and Operations

- Get shape, size and type of data in array

- Analogy:-
  - You are a warehouse manager and you have to track all products
  - All product has size, quantity, shape and price

### Properties

#### Shape :-

- Help when we use multidimensional data

```python
import numpy as np

arr_2d = np.array([[1,2,3], [4, 5,6]])
print(arr_2d.shape) # (2, 3)
```

#### Size:-

- Total elements in the array

```python
import numpy as np

arr_2d = np.array([[1,2,3], [4, 5,6]])
print(arr_2d.size) # 6
```

#### ndim:-

- Get dimension of the array

```python
import numpy as np

arr_2d = np.array([[1,2,3], [4, 5,6]])
print(arr_2d.ndim) # 2
```

#### dtype:-

- Get data type of elements

```python
import numpy as np

arr_2d = np.array([[1,2,3], [4, 5,6]])
print(arr_2d.dtype) # int64
```

> If there is only one float number between the int numbers the data type show float64. For string number it shows <U21

### Converting data types :-

- Syntax :-
  - array.astype(new_type)
- Example :-
  ```python
  arr_float = arr_2d.astype(float)
  print(arr_float)
  print(arr_float.dtype)
  ```

### Operator in numpy :-

#### Addition:- +

- Example :-

  ```python
  arr = np.array([10, 20, 30])

  print(arr+5)
  ```

> Similarlty for other operator

### Aggregation function :-

- Get summmary from data
- All functions :-

  - np.sum(arr) --- add all
  - np.mean(arr) --- average of array
  - np.min(arr) --- miniumum element
  - np.max(arr) --- maximum element
  - np.std(arr) --- standard equation
  - np.var(arr) --- variance

- Example:-

  ```python
  import numpy as np
  arrray = np.array([10, 20, 30, 40])
  print(np.sum(arrray)) # 100
  print(np.mean(arrray)) # 25.0
  print(np.min(arrray)) # 10
  print(np.max(arrray)) # 40
  print(np.std(arrray))
  print(np.var(arrray))
  ```

## Chapter 3:- Indexing and slicing

- Access any element using index
- Fancy indexing :- Select multiple indexing
- Boolean masking :- Filter elements using certain conditions

### indexing:-

- numpy use zero base indexing
- It has also negative indexing same as python

- syntax:-

  - array[index] -- for 1d array
  - array[row, col] -- for multidimenstional array

- Example:-

  ```python
  arr = np.array([10, 20, 30, 40, 50])

  print(arr[0])
  print(arr[2])
  print(arr[-1])
  ```

### Slicing :-

- Get subarray from array
- syntax :-
  - arr[start: end]
  - end is excluded like range function in python
- Example :-
  ```python
  array = np.array([10, 20, 30, 40, 50, 60, 70])
  print(array[1: 5]) # 2nd index to 4th index
  print(array[:2]) # 0th to 1st index
  print(array[::2]) # every second element
  print(array[::-1]) # reverse
  ```

### Fancy indexing :-

- Selecting multiple elements at once
- syntax :- array[[what to select]]
- Example :-
  ```python
  print(array[[0, 2, 4]])
  ```

### Boolean Masking :-

- Filter what you want
- Syntax :- array[array > 25]
- Example :-
  ```python
  print(array[array > 25])
  ```

## Chapter 4:- Reshaping and manipulating arrays

### reshaping array

- Change shape without modify in data
- syntax:-
  ```
  arr.reshape()
  ```
- Afterr conversion the elements are same
- We can reshape when dimension match only
- reshaping does not create copy. It returns a view.
- It affects original array

### falttening array

- When we want to convert multidimensional array to 1d array.
- ravel() :- Modify original array
- flatten() :- Not affect original array

- Difference between ravel and flatten is ravel Returns a view if possible, else a copy but flatten always returns a copy

  ```python
  import numpy as np

  arr = np.array([10, 20, 22, 40, 50, 60])

  new_arr = arr.reshape(2, 3)
  print(new_arr)



  arr_ravel = new_arr.ravel()
  arr_flat = new_arr.flatten()
  print(arr_ravel)
  print(arr_flat)
  ```

### Manipulate array :-

#### insert :-

- Insert element to array
- syntax :- np.insert(arr_name, inserting_position, inserting_element, axis = 0 or 1)

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.insert(arr, 2, 100, axis=0))
```

- By default axis is 0.
- 0 is for row and 1 is for columnn.
- axis is not mandatory, if there is no axis written by default it is 0.

#### append :-

- Append at last
- New array created. not affect original one
- syntax :- np.append(old_arr, add_element)

```python
app_append = np.append(arr_2d, [10, 20])
print(app_append)
```

#### Concat :-

- Mixed two arrays
- syntax :- np.concatenate((arr1, arr2), axis = 0)
- axis 0 hai to vertical concat hoga aur 1 hai to horizontal. means 0 hai to row add hoga aur 1 hoga to column mai add hoga.
