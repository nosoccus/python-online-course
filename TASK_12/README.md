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

  ![alt-text](TASK_12/img/1b_1.png)
  * #### ```ls```
  
  ![alt-text](TASK_12/img/1b_2.png)
  * #### ```ls ~```
  
  ![alt-text](TASK_12/img/1b_3.png)
  * #### ```ls -l```
  
  ![alt-text](TASK_12/img/1b_4.png)
  * #### ```ls -a```
  
  ![alt-text](TASK_12/img/1b_5.png)
  * #### ```ls -la```
  
  ![alt-text](TASK_12/img/1b_6.png)
  * #### ```ls -lda ~```
  
  ![alt-text](TASK_12/img/1b_7.png)
* **1C**. Execute and describe the following commands (store the output, if any):
  * #### ```mkdirtest```
  * #### ```cd test```
  * #### ```pwd```
  
  ![alt-text](TASK_12/img/1c_1.png)
  * #### ```touch test.txt```
  * #### ```ls -l test.txt```
    
  ![alt-text](TASK_12/img/1c_2.png)
  * #### ```mkdirtest2```
  * #### ```mv test.txt test2```
  * #### ```cd test2```
  * #### ```ls```
    
  ![alt-text](TASK_12/img/1c_3.png)
  * #### ```mv test.txt test2.txt```
  * #### ```ls```
    
  ![alt-text](TASK_12/img/1c_4.png)
  * #### ```cp test2.txt ..```
  * #### ```cd ..```
  * #### ```ls```
    
  ![alt-text](TASK_12/img/1c_5.png)
  * #### ```rm test2.txt```
  * #### ```rmdir test2```
    
  ![alt-text](TASK_12/img/1c_6.png)
* **1D**. Execute and describe the difference:
  * #### ```cat /etc/fstab```
    
  ![alt-text](TASK_12/img/1d_1.png)
  * #### ```less /etc/fstab```
      
  ![alt-text](TASK_12/img/1d_2.png)
  * #### ```more /etc/fstab```
      
  ![alt-text](TASK_12/img/1d_3.png)
* **1E**. Look through man pages of the listed above commands.
  * #### ```man cat /etc/fstab```
        
  ![alt-text](TASK_12/img/1e_1.png)
  * #### ```man less /etc/fstab```
        
  ![alt-text](TASK_12/img/1e_2.png)
  * #### ```man more /etc/fstab```
        
  ![alt-text](TASK_12/img/1e_3.png)



## Exercise 2:
* **2A**. Discovering soft and hard links. Comment on results of these commands (place the output into your report):
  * #### ```cd```
  * #### ```mkdirtest```
  * #### ```cd test```
      
  ![alt-text](TASK_12/img/2a_1.png)
  * #### ```touch test1.txt```
  * #### ```echo “test1.txt” > test1.txt```
  * #### ```ls -l``` // a hard link
        
  ![alt-text](TASK_12/img/2a_2.png)
  * #### ```ln test1.txt test2.txt```
  * #### ```ls -l``` // pay attention to the number of links to test1.txt and test2.txt
        
  ![alt-text](TASK_12/img/2a_3.png)
  * #### ```echo “test2.txt” > test2.txt```
  * #### ```cat test1.txt test2.txt```
        
  ![alt-text](TASK_12/img/2a_4.png)
  * #### ```rm test1.txt```
  * #### ```ls -l``` // now a softlink
        
  ![alt-text](TASK_12/img/2a_5.png)
  * #### ```ln -s test2.txt test3.txt```
  * #### ```ls -l``` // pay attention to the number of links to the created files
        
  ![alt-text](TASK_12/img/2a_6.png)
  * #### ```rm test2.txt;ls -l```
        
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
  * Then you are ready to execute the script:
  ```bash
  ./script.sh
  ```
        
  ![alt-text](TASK_12/img/2b_3.png)
