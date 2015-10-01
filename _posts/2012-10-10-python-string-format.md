---
id: 677
title: Python String Format Cookbook
author: Marcus Kazmierczak
layout: post
permalink: /2012/10/10/python-string-format/
categories:
  - python
tags:
  - string format
---
Every time I use Python's string formatter, version 2.7 and up, I get it wrong and for the life of me I can't figure out their documentation format. I got very used to the older % method. So I started to create my own string format cookbook. Let me know in the comments of any other good example to include.

## String Formatting Cookbook

### Number Formatting

The following table shows various ways to format numbers using python's *newish* str.format(), examples for both float formatting and integers.

To run examples use ` print("FORMAT".format(NUMBER)); `
So to get the output of the first example, you would run: ` print("{:.2f}".format(3.1415926));`

<table>
<tr><th> Number </th><th> Format </th><th> Output </th><th> Description </th></tr>
<tr><td> 3.1415926  </td><td> {:.2f}  </td><td> 3.14  </td><td> 2 decimal places </td></tr>
<tr><td> 3.1415926  </td><td> {:+.2f} </td><td> +3.14 </td><td> 2 decimal places with sign </td></tr>
<tr><td> -1         </td><td> {:+.2f} </td><td> -1.00 </td><td> 2 decimal places with sign </td></tr>
<tr><td> 2.71828    </td><td> {:.0f}  </td><td> 3   </td><td> No decimal places </td></tr>
<tr><td> 5          </td><td> {:0>2d} </td><td> 05  </td><td> Pad number with zeros (left padding, width 2) </td></tr>
<tr><td> 5          </td><td> {:x<4d} </td><td> 5xxx  </td><td> Pad number with x's (right padding, width 4) </td></tr>
<tr><td> 10         </td><td> {:x<4d} </td><td> 10xx  </td><td> Pad number with x's (right padding, width 4) </td></tr>
<tr><td> 1000000    </td><td> {:,}    </td><td> 1,000,000  </td><td> Number format with comma separator </td></tr>
<tr><td> 0.25       </td><td> {:.2%}  </td><td> 25.00%  </td><td> Format percentage </td></tr>
<tr><td> 1000000000 </td><td> {:.2e}  </td><td> 1.00e+09 </td><td> Exponent notation </td></tr>
<tr><td> 13         </td><td> {:10d}  </td><td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13 </td><td> Right aligned (default, width 10) </td></tr>
<tr><td> 13         </td><td> {:<10d} </td><td> 13 </td><td> Left aligned (width 10) </td></tr>
<tr><td> 13         </td><td> {:^10d} </td><td> &nbsp;&nbsp;&nbsp;&nbsp;13 </td><td> Center aligned (width 10) </td></tr>
</table>

## string.format() basics

Here are a couple of example of basic string substitution, the `{}` is the placeholder for the substituted variables. If no format is specified, it will insert and format as a string.

```python
s1 = "so much depends upon {}".format("a red wheel barrow")
s2 = "glazed with {} water beside the {} chickens".format("rain", "white")
```

You can also use the numeric position of the variables and change them in the strings, this gives some flexibility when doing the formatting, if you made a mistake in the order you can easily correct without shuffling all variables around.

```python
s1 = " {0} is better than {1} ".format("emacs", "vim")
s2 = " {1} is better than {0} ".format("emacs", "vim")
```

## Older ""%" string formatter

Prior to python 2.6, the way to format strings tended to be a bit simpler, though limited with the number of arguments it can receive. These methods still work as of Python 3.3, but there are veiled threats of deprecating them completely though no time table. [[PEP-3101][1]]

### Formating a floating point number:

```python
pi = 3.14159
print(" pi = %1.2f " % pi)
```

### Multiple Substitution Values

```python
s1 = "cats"
s2 = "dogs"
s3 = " %s and %s living together" % (s1, s2)
```

### Not Enough Arguments

Using the older format method, I would often get the error &#8220;TypeError: not enough arguments for format string" because I miscounted my substitution, do something like the following made it easy to miss a variable.

```python
set = " (%s, %s, %s, %s, %s, %s, %s, %s) " % (a,b,c,d,e,f,g,h,i)
```

The new python string formatter you can use numbered parameters so you don't have to count how many you have, at least on half of it.

```python
set = " ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}) ".format(a,b,c,d,e,f,g)
```

## More String Formatting with .format()

The format() function offers a fair amount of additional features and capabilities, here are a few useful tips and tricks using .format()

### Named Arguments

You can use the new string format as a templating engine and use named arguments, instead of requiring a strict order.

```python
madlib = " I {verb} the {object} off the {place} ".format(verb="took", object="cheese", place="table")
~~ I took the cheese off the table
```

### Reuse Same Variable Multiple Times

Using the % formatter, requires a strict ordering of variables, the .format() method allows you to put them in any order as we saw above in the basics, but also allows for reuse.

```python
str = "Oh {0}, {0}! wherefore art thou {0}?".format("Romeo")
~~ Oh Romeo, Romeo! wherefore art thou Romeo?
```

### Convert Values to different Bases

You can use the following letters to convert a number to their bases, <b>d</b>ecimal, he<b>x</b>, <b>o</b>ctal, <b>b</b>inary

```python
print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))
~~ 21 - 15 - 25 - 10101
```


### Use Format as a Function

You can use .format as a function which allows for some separation of text and formatting from code. For example at the beginning of your program you could include all your formats and then use later. This also could be a nice way to handle internationalization which not only requires different text but often requires different formats for numbers.

```python
## defining formats
email_f = "Your email address was {email}".format

## use elsewhere
print(email_f(email="bob@example.com"))
```

Hat tip to [earthboundkids][2] who provided this on reddit.

### Escaping Braces

If you need to use braces when using str.format(), just double up

```python
print(" The {} set is often represented as {% raw %}{{0}}{% endraw %}".format("empty"))
~~ The empty set is often represented as {0}
```

### Reference

  * [Python String Library][3] &#8211; Standard Library Documentation
  * [Python Essential Reference][4] &#8211; book on Amazon
  * My [Python Argparse Cookbook][5] &#8211; a similar cookbook for parsing command-line arguments

 [1]: http://www.python.org/dev/peps/pep-3101/
 [2]: http://www.reddit.com/r/Python/comments/174e1i/python_string_format_cookbook/c82ot0h
 [3]: http://docs.python.org/3/library/string.html
 [4]: http://www.amazon.com/gp/product/0672329786/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0672329786&linkCode=as2&tag=mkazcom-20
 [5]: /2014/07/26/python-argparse-cookbook/
