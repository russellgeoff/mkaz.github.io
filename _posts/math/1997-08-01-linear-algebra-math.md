---
title: Linear Algebra Math
author: Marcus Kazmierczak
layout: post
categories:
  - math
---

Here are some of the definitions and examples used in Linear Algebra and specifically the linear algebra calculators available.

Let <b>A</b>, <b>B</b>, and <b>C</b> represent <i>n</i> x <i>n</i> matrices.

Example of a 3 x 3 Matrix:
<pre>
1  2  3
1  1  2
0  1  2
</pre>

<dt><b>A</b> + <b>B</b> = <b>C</b> </dt>
<dd>The <b>addition</b> of two matrices is straight forward. You just add each matrix position-wise. So the upper-left element of matrix <b>A</b> plus the upper-left element of matrix <b>B</b> is the upper-left element in matrix <b>C</b>. Do the same for all elements. </dd>

<dt><b>A</b> x <b>B</b> = <b>C</b></dt>
<dd> The <b>multiplication</b> of two matrices is not quite as simple. First we need the matrices to be of proper size. This means matrix <b>A</b> size <i>n</i> x <i>m</i> must be multiplied by a <i>m</i> x <i>p</i> matrix. The resultant matrix will then be <i>n</i> x <i>p</i>.
For our case, we are using <i>n</i> x <i>n</i> matrices, so this isn't a problem.

The equation for multiplying two matrices is : <i>(elementwise)</i>
<pre>
    [<b>AB</b>]<sub>ij</sub> = <b>SIGMA</b> [<b>A</b>]<sub>ik</sub>[<b>B</b>]<sub>kj</sub></font>
</pre>

Where the <b>SIGMA</b> summation goes from k=1...n


A example element from our 3x3 Case. To get the first element in our solution matrix <code> c<sub>11</sub></code>

<pre>c<sub>11</sub> = (a<sub>11</sub> * b<sub>11</sub>) + (a<sub>12</sub> *
      b<sub>21</sub>) + (a<sub>13</sub> * b<sub>31</sub>)
</pre>

Where a<sub>ij</sub> and b<sub>ij</sub> are from matrices <b>A</b>, <b>B</b> respectively.

<hr>

<dt>trace(<b>A</b>) </dt>
<dd>The<b> trace</b> of a matrix is simply the summation of its main diagonal.</dd>

<hr>

<dt><b>A</b><sup>T</sup> </dt>
<dd>The <b>transpose</b> of a matrix is switching the rows and columns. </dd>

For example: 
<table>
<tr>
  <td><b>A</b> = </td>
  <td><tt>a b c <br>
  d e f <br>
  g h i </tt></td>
  <td WIDTH="50"></td>
  <td><b>A</b><sup>T</sup> = </td>
  <td><tt>a d g <br>
  b e h <br>
  c f i</tt> </td>
</tr>
</table>

<hr>

<dt> det(<b>A</b>) </dt>
<dd> The <b>determinant</b> of a matrix is not quite simple. For a <i>n x n</i> matrix the definition of the determinant is as follows :

<pre>det(<b>A</b>) = <b>SIGMA</b> (±)a<sub>1j<sub>1</sub></sub> a<sub>2j<sub>2</sub></sub>. . .a<sub>nj<sub>n</sub></sub></pre>

Where <b>SIGMA</b> is our summation over all permutations j<sub>1</sub> j<sub>2</sub> ... j<sub>n</sub> of the set <b>S</b>={1, 2, ..., n }. 
      
The sign is + or - according to whether the permutation is even or odd.</p>

<b>Example:</b> In our 3x3 case it is a little easier, and boils down to : 

<pre>det(<b>A</b>) = aei + cdh + bfg - ceg - bdi - afh </pre>

Where are matrix first row is a b c , 2nd row d e f, and 3rd row, g h i


<b>Calculation Technique:</b> For the <i>n</i> x <i>n</i> the calculation of the determinant, by definition, is based upon a factorial number of calculations with respect to the size of the matrix. ie. a 3x3 matrix would have 6 calculations (3!) to make, whereas a 20x20 matrix would have 2.43 x 10^18 calculations (20!). 

So instead of brute forcing the calculations, I first do some operations on the matrix, which converts it to a upper triangular matrix, and then calculate the determinant by multiplying down the diagonal, since everything below is 0, this will give the determinant.

<hr>

<dt>adj(<b>A</b>)</dt>
<dd>The <b>adjoint</b> of <b>A</b> is the transpose of the matrix whose <i>i</i>th, and <i>j</i>th element is the cofactor A<sub>ij</sub> of the <i>a</i><sub>ij</sub> element from matrix <b>A</b>.<p>The <b>cofactor</b> of an element <i>a</i><sub>ij</sub> from matrix <b>A</b> is : <br>

<pre>
  <i>a</i><sub>ij</sub> = (-1)<sup>i + j</sup> * det (<b>A'</b>), where <b>A'</b> is the matrix obtained from &quot;omitting&quot; the ith and jth rows, of matrix <b>A</b>.
</pre>

<hr>

<dt> inv(<b>A</b>) </dt>
<dd>The <b>inverse</b> of <b>A</b> is the matrix which when multiplied to <b>A</b> returns the identity matrix. </dd>

<b>Calculation Technique:</b> The inverse was obtained using the Theorem:

<pre><b>A</b>adj(<b>A</b>) = det(<b>A</b>)I<sub>n</sub></pre>

Which when manipulated gives you: 

<pre><b>A</b><sup>-1</sup> = (1 / det(<b>A</b>)) * adj(<b>A</b>)</pre>

