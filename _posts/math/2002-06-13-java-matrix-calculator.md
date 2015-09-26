---
title: Java Matrix Calculator
author: Marcus Kazmierczak
layout: post
categories:
  - math
---

### Download

* <a href="/a/math/MatrixCalculator.java"> MatrixCalculator.java </a> ver. 1.6

* <a href="/a/math/MatrixCalculator-1.5.java"> MatrixCalculator-1.5.java </a> ver. 1.5


### Change Log: 

* <b>Version 1.6 - June 30, 2005</b>br>
Contributed by Pierre Sequin &lt;sequin_pierre&#064;yahoo.ca&gt; <br>
Updated so it accepts any rectangular matrix for the transpose and also for multiplication if matrices A and B are appropriate size (ie 2x3 3x5 are acceptable for multiplication and produce a 2x5 matrix)

* <b>Version 1.5</b> - June 13, 2002 </b><br>
A rewrite of the older Java applet which was lost many computers ago,
only the functions were saved thanks to the web. This version was the
first GUI in Swing.  Source code fully available.

* Original Version 1996-97. Lost :(


### Compile and Run Matrix Calculator

No special classes or libraries are used with this application. The complete
source resides in the one file above. After downloading, the following should
work in any JDK 1.2 compatible compiler:<br>
<pre>
$ javac MatrixCalculator.java
$ java MatrixCalculator 
</pre>

<b>Screen Shot</b><br>
<img src="/a/math/mc_screen01.png" width=598 height=332 border=1 alt="Matrix Calculator Screen Shot">


### Matrix Calculator Tips/Help

All Matrices must be symmetric (n x n)

<p>Enter Matrix Elements Row by Row separated by spaces.
Ex. (3x3) </p>
<pre>
1 2 3
4 5 6
7 8 9
</pre>

Results will be placed in the C matrix.

The calculation of the determinant, by definition, is based upon a factorial number of calculations with respect to the size of the matrix. ie. a 3x3 matrix would have 6 calculations (3!) to make, whereas a 20x20 matrix would have 2.43 x 10^18 calculations (20!). So instead of brute forcing the calculations, I first do some operations on the matrix, which converts it to a upper triangular matrix, and then calculate the determinant by multiplying down the diagonal, since everything below is 0, this will give the
determinant.

<b>Floating Points and Accuracies</b> - For some reason computers aren't as accurate as I think they are, probably my calculation techniques. The accuracy of the numbers are probably only to 3 maybe 2 decimal places. If you keep applying operations to matrices and then use the resultant matrix a couple of times, the decimals get out of whack.

Calculating an inverse and then multiplying the matrix by it, is a good example of this.

### Test Some Mathematical Theories

* The determinant of A-inverse equals 1 over the determinant of A.
* If two rows of matrix A are equal, the determinant of A equals 0.
* det( A * B) = det(A) * det(B) 
* A * B does not necessarily equal B * A 
* The determinant of A-transpose equals the determinant of A.

* If the matrix B is constructed by interchanging two rows (columns) in matrix A, then the determinant of B equals the negative determinant of A 

* You can test, adj(A) = det(A) * inv(A), but this is the theorem I use to calculate the inverse, so it better work.

### Mathematics and Linear Algebra

<b>Calculating the Determinant</b>
The calculation of the determinant, by definition, is based upon a factorial number of calculations with respect to the size of the matrix. ie. a 3x3 matrix would have 6 calculations (3!), whereas a 20x20 matrix would have 2.43 x 10^18 calculations (20!).

So instead of brute forcing the calculations, I first do some operations on the matrix which converts it to a upper triangular matrix, and then calculate the determinant by multiplying down the diagonal, since everything below is 0, this will give the determinant.

Read about the <a href="/linear-algebra-math/">Linear Algebra Math</a> behind the calculators for more information and mathematical explanations on the definitions and calculation techniques.

