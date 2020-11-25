# TASK 12
> This assignment checks the knowledge of Linux bash. (and patience with writing of the documentation :D)

## Prerequisites:
* Install Windows Subsytem for Linux if you are using Windows.
* Please, create screenshots with Linux command output results in you hometasks directories.

Previously, I have installed WSL2 and setup Ubuntu 20.04 for it. So there is the screenshots of commands execution and output.


## Exercise 1:
* **1A**. Invoke ```pwd``` to see your current working directory (there should be your home directory).
![alt-text](TASK_12/img/1a_pwd.png "1a_pwd")
* **1B**. Collect output of these commands:
  * #### ```ls -l /```
  > arg ```-l``` is stands for long format, ```/``` - for root folders

  ![alt-text](TASK_12/img/1b_1.png)
  * #### ```ls```
  > bare ls - list contents of a directory (files and directories)
  
  ![alt-text](TASK_12/img/1b_2.png)
  * #### ```ls ~```
  > ls for user directory

  ![alt-text](TASK_12/img/1b_3.png)
  * #### ```ls -l```
  > arg ```-l``` is stands for long format

  ![alt-text](TASK_12/img/1b_4.png)
  * #### ```ls -a```
  > lists all files in the given directory, including those whose names start with "." (which are hidden files in Unix)

  ![alt-text](TASK_12/img/1b_5.png)
  * #### ```ls -la```
  > ls hidden files in long format

  ![alt-text](TASK_12/img/1b_6.png)
  * #### ```ls -lda ~```
  > ```-d``` shows information about a symbolic link or directory, other is described aboveю

  ![alt-text](TASK_12/img/1b_7.png)
* **1C**. Execute and describe the following commands (store the output, if any):
  * #### ```mkdir test```
  > creates a folder named ```test```
  * #### ```cd test```
  > changes current directory to the ```test```
  * #### ```pwd```
  > prints working directory
  
  ![alt-text](TASK_12/img/1c_1.png)
  * #### ```touch test.txt```
  > creates file ```test.txt```
  * #### ```ls -l test.txt```
  > ls in long format files that match pattern ```test.txt```
    
  ![alt-text](TASK_12/img/1c_2.png)
  * #### ```mkdirtest2```
  > creates folder named ```test2```
  * #### ```mv test.txt test2```
  > moves file ```test.txt``` from folder ```test``` to ```test2```
  * #### ```cd test2```
  > changes current directory to ```test2```
  * #### ```ls```
  > lists contents of a directory ```test2```
    
  ![alt-text](TASK_12/img/1c_3.png)
  * #### ```mv test.txt test2.txt```
  > moves file ```test.txt``` to file ```test2.txt```
  * #### ```ls```
  > lists contents of a directory
    
  ![alt-text](TASK_12/img/1c_4.png)
  * #### ```cp test2.txt ..```
  > copies file ```test2.txt``` to the folder above
  * #### ```cd ..```
  > changes current directory to the folder above (```test```)
  * #### ```ls```
  > lists contents of a directory
    
  ![alt-text](TASK_12/img/1c_5.png)
  * #### ```rm test2.txt```
  > removse(deletes) the file ```test2.txt```
  * #### ```rmdir test2```
  > removes the directory test2 (failed because not empty; need flag ```-rf```)
    
  ![alt-text](TASK_12/img/1c_6.png)
* **1D**. Execute and describe the difference:
  * #### ```cat /etc/fstab``
  > shows contents of ```/etc/fstab``` file
    
  ![alt-text](TASK_12/img/1d_1.png)
  * #### ```less /etc/fstab```
  > shows less contents of ```/etc/fstab``` file
      
  ![alt-text](TASK_12/img/1d_2.png)
  * #### ```more /etc/fstab```
  > shows more contents of ```/etc/fstab``` file

  ![alt-text](TASK_12/img/1d_3.png)
* **1E**. Look through ```man pages``` of the listed above commands.
  * #### ```man cat /etc/fstab```
  > shows the manual for ```cat```

  ![alt-text](TASK_12/img/1e_1.png)
  * #### ```man less /etc/fstab```
  > shows the manual for ```less```

  ![alt-text](TASK_12/img/1e_2.png)
  * #### ```man more /etc/fstab```
  > shows the manual for ```cat```

  ![alt-text](TASK_12/img/1e_3.png)



## Exercise 2:
* **2A**. Discovering soft and hard links. Comment on results of these commands (place the output into your report):
  * #### ```cd```
  > return to parent directory
  * #### ```mkdir test```
  > make directory ```test``
  * #### ```cd test```
  > change directory to ```test```

  ![alt-text](TASK_12/img/2a_1.png)
  * #### ```touch test1.txt```
  > create file ```test1.txt```
  * #### ```echo “test1.txt” > test1.txt```
  > writes "test1.txt" to ```test1.txt```
  * #### ```ls -l``` // a hard link
  > checks files in directory in long format

  ![alt-text](TASK_12/img/2a_2.png)
  * #### ```ln test1.txt test2.txt```
  > creates a hard link ```test2.txt``` to the file ```test1.txt```
  * #### ```ls -l``` // pay attention to the number of links to test1.txt and test2.txt
  > checks files in directory in long format
        
  ![alt-text](TASK_12/img/2a_3.png)
  * #### ```echo “test2.txt” > test2.txt```
  > writes "test2.txt" to ```test2.txt```
  * #### ```cat test1.txt test2.txt```
  > catenate two files

  ![alt-text](TASK_12/img/2a_4.png)
  * #### ```rm test1.txt```
  > remove ```test1.txt``` file
  * #### ```ls -l``` // now a softlink
  > checks files in directory in long format. There is only ```test2.txt```.

  ![alt-text](TASK_12/img/2a_5.png)
  * #### ```ln -s test2.txt test3.txt```
  > creates soft link ```text3.txt``` to the ```text2.txt```.
  * #### ```ls -l``` // pay attention to the number of links to the created files
  > There are two files: ```text2.txt``` and ```text3.txt```, where ```text3.txt``` is a soft link to the ```test2.txt```.

  ![alt-text](TASK_12/img/2a_6.png)
  * #### ```rm test2.txt;ls -l```
  > removes the file ```test2.txt``` and lists only ```test3.txt```.
        
  ![alt-text](TASK_12/img/2a_7.png)
* **2B**. Dealing with ```chmod```.
  * An executable script. Open your favorite editor and put these lines into a file:
  ```bash
  #!/bin/bash
  echo “Drugs are bad MKAY?”
  ```
          
  ![alt-text](TASK_12/img/2b_1.png)
          
  ![alt-text](TASK_12/img/2b_2.png)
  * Give name “script.sh” to the script and call to:
  ```bash
  chmod +x script.sh
  ```
  > ```chmod``` gives a permission to a file and ```x``` stands for execution, so it gives a user permission to execute the file
  * Then you are ready to execute the script:
  ```bash
  ./script.sh
  ```
        
  ![alt-text](TASK_12/img/2b_3.png)
