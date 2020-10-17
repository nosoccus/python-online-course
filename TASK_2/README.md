# TASK 2
> This assignment consists of three exercises. They check the knowledge of basic data types and their functions.

- ## [Exercise 1:](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_2/exercise_1.py)
### Requirements:
  * ✔️ Return the count of negative numbers in next list [4, -9, 8, -11, 8].
  * ✔️ Do not use conditionals or loops

> I decided to use ```filter()``` and lambda functions to find the negative values.
Whereas ```filter()``` returns the iterator I converted it to a ```list``` to use ```len()``` function.


- ## [Exercise 2:](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_2/exercise_2.py)
### Requirements:
  * ✔️ Set the first-place player (at the front of the list) to the last place and vice versa.

 ```python
players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka', 'Karolina Pliskova', 'Elina Svitolina']
```

> So in this exercise, we can swap players in the list by indexes, like ```players[0], players[-1] = players[-1], players[0]```


- ## [Exercise 3:](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_2/exercise_3.py)
### Requirements:
  * ✔️ Swap words "reasonable" and "unreasonable" in quote:
```
"The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself."
```
  * ✔️ Do not use <string>.replace() function or similar.

> In the last exercise I used primitive slices and concatenation, seeing I cannot apply any str functions.
