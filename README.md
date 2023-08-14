# Data Structures & Algorithms III - SCS 2201: String Matching Assignment - Using Naive String Matching Algorithm

## Reason to Choose Naive Algorithm 

I chose to use the Naive algorithm for the assignment because it's easy to work with. This let me concentrate on other parts of the task and still get a working solution.

## Pattern Matching

This Python program reads a pattern and a text from separate files. Then identifies where the pattern matches within the text. The pattern can include special characters such as ^, $, and ., each with different meanings.

## Features

The program can deal with patterns starting with ^, which means the pattern must match the beginning of the text.
The program can deal with patterns ending with $, which means the pattern must match the end of the text.
The program can deal with patterns containing ., which means it can match any character.

The program writes the matching positions to another file.

## Usage

To use this program, you need to prepare two files: one for the pattern and another for the text. These files should be placed in the "test_cases" folder. The pattern file should have a single line with the pattern, while the text file should contain a single line with the text. For example:

#### pattern1.txt:

```
^.at$
```

#### text1.txt:

```
cat
```
#### pattern2.txt:

```
^hell.
```

#### text2.txt:

```
hello world hello world
```
#### pattern3.txt:

```
w.r.d$
```

#### text3.txt:

```
hello world
```
#### pattern4.txt:

```
.at
```

#### text4.txt:

```
cat mat hat sit
```

The program will read these files and find the positions in the text where the pattern matches. The output will be written to another file, which will be placed in the out folder. The output file will contain one line for each matching position, followed by an empty line. For example:

#### patternmatch1.output.txt:

```
0
```
#### patternmatch2.output.txt:

```
0
```
#### patternmatch3.output.txt:

```
6
```
#### patternmatch4.output.txt:

```
0
4
8
```
For example, 0 means that the pattern matches position 0 in the text.

## Installation

To execute this program, you should have Python installed. Then, navigate to the directory containing the "main.py" file and use the following command to run the program:

```
python main.py
```

## Testing

Test cases are stored in **test_cases** folder. The relevent text for patter**n**.txt is text**n**.txt. And their output will be generated in **out** folder, with the name **patternmatchn.output.txt**

## Dependencies

This program doesn't need any library to work.
