# TASK 10
> This assignment consists of three exercises. They check the knowledge of operations with files.

## [Exercise 1](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_10/sort.py):
### Requirements:
  * Open file `data/unsorted_names.txt` in data folder.
  * Sort the names and write them to a new file called `sorted_names.txt`.
  * Each name should start with a new line as in the following example:

  **Example:**  
  ```
  Adele
  Adrienne
  ...
  Willodean
  Xavier
  ```  



## [Exercise 2](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_10/common.py):
  ### Requirements:
  * Implement a function which search for most common words in the file.
  * Use `data/lorem_ipsum.txt` file as an example.
  * NOTE: Remember about dots, commas, capital letters etc

  **Example:**  
  ```python
  def most_common_words(filepath, number_of_words=3):
    pass
  print(most_common_words('lorem_ipsum.txt'))
  >>> ['donec', 'etiam', 'aliquam']
  ```



## [Exercise 3](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_10/students.py):

File `data/students.csv` stores information about students in CSV](https://en.wikipedia.org/wiki/Comma separated_values) format. This file contains the student’s names, age and average mark.
  ### Requirements:
  *  Implement a function which receives file path and returns names of top performer students.

    **Example:**
  ```python
  def get_top_performers(file_path, number_of_top_students=5):
    pass
  print(get_top_performers("students.csv"))
  >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
  ```

  * Implement a function which receives the file path with students info and writes CSV student information to the new file in descending order of age.

  **Example:**  
  ```
  student name,age,average mark
  Verdell Crawford,30,8.86
  Brenda Silva,30,7.53
  ...
  Lindsey Cummings,18,6.88
  Raymond Soileau,18,7.27
  ```  
