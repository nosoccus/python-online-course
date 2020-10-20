# TASK 3
> This assignment consists of three exercises. They check the knowledge of conditionals.

👍 All exercises are done and checked for PEP-8.

- ## [Exercise 1:](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_3/point.py)
### Requirements:
  * ✔️ Write the program that determines whether Point A(x, y) is in the shaded area or not.

![alt-text](TASK_3/plot.png "Shaded area")


> In this exercise is only needed to write conditionals for ```x``` and ```y``` parameters, where ```-1 <= x <= 1``` and ```0 <= y <= 1```


- ## Exercise 2 - "FizzBuzz": [First Version](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_3/fizzbuzz1.py) / [Second Version](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_3/fizzbuzz2.py)
### Requirements:
  * ✔️ Write a program that prints the input number from 1 to 100. But for a multiple of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


 > In this task I decided to use string concatenation to avoid one excessive ```if``` statement for ```"FizzBuzz"```. Also, I made a second version of the task with ```ternary operators``` to reduce the number of strings.

- ## [Exercise 3 - "Baccarat":](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_3/baccarat1.py)
### Requirements:
  * ✔️ Simulate the one round of play for the baccarat game:
  * ✔️ Rules:
   * Cards have a point value:
       * The 2 through 9 cards in each suit are worth face value (in points).
       * The 10, Jack, Queen, and King have no point value (i.e. are worth zero).
       * Aces are worth 1 point.
   * Sum the values of cards. If the total is more than 9 reduce 10 from the result. E.g. 5 + 9 = 14, 14 - 10 = 4, 4 is the result.
   * The player is not allowed to play other cards like the Joker.


> In the first version of this exercise I used the provided skeleton. I created the list of values of each card and check the value of the card by index.
