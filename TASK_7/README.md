# TASK 7
> This assignment consists of two exercises. They check the knowledge of classes.

Not a perfect task 😥. OOP is not my best power

- ## [Task 1 - Rectangle](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_7/reactangle.py)
  ### Requirements for low level:
  * ✔️ To develop **Rectangle** class with following content:
    * 2 closed float **sideA** and **sideB** (sides A and B of the rectangle).
    * Constructor with two parameters **a** and **b** (parameters specify rectangle sides).
    * Method **GetSideA**, returning value of the side A.  
    * Method **GetSideB**, returning value of the side B.
    * Method **Area**, calculating and returning the area value.  
    * Method **Perimeter**, calculating and returning the perimeter value.  
    * Method **IsSquare**, checking whether current rectangle is shape square or not.
    * Returns _True_ if the shape is square and _False_ in another case.  
    * Method **ReplaceSides**, swapping rectangle sides.  


- ## [Task 2 - Employee](https://gitlab.com/nosoccus/python-online-course-epam/-/blob/master/TASK_7/employee.py)
  ### Requirements for low level:
  * ✔️ To create basic class **Employee** and declare following contents:  
    * Three closed fields - text field **name** (employee last name), money fields - **salary** and **bonus**.
    * Public property **Name** for reading employee's last name.
    * Public property **Salary** for reading and recording salary field.
    * Constructor with parameters string **name** and money **salary** (last name and salary are set).
    * Method **SetBonus** that set bonuses to salary, amount of which is delegated/conveyed as bonus.
    * Method **ToPay** that returns the value of summarized salary and bonus.  
  * ✔️ To create class **SalesPerson** as class **Employee** inheritor and declare within it:  
    * Closed integer field **percent** (percent of sales targets plan performance/execution).  
    * Constructor with parameters: **name** - employee last name, **salary, percent** - percent of plan performance, first two of which are passed to basic class constructor.
    * Redefine method of parent class **SetBonus** in the following way: if the salesperson completed the plan more than 100%, so his bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3). 
  * ✔️ To create class **Manager** as **Employee** class inheritor, and declare with it:
    * Closed integer field **quantity** (number of clients, who were served by the manager during the month).
    * Constructor with parameters string **name** - employee last name, **salary** and integer **clientAmount** - number of served clients, first two of which are passed to basic class constructor.  
    * Redefine method of parent class **SetBonus** in the following way: if the manager served over 100 clients, his bonus is increased by 500, and if more than 150 - by 1000.
