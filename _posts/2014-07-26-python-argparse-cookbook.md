---
id: 3730
title: Python Argparse Cookbook
author: Marcus Kazmierczak
layout: post
permalink: /2014/07/26/python-argparse-cookbook/
categories:
  - python
tags:
  - arguments
  - command-line
---
I use Python as my go to tool for command-line scripts. So I find myself often parsing command-line arguments for these script. Since I use various programming languages I don't remember anything, so I'm constantly looking at documentation and sadly, Python docs are a bit challenging to read.

So, in a similar vein as my [Python String Format Cookbook][1], I wrote my own docs for argument parsing which I'll use myself as a reference and hopefully useful to you.

## What Library to Use

I don't know the history but there are a couple of different standard libraries that can be used for parsing arguments. The one you want to use is **argparse** module. Similiar in name to **optparse** which is the older deprecated module.

Also confusingly there is a **getopt** module which handles more or less the same parsing of command-line arguements but is a bit more complicated and usually requires more code to be written.

## Basic Example

First, up a simple example which is just grabbing a single argument and no flags or other parameters passed in. For this case, you can just use `sys.argv` array which contains all of the parameters passed in.

The first element in `sys.argv` is the script itself. So a parameter passed in will be in the second element: `sys.argv[1]`

<pre class="brush: python; title: ; notranslate" title="">import sys

if len(sys.argv) &gt; 1:
    print( "~ Script: " + sys.argv[0] )
    print( "~ Arg   : " + sys.argv[1] )
else:
    print(" No arguments ")
</pre>

Saving as `test.py` and running gives:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py Foo
~ Script: test.py
~ Arg   : Foo
</pre>

### Multiple Arguments with sys.argv

Since `sys.argv` is simply a list, you can grab blocks of arguments togther or slice around as you would any other list.

Last argument: `sys.argv[-1]`

All args after first: `" ".join(sys.argv[2:])`

## Flag Parameters

You need to start using a module when you want to start including flags such as `--help` or want to have optional arguments, or varying length parameters. As mentioned, the best standard module to use is **argparse**.

### Help and Verbose Examples

<pre class="brush: python; title: ; notranslate" title="">import argparse

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )

args = parser.parse_args()

if args.verbose:
    print("~ Verbose!")
else:
    print("~ Not so verbose")
</pre>

Here's how to run the above example:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py
~ Not so verbose

$ python test.py --verbose
~ Verbose!
</pre>

The action parameter tells argparse to store true if the flag is found, otherwise it stores false. Also a great thing about using `argparse` is you get built-in help. You can try it out by passing in an unknown parameter, `-h` or `--help`

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py --help
usage: test.py [-h] [--verbose]

Demo

optional arguments:
  -h, --help  show this help message and exit
    --verbose   verbose output
</pre>

A side effect of using argparse, you will get an error if a user passes in a command-line argument not expected, this includes flags or just an extra argument.

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py filename
usage: test.py [-h] [--verbose]
test.py: error: unrecognized arguments: filename
</pre>

### Multiple, Short or Long Flags

You can specify multiple flags for one argument, typically this is down with short and long flags, such as `--verbose` and `-v`

<pre class="brush: python; title: ; notranslate" title="">import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v',
    action='store_true',
    help='verbose flag' )

args = parser.parse_args()

if args.verbose:
    print("~ Verbose!")
else:
    print("~ Not so verbose")
</pre>

### Required Flags

You can make a flag required by setting, `required=True` this will cause an error if the flag is not specified

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('--limit', required=True, type=int)
args = parser.parse_args()
</pre>

## Positional Arguments

The examples so far have been about flags, parameters starting with `--`, argparse also handles the positional args which are just specified without the flag. Here's an example to illustrate.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

print("~ Filename: {}".format(args.filename))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py filename.txt
~ Filename: filename.txt
</pre>

## Number of Arguments

Argparse determines the number of argument based on the action specified, for our verbose example, the store_true action takes no arguments. By default, argparse will look for a single argument, shown above in the filename example.

If you want your parameter to accept a list of items you can specify `nargs=n` for how many arguments to accept.

<pre class="brush: python; title: ; notranslate" title="">import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs=2)
args = parser.parse_args()

print("~ Nums: {}".format(args.nums))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py 5 2
~ Nums: ['5', '2']
</pre>

### Variable Number of Parameters

The nargs argument accepts a couple of extra special parameters. If you want the argument to accept all of the parameters, you can use `*` which will return all parameters if present, or empty list if none.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs='*')
args = parser.parse_args()

print("~ Nums: {}".format(args.nums))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py 5 2 4
~ Nums: ['5', '2', '4']
</pre>

If you want to require, 1 or more parameters, use `nargs='+'`

Positional arguments are determine by the position specified. This can be combined with the `nargs='*'` for example if you want to define a filename and a list of values to store.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('nums', nargs='*')
args = parser.parse_args()

print("~ Filename: {}".format(args.filename))
print("~ Nums: {}".format(args.nums))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py file.txt 5 2 4
~ Fileanme: file.txt
~ Nums: ['5', '2', '4']
</pre>

You can also specify `nargs='?'` if you want to make a positional argument optional, but you need to be careful how you combine ? and * parameters, especially if you put an optional positional parameter before another one.

This makes sense, not requiring the last args:

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('nums', nargs='?')
args = parser.parse_args()
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py test.txt 3
~ Filename: test.txt
~ Nums: 3

$ python test.py test.txt
~ Filename: test.txt
~ Nums: None
</pre>

However, using the `nargs='?'` first will give unexpected results when arguments are missing, for example:

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='?')
parser.add_argument('nums', nargs='*')
args = parser.parse_args()
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py 3 2 1
~ Filename: 3
~ Nums: ['2', '1']
</pre>

You can use `nargs` with flag arguments as well

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('--geo', nargs=2)
parser.add_argument('--pos', nargs=2)
parser.add_argument('type')
args = parser.parse_args()
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py --geo 5 10 --pos 100 50 square
~ Geo: ['5', '10']
~ Pos: ['100', '50']
~ Type: square
</pre>

## Variable Type

You might notice that the parameters passed in are being treated like strings and not numbers, you can specify the variable type by specifying `type=int`. By specifying the type, argparse will also fail if an invalid type is passed in.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('nums', nargs=2, type=int)
args = parser.parse_args()

print("~ Nums: {}".format(args.nums))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py 5 2
~ Nums: [5, 2]
</pre>

### File Types

Argparse has some built in filetypes which makes it easier to open files specified on the command line. Here's an example reading a file, you can do the same writing a file.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('f', type=argparse.FileType('r'))
args = parser.parse_args()

for line in args.f:
    print( line.strip() )
</pre>

## Default Value

You may specify a default value if the user does not pass one in. Here's an example using a flag.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('--limit', default=5, type=int)
args = parser.parse_args()

print("~ Limit: {}".format(args.limit))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py
~ Limit: 5
</pre>

## Remainder

If want to gather the extra arguments passed in, you can use remainder which gathers up all arguments not specified into a list

<pre class="brush: python; title: ; notranslate" title="">import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )
parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args()

print(args.args)
</pre>

Specifying remainder will create a list of all remaining arguments:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py --verbose foo bar
['foo', 'bar']
</pre>

## Actions

The default action is to assign the variable specified, but there are a couple of other actions that can be specified.

### Booleans

We have already seen the boolean flag action which is `action='store_true'` which also has a counter action for `action='store_false'`

### Count

You can use the count action, which will return how many times a flag was called, this can be useful for verbosity or silent flags

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')
args = parser.parse_args()

print("~ Verbose: {}".format(args.verbose))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py
~ Verbose: None

$ python test.py --verbose
~ Verbose: 1

$ python test.py --verbose -v --verbose
~ Verbose: 3
</pre>

### Append

You can also use the append action to create a list if multiple flags are passed in.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser()
parser.add_argument('-c', action='append')
args = parser.parse_args()

print("~ C: {}".format(args.c))
</pre>

Output:

<pre class="brush: plain; title: ; notranslate" title="">$ python test.py
~ C: None

$ python test.py -c hi
~ C: ['hi']

$ python test.py -c hi -c hello -c hey
~ C: ['hi', 'hello', 'hey']
</pre>

## Choices

If you only want a set of allowed values to be used, you can set the choices list, which will display an error if invalid entry.

<pre class="brush: python; title: ; notranslate" title="">parser = argparse.ArgumentParser(prog='roshambo.py')
parser.add_argument('throw', choices=['rock', 'paper', 'scissors'])
args = parser.parse_args()

print("~ Throw: {}".format(args.throw))
</pre>

## Examples

I'll end with two examples, many of the example above are not as complete I would use in reality, they were kept short to focus on the idea being illustrated.

### Copy Script Example

<pre class="brush: python; title: ; notranslate" title="">import argparse
import sys

parser = argparse.ArgumentParser(description='script to copy one file to another')

parser.add_argument('-v', '--verbose',
    action="store_true",
    help="verbose output" )

parser.add_argument('-R',
    action="store_false",
    help="Copy all files and directories recursively")

parser.add_argument('infile',
    type=argparse.FileType('r'),
    help="file to be copied")

parser.add_argument('outfile',
    type=argparse.FileType('w'),
    help="file to be created")

args = parser.parse_args()
</pre>

### Bug Script Example

Here is an example for a script that closes a bug

<pre class="brush: python; title: ; notranslate" title="">import argparse
import sys

parser = argparse.ArgumentParser(description='close bug')

parser.add_argument('-v', '--verbose',
    action="store_true",
    help="verbose output" )

parser.add_argument('-s',
    default="closed",
    choices=['closed', 'wontfix', 'notabug'],
    help="bug status")

parser.add_argument('bugnum',
    type=int,
    help="Bug number to be closed")

parser.add_argument('message',
    nargs='*',
    help="optional message")

args = parser.parse_args()

print("~ Bug Num: {}".format(args.bugnum))
print("~ Verbose: {}".format(args.verbose))
print("~ Status : {}".format(arg.s))
print("~ Message: {}".format(" ".join(args.message)))
</pre>

## Resources

  * [Official Argparse Documentation][2] &#8211; the official documentation is more complete, there are even more options to the module than I showed.

  * [Official Argparse Tutorial][3] &#8211; More examples and the official walk through on using argparse.

  * See my [Python String Format Cookbook][1] for a similar tutorial with regards to string formatting

 [1]: https://mkaz.com/2012/10/10/python-string-format/
 [2]: https://docs.python.org/dev/library/argparse.html
 [3]: https://docs.python.org/2/howto/argparse.html
