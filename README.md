# Results Analyzer

## General information:
This software generates charts and tables with data based on exam results. The final PDF file contains both total data and every question data.

## Additional information:
It takes 4 different answers: A, B, C, D.<br />
Information if majority of 15% of students with best results selected other answer than the correct one.<br />
Possibility of adding question photo to every question in final report.<br />

## How to run
Best way to run is to start setup.py and use GUI.

## How to use:
1.	Select results data file.
2.	Select correct answers file.
3.	Select destination directory for the reports.
4.	(optional) Fill “Multiple separator” and “All correct symbol”.
5.	Fill “Pass rate” and select unit.
6.	Select exams.
7.	(optional) Load image files
8.	Start

## Add exam images:
- To add images use “Load” button in the row with exam. Warning! Names of the image files must be in alphabetical order! If you use numbers to order put zero in front of lower numbers. For example use 01, 02, 03… instead of 1, 2, 3… when number of questions is bigger than 10 and lower than 99.<br />
- If the question image file’s resolution is too big it will be resized to fit the page.

## Input data information:
- Input files are results and keys files in CSV format (separator - ;). Results file must contain header, otherwise first row will not be calculated. <br />
- Order of the results and keys does not matter.<br />
- Uppercase/lowercase does not matter.<br />
- If your answers are not “A/B/C/D” just change it to these values.<br />
- If answer is not A/B/C/D it will be counted as incorrect.<br />
- It is possible to put multiple correct answers – just fill the “Multiple separator” entry with the separator used in file with correct answers. For example “ or “ - “A or B or C”.<br />
- Also when all answers are correct fill the “All correct symbol” entry with the symbol used in file with correct answers. - Then all answers to this question will be counted as correct. <br />

## Example data:
### Results:<br />
```
examname;version;1;2;3;4;5;6;7;8;9;10
Exam3;X;D;D;D;C;C;D;D;B;C;B
Exam1;Y;D;D;A;B;B;D;C;B;B;D
Exam2;X;D;A;D;C;B;B;B;A;C;B
```
### Keys:
```
examname;version;1;2;3;4;5;6;7;8;9;10
Exam1;X;D;B;C;D;B;B;C;C;A;D
Exam2;X;D;all;A;A or B;C;C;C;B;A;D
```
