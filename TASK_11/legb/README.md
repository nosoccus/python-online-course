### Requirements:
  * Find a way to call ```inner_function``` without moving it from inside of ```enclosed_function```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb1.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main1.py). Fistly, I modified ```enclosed_function``` to return the ```inner_function()```. Then, I created new python script and imported the ```enclosed_function``` from ```legb.py```.

  * Modify ONE LINE in ```inner_function``` to make it print variable ```'a'``` from ```global scope```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb2_1.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main2_1.py) to call variable from ```global scope``` I added ```global``` keyword.

  * Modify ONE LINE in ```inner_function``` to make it print variable ```'a'``` from ```enclosing function```.
    > Solution: [legb.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/legb2_2.py), [main.py](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11/legb/main2_2.py) to call variable from ```enclosing_function``` I added ```global``` keyword.

### [Back to TASK_11](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_11)
