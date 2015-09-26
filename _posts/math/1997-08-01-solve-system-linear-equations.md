---
title: Solve a System of Linear Equations
author: Marcus Kazmierczak
layout: post
categories:
  - math
---


<p data-height="468" data-theme-id="7221" data-slug-hash="GJgpE"
data-default-tab="result" data-user="mkaz" class='codepen'>See the Pen <a
href='http://codepen.io/mkaz/pen/GJgpE/'>Solve a Linear System of Equations</a>
by Marcus Kazmierczak (<a href='http://codepen.io/mkaz'>@mkaz</a>) on <a
href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>



## The Mathematics Behind It

<p>The above solves a system of 3 equations and 3 unknowns, for example :</p>
<pre>
	 x + 2y + 3z = 9
	2x -  y +  z = 8
	3x      -  z = 3
</pre>

<p>This would be entered into the matrix above as : </p>
<pre>
	1   2   3  : 9
	2  -1   1  : 8
	3   0  -1  : 3
</pre>

<p>And the result would give you </p>
<pre>
		x =  2
		y = -1
		z =  3
</pre>

which can be easily checked by entering each value into any of the equations. 

Now how was this all done so magically using Java Script?

The technique I used to solve the system of equations is called row reduction, or <b>reduced row eschelon form</b>. This is manipulating the equations by one of the following operations:


1. Multiplying any Row by a Non-Zero Constant

2. Replacing a Row(k) with { Row(i) + Row(k) } ; where i, k are any row

3. Interchanging any two rows. (flipping row(i) with row(k))


By applying these operations, you can reduce the matrix down so you have 1's along the diagonal and zero's elsewhere. Which leaves you with the solution in the augmented portion of the matrix.

A couple of problems do arise in particular systems. There are sets of equations which have no solution, and also systems which have infinitely many solutions. They arise geometrically from having either two parallel planes (no solutions) or having two planes being the same (infinite solutions).

Both cases were not handled very well by my programming. I may try and fix it up some. <i>BUT</i> I did check my answer, and an alert will display if there is an erroneous solution. So I covered myself.

## Related Links

* <a href="/java-matrix-calculator/">Have you seen the Java Applet Matrix Calculator?</a> I have made a new matrix calculator this time using double arrays in Java, which can now calculate <b>n x n</b> matrices, up to 50 x 50.

* Read about <a href="/linear-algebra-math/">the Linear Algebra mathematics </a> behind the calculators for some mathematical explanations on how the matrices are calculated.

