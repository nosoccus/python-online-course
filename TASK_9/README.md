# TASK 9
> This assignment consists of five exercises. They check the knowledge of operations with strings and strings methods.

## [Exercise 1](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_9/quotes.py):
### Requirements:
  * Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.  


## [Exercise 2](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_9/palindrome.py):
  ### Requirements:
  * Write a function that check whether a string is a palindrome or not.
  * To check your implementation you can use strings from [here] (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)   

## [Exercise 3](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_9/shortest.py):
  ### Requirements:
  * Implement a function `get_shortest_word(s: str) -> str` which returns the shortest word in a given string.
  * The word can contain any symbols except whitespaces (` `, `\n`, `\t` and so on).
  * If there are multiple shortest words in the string with a same length return the word that occurs first.
  * Usage of any split functions is forbidden.

  **Example:**  
  ```python
  >>> get_shortest_word('Python is simple and effective!')
  'is'
  >>> get_shortest_word('Any pythonista like namespaces a lot, a? O')
  'a'
  ```  

## [Exercise 4](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_9/bunch.py):
  ### Implement a brunch of functions which receive a changeable number of strings and return next parameters:
  * characters that appear in all strings;
  * characters that appear in at least one string;
  * characters that appear at least in two strings;  
  * characters of alphabet, that were not used in any string;
    * Note: use `string.ascii_lowercase` for list of alphabet letters.

  **Example:**  
  ```python
  test_strings = ["hello", "world", "python"]
  print(test_1_1(*test_strings))
  >>> {​​​​​​​​'o'}​​​​​​​​
  print(test_1_2(*test_strings))
  >>> {​​​​​​​​'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}​​​​​​​​
  print(test_1_3(*test_strings))
  >>> {​​​​​​​​'h', 'l', 'o'}​​​​​​​​
  print(test_1_4(*test_strings))
  >>> {​​​​​​​​'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}​​​​​​​​
  ```


## [Exercise 5](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_9/count_letters.py):
  ### Requirements:
  * Implement a function, that takes string as an argument and returns a dictionary.
  * Dictionary should containsd  letters of given string as keys and number of their occurrence as values.

  **Example:**  
  ```python
  print(count_letters("stringsample"))
  >>> {​​​​​​​​'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1,
       'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}​​​​​​​​
  ```
