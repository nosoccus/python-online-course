# TASK 12
> This assignment checks the knowledge of Linux bash. (and patience with writing of the documentation :D)

## Prerequisites:
* Install Windows Subsytem for Linux if you are using Windows.
* Please, create screenshots with Linux command output results in you hometasks directories.

Previously, I have installed WSL2 and setup Ubuntu 20.04 for it. So there is the screenshots of commands execution and output.


## Exercise 1:
* **1A**. Invoke ```pwd``` to see your current working directory (there should be your home directory).
  * ```ls -l /```
  * ```ls```
  * ```ls ~```
  * ```ls -l```
  * ```ls -a```
  * ```ls -la```
  * ```ls -lda ~```
* **1C**. Execute and describe the following commands (store the output, if any):
  * ```mkdirtest```
  * ```cd test```
  * ```pwd```
  * ```touch test.txt```
  * ```ls -l test.txt```
  * ```mkdirtest2```
  * ```mv test.txt test2```
  * ```cd test2```
  * ```ls```
  * ```mv test.txt test2.txt```
  * ```ls```
  * ```cp test2.txt ..```
  * ```cd ..```
  * ```ls```
  * ```rm test2.txt```
  * ```rmdir test2```
* **1D**. Execute and describe the difference:
  * ```cat /etc/fstab```
  * ```less /etc/fstab```
  * ```more /etc/fstab```
* **1E**. Look through man pages of the listed above commands.
  * ```man cat /etc/fstab```
  * ```man less /etc/fstab```
  * ```man more /etc/fstab```



## Exercise 2:
* **2A**. Discovering soft and hard links. Comment on results of these commands (place the output into your report):
  * ```cd```
  * ```mkdirtest```
  * ```cd test```
  * ```touch test1.txt```
  * ```echo “test1.txt” > test1.txt```
  * ```ls -l``` // a hard link
  * ```ln test1.txt test2.txt```
  * ```ls -l``` // pay attention to the number of links to test1.txt and test2.txt
  * ```echo “test2.txt” > test2.txt```
  * ```cat test1.txt test2.txt```
  * ```rm test1.txt```
  * ```ls -l``` // now a softlink
  * ```ln -s test2.txt test3.txt```
  * ```ls -l``` // pay attention to the number of links to the created files
  * ```rm test2.txt;ls -l```
* **2B**. Dealing with chmod.
  * An executable script. Open your favorite editor and put these lines into a file:
  ```bash
  #!/bin/bash
  echo “Drugs are bad MKAY?”
  ```
  * Give name “script.sh” to the script and call to:
  ```bash
  chmod +x script.sh
  ```
  * Then you are ready to execute the script:
  ```bash
  ./script.sh
  ```

