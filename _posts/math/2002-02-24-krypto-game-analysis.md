---
title: Krypto Game Analysis
author: Marcus Kazmierczak
layout: post
categories:
  - math
---

Krypto is a game which five cards are put down each with a number on it from one to twenty-five.  Using normal arithmetic operations ( +, -, * , / ) on these five cards to equal a sixth card that is also from one to twenty-five.

An example game:

<pre>
    Game:  2   4   3   6   5   :  6
</pre>


Here's two possible solutions:

<pre>
    Solution 1:  6 + 5 + 2 - 4 - 3  = 6 
    Solution 2:  (((2 + 3) - 5) * 4) + 6 = 6 
</pre>

As you can see, you can rearrange the numbers any way you want and apply the operations in any order using parentheses.

So, being the mathematical and programmer type of guy
that I am, I wrote up a program to solve these Krypto games.
My program finds 5,000 solutions for the above problem.

After creating the solver program, I thought about games that don't have a solution, one obvious game being:

<pre>
    Game:  1   1   1   1   1   :  25
</pre>

Being still the same type of guy I wrote a program to find all games which don't have a solution. Of the total 2,968,875 possible games there are only 61,910 without a solution, only  2.09% of the games.

Ok, enough with the background info... if you are a similar type of person as me, why else would you still be reading this, you want the math and programs behind all this. So here goes.  


## The Mathematics Behind Solving Krypto

I'd been playing with Python when programming my <a href="/prime-numbers/">prime number scripts</a> and decided this was another perfect opportunity for Python.  Since Python has a nice <b>eval()</b> function, which evaluates math equations, all I had to do was generate all the different possible equations for one Krypto game and Python could simply evaluate my equations .


#### Permutation of Game Numbers

First thing I needed to do was generate all the different permutations of ordering the numbers in the game. For example: 

<pre>
    2  4  3  6  5
    2  4  3  5  6
    2  4  5  6  3
    ...
    5  6  3  4  2
</pre>

A permutation of <b>n</b> numbers with ordering will give us n! (n-factorial) orderings. For our case this will be 120 orderings of the game numbers.

Being the lazy person I am, I searched the web and found the exact routine I was looking for in "Programming Python: Chapter 17"

#### Combinations of Operations

Now we have all the different ways the numbers can be ordered what we need to do is plug-in all the different ways operations can be distributed across each ordering.

Unfortunately I couldn't find this algorithm to generate these list, so I had to write one up. After writing out a few examples, a nice pattern emerged which I based my routine on.  Here's the few examples using just two operations (+,-):

Choosing two items:

<pre>
    + + 
    + - 
    - + 
    - - 
</pre>

Choosing three items:

<pre>
    + + + 
    + + - 
    + - + 
    + - - 
    - + + 
    - + - 
    - - + 
    - - - 
</pre>

Looking at choosing three items, the pattern in the farthest right column, the item switches over the period 1 meaning it switches each time: plus, minus, plus, minus. 

In the next column the switching period is 2: plus, plus, minus, minus.

In the first column the switching period is 4: + + + + - - - -

So the pattern is the operations switch starting column number C=0 at the right  2^C.  This was easily expanded when using 4 operations.

So generating all the different combinations of four-different operations choosing four items gives me 4^4 items or 256 orderings of operations.

<b>Mini-Summary</b>

Now having all the different permutations of the numbers and the combinations of the operations I can start generating equations. 

Example:

<pre>
    Taking the first permutation of numbers:  2 4 3 6 5 
    And the first combo of operations: + + + + 
    Gives me the equation: 2 + 4 + 3 + 6 + 5 
    Evaluate and check against what we are trying for.
</pre>

But wait... what about:

<pre>
    Permutation: 2 4 3 6 5 
    Operations:  + * + * 
    Equation: 2 + 4 * 3 + 6 * 5
</pre>

The above can be evaluated several different ways depending on
how you use parentheses. Example:

<pre>
    2 + 4 * 3 + 6 * 5 = 44    &lt;-- standard order of operations
    (2 + 4) * (3 + 6) * 5 =  270 
    (2 + (4 * 3) + 6) * 5 = 100 
</pre>


#### Parenthesizing Equations

So I need to apply all the different ways parentheses can be used on an equation of five numbers and four operations. It turns out to be fourteen different ways.  This was done by hand creating the different parentheses cases.  

So now we need to evaluate 120 permutation over 256 operations against 14 different parenthetical equations. This gives the total possible ways of solving one Krypto game which is 120 * 256 * 14 = 430,080 

Several of these are duplicates, for example if you have all plus, all minus, or all multiplication you don't need parentheses. But I figured that the computation time to do checks probably slowed the computer down more than just brute force. I'm not 100% sure if this is right or not. A couple of variations I tried slowed it down a few sped it up.


Also I have a few other hypotheses which I haven't proved but I believe are provable.  One is that you can always use the absolute value of your answer since if you get a negative result, a positive result can be found by rearranging the ordering.

My other hypothesis is that when dividing and you get a non-integer result you can throw out this attempt even though when multiplying by another integer may get you back to a whole integer. Since all permutations and ordering are done you will make an attempt to solve the equation when multiplying first and never reach a non-integer solution. 

So after coding all of this up in Python and getting it all to work.  I had a program which could solve a Krypto game. woo hoo!   One problem, it took approx. 2 min 30 sec to find all the solutions to one game, or to find that a game had no solution. 

Next I wrote a script to generate the 2,968,875 different Krytpo games which which turns out to be a 45mb text file!  This number comes from Pascal's Triangle (see related links below) and it was easier to code then figure out how that number is actually calculated.

Generating all the games is simply some "for loops" using the previous loop number, remember the game 1 2 3 4 5 is the same as the game 5 4 3 2 1.  (See scripts below for details)


So now it was just a matter of processing all of these games. My rough guestimates on how many possible games that don't have a solution using my Python scripts:

<pre>
    5,000 * 2m30s = 208+ hours of computing time 
    2,000 * 2m30s = 83+ hours of computing time 
</pre>

When actually there are 61,910 games without a solution which would have been over 107 days straight computing time needed. After thinking of various ways of getting this number down, I decided that Python was not the right solution and tried a compiled language.

So I rewrote everything in C, which is not my strongest language, but that's what I get for taking math classes instead of computer classes.  I had to create my own equation evaluator using registers, since C doesn't have the same nice eval() function.  But somehow I got it all to work and was able to calculate the total number of solutions in just under 4 hours of computing time.

You can download all 61,910 games that don't have a solution here: <a href="/math/krypto-files/games_nosols.txt.gz">games_nosols.txt.gz</a> (176kb)



## Download Programs Here

<b>Python Code</b> (ver 2.2)

* <a href="/a/krypto-files/solver.py"><b>solver.py</b></a> - Main Solving script, you can enter a game or generate a randome one and this script solves it. Check file for other options.


* <a href="/a/krypto-files/mkryptolib.py"><b>mkryptolib.py</b></a> - My Krypto library, this holds all of the functions for permutations, choosing and parentheses. The solver script above requires this library.


* <a href="/a/krypto-files/create_games.py"><b>create_games.py</b></a> - This script generates all of the possible Krypto games, it prints to stdout (your screen) so you probably want to redirect this to a file.


<b>C Code</b><br>

* <a href="/a/krypto-files/solver.c"><b>solver.c</b></a><br> C Solver program. This script finds all the solutions to a particular game, specified by command-line.
		
* <a href="/a/krypto-files/nosols.c"><b>nosols.c</b></a><br> This program reads in Krypto games from a text file and writes out if the game if there is no solutions. Text file specified at the command-line, format expected from create_games program.


* <a href="/a/krypto-files/create_games.c"><b>create_games.c</b></a><br> A script to generate the different Krypto games. I plugged in different numbers in this script to generate five or so different text files of games so I could run them on several computers at the same time.
	

All program timings are based on programs running on my Ti Powerbook G4 500mhz running Mac OS X 10.1.3.
 
Programs were also tested and ran on Redhat Linux 7.2 

* * * 


## Related Links

<a href="http://www.pearsonlearning.com/plearn/html/cat_progseries.cfm?sub_id=S4&grade=-1,12&prog_id=13762002&imprint_id=IM5">Pearson Learning Group</a><br>
Manufacturer of the game Krypto. Available from their site for $8.95

<a href="http://www.math.niu.edu/~rusin/uses-math/games/krypto/">Krypto Arithemetic Card Game</a> Analysis Page<br>
A great site by Dave Rusin, very similar to mine which includes Maple programs to solve Krypto games. I confirmed my parentheses from this site and got some good ideas from his analysis pages.
	
<a href="http://webpages.shepherd.edu/skunyosy/miles/counting.html">Counting Techniques</a><br>
A site with different counting techniques such as permutations, combinations and Pascal's Triangle.  This site covers the basics covered in most any Probablity class.

<a href="http://www.amazon.com/exec/obidos/ASIN/B00004NKL3/mkazcom-20">Smath Board Game</a> A similar game to Krypto but Smath is a board game instead of a card game.  Basically Smath is a math version of Scrabble where you form valid math equations using the various tiles. Operations, Numbers, Brackets, etc...


