# W6_5

Create a program which can analyse numbers in a text file.

Required values in analysis:

* Total - integer - Sum of numbers
* Count - integer - Rows that contain values
* Greatest - integer - The greatest number of them all
* Average - decimal - The numbers average

Think about the processes or “steps” of the analytics first. A prosess which can be described with a name should be wrapped into a function. This function then should only do the task, which belongs to it based on the name. For example if the function name is “readValues”, then the function should read the values from a file. If the function name is “analyseNumbers”, then it should not read a textfile.

Pseudo-example below:

````
SEPARATOR = ";"
def readValues() -> str:
  # read operations...
  Values: str = ""
  Values += str(13) + SEPARATOR
  Values += str(45) + SEPARATOR
  Values += str(20)
  return Values
````
Contain only things that the Divide the program structure based on the processes. Define functions to handle the meaningful smaller parts of the program e.g., reading numbers from a given textfiles, analysing numbers and displaying results. Reading values from a file and then storing the values back into a string for the return will help to separate value reading and analysis into their own functionalities.

This task will not evaluate how well you have structured your code or separated the processes into their own functionalities. But definitely this is a good place to start to consider how robust code are you actually building.

Present average result in 2 digit precision. 

Dataset details:

* These datasets contain only positive integer numbers.
* No empty lines.
  
The results are displayed in CSV format in the example program runs. The first row contains headers, followed by a single data row. Both the column headers and the data values are separated by a semicolon (;). The format is similar to how data is structured in Excel.

| Count | Sum | Greatest | Average| 
| ------ | ------ | ----- | ------ |
| 2  | 53  | 43 | 26.50|

Run 1
````
Program starting.
Insert filename: A6_T5_D1.txt
#### Number analysis - START ####
File "A6_T5_D1.txt" results:
Count;Sum;Greatest;Average
2;53;43;26.50

#### Number analysis - END ####
Program ending.
````

Run 2
````
Program starting.
Insert filename: A6_T5_D2.txt
#### Number analysis - START ####
File "A6_T5_D2.txt" results:
Count;Sum;Greatest;Average
10;508;91;50.80

#### Number analysis - END ####
Program ending.
````

Run 3
````
Program starting.
Insert filename: A6_T5_D3.txt
#### Number analysis - START ####
File "A6_T5_D3.txt" results:
Count;Sum;Greatest;Average
100;5608;98;56.08

#### Number analysis - END ####
Program ending.
````
