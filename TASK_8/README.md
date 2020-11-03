# TASK 8
> This assignment consists of six exercises. They check the knowledge of errors and exceptions. Also, there is no demand to write code, because all exercises compiled in your own head. This task is really important because it checks your intuition and experience.

## Exercise 1:
![alt-text](TASK_8/ex1.png "Exercise 1")

This simple code snippet program requires _input_ from a user, so there are _several scenarios_:
  * If the user enters a number that less or equal ```b```, the program will raise ```AssertionError 'Not enough'```.
  * If the user enters a number that more than ```b```, nothing will happen, the program will just be ended.
  * If the user enters something that cannot be converted to ```int```, the program will raise ```ValueError```


## Exercise 2:
![alt-text](TASK_8/ex2.png "Exercise 2")
  * ✔️ If we run this code snippet the program will raise ```NameError``` because there is no ```bar()``` function declaration.
  * ❓ But _IMAGINE IF_ there was correctly declared ```bar()``` function that return some value. Then program would execute only finally block and then ```foo()``` function block. So output would be like:

   ```python
   after bar
   or this after bar?
   ```


## Exercise 3:
![alt-text](TASK_8/ex3.png "Exercise 3")

This exercise is similar to previous, because uses the same ```try: ... finally:``` block. The return value of the function is determined by the last ```return``` value. The return value of the function and accordingly the program output will be ```2```. Since the ```finally``` clause always executes, the return statement in the ```finally``` clause will always be the last one executed.


## Exercise 4:
![alt-text](TASK_8/ex4.png "Exercise 4")

  * ✔️ The program will raise ```SyntaxError``` since ```else``` block in ```try``` construction uses only if there is ```except``` block and places only before ```finally``` block.
  * ❓ But _IMAGINE IF_ there was bare ```except``` and ```block``` was before ```finally```, the program would execute ```try``` and ```finally``` blocks. So output would be like:

    ```python
    1
    2
    ```


## Exercise 5:
![alt-text](TASK_8/ex5.png "Exercise 5")
  * ✔️ The program will raise two ```TypeError```:
    * The first because of ```raise "Error"``` line. Exceptions must derive from ```BaseException```.
    * The second because of ```except "Error"```. Exceptions classes must inherit from ```BaseException```.
  * We can fix it by creation of two classes. So code would be like:

    ```python
    class Error(Exception):
    """Base class for other exceptions"""
    pass


    class BadComparsion(Error):
        pass


    try:
        if '1' != 1:
            raise BadComparsion
        else:
            print("Error has not occured")
    except BadComparsion:
        print("Error has occured")

    Output:
    >>> Error has occured.
    ```


## Exercise 6:
![alt-text](TASK_8/ex6.png "Exercise 6")

This is another one and the last that requires user input. By the way, code has ```bare except``` that is *not* recommended and infinite loop.
  * If user enters invalid filename, the program will print ```print("Input file not found")``` and it will continue to ask input.
  * If user enters valid filename, the program will open this file for reading and it will continue to ask input.
  * Note: probably, there is no exit out of the program 😕
