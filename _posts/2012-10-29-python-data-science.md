---
id: 670
title: Python Data Science
author: Marcus Kazmierczak
layout: post
permalink: /2012/10/29/python-data-science/
categories:
  - python
tags:
  - data science
---
My notes, resources and examples using Python, NumPy, SciPy and Matplotlib as alternatives to R and Matlab for data science and analysis.

### Load Data from Text File

```
import pylab
filename = "cool_data.dat"

# use skiprows if your data file has headers
data = pylab.loadtxt(filename, skiprows=1)
```

An example loading comma delimited data using Numpy:

```
import numpy as np
data = np.loadtxt(open('comma_delim.csv'), delimiter=",")
```

### Plotting and Graphing

#### Log Scale

```
import math
import matplotlib.pyplot as pyplot

X = list(xrange(1,25))
Y= []
for i in X:
    Y.append(math.pow(10, i))
pyplot.xlim(0,25)
pyplot.ylim(max(Y))
pyplot.yscale('log')
pyplot.plot(X,Y)
```

#### Labels for Titles and Axes

```
import matplotlib.pyplot as pyplot
import pylab
X = pylab.np.random.normal(0,1,500)
Y = pylab.np.random.normal(0,1,500)
pyplot.scatter(X,Y)
pyplot.title("Scatter Plot Example")
pyplot.xlabel("X-Axis")
pyplot.ylabel("Y-Axis")
```

#### Saving a Graph

The following will create a png image 648&#215;432 pixels. Note, you most likely will want to keep the dpi set to 72 since this has a direct effect on the font sizes in the rendered image

```
import pylab
... setup of data ...

# figure size in inches
pylab.rcParams['figure.figsize'] =  9, 6
pylab.plot(X,Y)
pylab.savefig("graph.png", dpi=72) # dots per inch
```

### Installing NumPy, SciPy and Matplotlib on OS X

I had a little trouble with the initial setup of some of the key libraries used for machine learning, stats and data science.

Here's what worked for me, to install on Mac OS X, the key was to not use the built-in python, download the binary from [python.org][1]. Secondly, make sure you set your environment variables to use this binary.

The symlinks to the python binaries were put in `/usr/local/bin`

The actual binaries are installed in `/Library/Frameworks/Python.framework/Versions/3.3/bin`

You need to install `gfortran` as a prerequisite, which I did using [Homebrew][2]  
brew install gfortran

If you are still using Python 2.7, pip install works fine, make sure the pip you are using is for the binary you installed, and not the base system. Most likely should be /usr/local/bin/pip and not /usr/bin/pip

```
$ pip install numpy
$ pip install scipy
$ pip install matplotlib
```

If you are using Python 3.3, which I have switched to and have had no problems using once installed, it seems the pip libraries aren't as up-to-date or require the latest code, so I checked out from source and built

```
$ git clone https://github.com/numpy/numpy.git
$ cd numpy
$ python setup.py install

$ git clone https://github.com/scipy/scipy.git
$ cd scipy
$ python setup.py install

$ git clone https://github.com/matplotlib/matplotlib.git
$ cd matplotlib
$ python setup.py install
```

## Resources

  * [NumPy for Matlab Users][3]
  * [Matplotlib Tutorial][4]
  * [Formating Strings with Python][5] (ebeab)

 [1]: http://python.org/download/
 [2]: http://brew.sh/
 [3]: http://wiki.scipy.org/NumPy_for_Matlab_Users
 [4]: http://www.loria.fr/~rougier/teaching/matplotlib/
 [5]: http://ebeab.com/2012/10/10/python-string-format/
