# TASK 10
> This assignment consists of four exercises. They check the knowledge of modules and decorators.

## [Exercise 1](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb):
### Requirements:
  * Find a way to call ```inner_function``` without moving it from inside of ```enclosed_function```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb1.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main1.py). Fistly, I modified ```enclosed_function``` to return the ```inner_function()```. Then, I created new python script and imported the ```enclosed_function``` from ```legb.py```.

  * Modify ONE LINE in ```inner_function``` to make it print variable ```'a'``` from ```global scope```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb2_1.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main2_1.py) to call variable from ```global scope``` I added ```global``` keyword.

  * Modify ONE LINE in ```inner_function``` to make it print variable ```'a'``` from ```enclosing function```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb2_2.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main2_2.py) to call variable from ```enclosing_function``` I added ```global``` keyword.

> The condition is inaccurate in this exercise, so there are many ways to interpret and solve it.

## [Exercise 2](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/remember_last.py):
  ### Requirements:
  * Implement a decorator ```remember_result``` which remembers last result of function it decorates and prints it before next call.

  **Example of code:**  
  ```python
  @remember_result
  def sum_list(*args):
    result = ""
    for item in args:
      result += str(item)
    print(f"Current result = '{result}'")
    return result
  ```

  **Example of execution:**
  ```python
  sum_list("a", "b")
  >>> "Last result = 'None'"
  >>> "Current result = 'ab'"
  sum_list("abc", "cde")
  >>> "Last result = 'ab'"
  >>> "Current result = 'abccde'"
  sum_list(3, 4, 5)
  >>> "Last result = 'abccde'"
  >>> "Current result = '345'"
  ```



## [Exercise 3](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/call_once.py):
  ### Requirements:
  * Implement a decorator ```call_once``` which runs a function or method once and caches the result.
  * All consecutive calls to this function should return cached result no matter the arguments.

  **Example of code:**  
  ```python
  @call_once
  def sum_of_numbers(a, b):
    return a + b
  ```  

  **Example of execution:**
  ```python
  print(sum_of_numbers(13, 42))
  >>> 55
  print(sum_of_numbers(999, 100))
  >>> 55
  print(sum_of_numbers(134, 412))
  >>> 55
  print(sum_of_numbers(856, 232))
  >>> 55
  ```



## [Exercise 4](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/modules):
  ### Implement a brunch of functions which receive a changeable number of strings and return next parameters:
  * Run the module ```[modules/mod_a.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/modules/mod_a.py)```. Check its result. Explain why does this happen.
  * Try to change ```x``` to a list ```[1,2,3]```. Explain the result.
  * Try to change ```import``` to ```from x import *``` where ```x``` - module names. Explain the result.
