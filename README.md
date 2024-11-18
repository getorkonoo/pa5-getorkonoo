# Programming Assignment 5

**Points:** 100 total (20 part 1, 80 for the other parts of the project)

**Due:** See "Part 1" and "Final" sections

## Problem

The files **2016_09.csv** and **2016_10.csv** contain data for taxi trips in the city of Chicago for the months 
of September and October (respectively) 2016 in comma-separated values format. Each line contains the values in 
the following order:

1. Taxi's id number
2. Date and time of the start of the trip in month/day/year hour:minute format
3. Date and time of the end of the trip in month/day/year hour:minute format
4. Duration of trip in seconds
5. Distance of the trip in miles
6. Cost of the trip
7. Payment type ("Cash" or "Credit Card")
8. Taxi company
9. Pickup location latitude (-90 to 90)
10. Pickup location longitude (-180 to 180)
11. Dropoff location latitude (-90 to 90)
12. Dropoff location longitude (-180 to 180)

Write a program which, given the name of a file in the above format, loads the file into a list of lists and is able to perform the following tasks (include one function per task):

1. Output the average cost for cash payments.
2. Output the average cost for credit card payments.
3. Output the number of all trips that started or ended on a user-given date.
4. Output to a file (name provided by the user) the information for all trips that occurred within a given distance of a user-given point (latitude, longitude). 
  * Each output line should be in the same format as the input file
  * Distance is given by the user in miles
  * Location is given by the user as a latitude and longitude
  * The distance between two points P1 = (lat1, lon1) and P2 = (lat2, lon2) can be calculated using the formula distance = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 3,959 miles. Note that one point comes from the user and the other comes from the file entry. **Note:** The [trigonometric functions](https://docs.python.org/3/library/math.html#trigonometric-functions) can be found in the math module.

Note 1: none of the functions (other than main) should output anything to the screen. If you need to call a function and  output something, then that function can return a value and you can output that value in the main.
Note 2: you will need to code other functions

The program must allow the user to choose which of the above options (1,2,3,4) they want to do. Your program must work for any file with the above format without any modification. Additionally, your program should perform error checking, including filename checking, try/except in file-processing functions, and checking that input by the user is of the valid type in the valid range as follows:  
check that the distance entered by the user is a non-negative integer,  
check that the latitude entered by the user is between -90 and 90 (you do not have to check that the user entered a float, you can assume that he/she did)  
check that the longitude entered by the user is between -180 and 180 (you do not have to check that the user entered a float, you can assume that he/she did)  
for the date, you can assume that the user will enter the date in the proper format; no need for error checking here.  

## Part 1: due Wed November 17, 2021, 10AM 

1. Create a new Python file and place **intro comments** at the top:
CS151, Pr. Franceschi, Programming Assignment 5  
  
\# Name:  
\# Date:  
\# Problem Summary:  
\# Inputs:  
\# Outputs:   
2. Code a function, including comments, to read from a file (similar to the ones supplied) and return a list of lists.  
3. Create a new file with just the **first 10 lines** of one of the 2 data files provided. Name it **testinput.csv**.  
4. Code a function, including comments, to calculate and return the distance between 2 points on earth. A point is defined as having a latitude and a longitude.  
5. Inside main, call the function in 2 above for the "small" file in 3 above and output the returned list of lists. Call the function in 4 above as follows: Test your distance function with the coordinates of **Baltimore** (+39.2904, -76.6122) and **Washington DC** (+38.9072, -77.0369). The approximate distance result should be **34.92485 miles**.

## IMPORTANT NOTE: I will be giving a solution in class on Wednesday November 24, so you cannot turn in this assignment (Part 1) after that date/time

### Submission

* **Github:** commit and push your .py file changes and check github.com to confirm the update.  

## Final: due Tue Nov 23, 2021, 10AM

1. Write the Python **code** corresponding to each of your algorithm's steps.
2. Testing: 
  * Create a test file that contains the first 10 lines from one of the original data file. Name it **testinput.csv**. 
  * Create a set of test cases based on this test file (**1 case per question**) using Excel in a file named **testcases.xlsx**.

**Test** your completed code using your test cases. If the output doesn't match, correct your program.

### Submission

* **Github and Moodle:** 
* commit and push your .py file changes and check github.com to confirm the update.
* Your test file in testinput.csv
* Your testcases.xls file.

This assignment does **not** require a flowchart.
