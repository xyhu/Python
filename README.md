Python
======
This repository contains codes from my Python class.

* Project 1: Cellular Automation. The description of the project requirement can be found here:
http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P1/
  - Topics: interpreter, expressions, strings, functions and the various flow-of-control constructs
  - project1.py: codes
  - rule~.pbm: bitmap produced by corresponding rule using project1.py

* Project 2
  * 2a: Python-powered Unit Converter. The description of the project requirement can be found here:
http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P2a/
    - Topics: tuples, lists, dictionaries
    - Project2_Unit_Conversion.py: codes

  * 2b: Basic web programming. The description of the project requirement can be found here:
http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P2b/
    - Topics: basic web fetching
    - Project2_Web_programming.py: codes
    - Description: The program extract NBA champion data from: http://www.landofbasketball.com/championships/year_by_year.htm and runs as follows:<br>

    Want to find out the NBA champions for a particular year? Simply tell me the year (e.g. 2013-14), and I will tell you everything as follows:<br>
    
    	Champion
    	Score
    	Runner-up
    	Final-MVP
    	Final-MVP's team
    	Season-MVP
    	Season-MVP's team
    	
    Please note that Finals MVP started from year 1968-69, Season MVP started from 1955-56<br>
    Find the NBA champion of year XXXX-XX, or (q)uit]: 1970-71<br>
    
        Milwaukee Bucks
        4-0
        Baltimore Bullets
        Kareem Abdul-Jabbar
        (Milwaukee Bucks)
        Kareem Abdul-Jabbar
        (Milwaukee Bucks)
      
    Find the NBA champion of year XXXX-XX, or (q)uit]: <br>

* Project 3: Online Mad Libs. The description of the project requirement can be found here:
http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P3/
  - Topics: deploying CGI scripts, HTTP headers, CGI module functions, form processing
  - Mad_Libs.cgi: codes that generate forms for user to fill in
  - Mad_Libs2.cgi: codes that give the user the sentence with their words

* Project 4: Turtle Behavior. The description of the project requirement can be found here:
http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P4/
  - Topics: object-oriented programming
  - Statue.py: inherited from class Turtle(this is not the turtle module in Python, it is provided by the project. Same below). It creates a statue at the center of the widget.
  - Mouse.py: inherited from class Turtle. It creates a mouse(blue filled square) that moves counterclockwise around the statue for 1m (defined as 25 pixels) for every step.
  - Cat.py: inherited from class Turtle. It creates a cat(red filled square) that moves 1m(defined as 25 pixels) towards the statue if it sees the mouse until it cannot further move into the statue. Otherwise, it will move counterclockwise for 1.25m for every step.
  - CatMouse.py: the driver program
