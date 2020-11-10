### Exercise 4:
* Run the module ```[modules/mod_a.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/modules/mod_a.py)```.
  * Firstly, we ```import mod_c``` module that contains assignment of ```x=5``` variable.
  * Secondly, we ```import mod_b```module that contains the redefiniton of x variable, but value will be the same.
  * So, when we ```print(mod_c.x)``` we will get the value from ```mod_b```.

  **Input will be like**:
  ```python
  5
  ```

* Try to change ```x``` to a list ```[1,2,3]```.
  * So lets change ```x``` in ```mod_c``` and check if I correct in previous task.
  * Again run the ```mod_a``` module.
  * Value of ```x``` will be from ```mod_b```.

  **Input will be like**:
  ```python
  5
  ```

* Try to change ```import``` to ```from x import *``` where ```x``` - module names.
  * The statement ```from x import *``` have the same effect as ```import x```.
  * So there is no a any changes in my opinion.

  **Input will be like**:
  ```python
  5
  ```
