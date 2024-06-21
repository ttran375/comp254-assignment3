# Lab Assignment #3 – Using Recursion

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ttran375/comp254-assignment3/blob/main/src/notebook.ipynb)

Purpose: The purpose of this Lab assignment is to:

- Design recursive algorithms

- Implement recursive methods in Java or Python

References: Read the course’s text chapter 5 and the lecture slides.
This material provides the necessary information that you need to
complete the exercises.

## Exercise 1

**If your first name starts with a letter from A-J inclusively:**

Create a **recursive algorithm** to compute the **product of two
positive integers**, *m* and *n*, using only addition and subtraction.
Implement the Java or Python code. **Hint:** You need subtraction to
count down from *m* or *n* and addition to do the arithmetic needed to
get the right answer. Check *linearSum* method from Week 5 examples.

**If your first name starts with a letter from K-Z inclusively:**

Write a recursive method to produce the following pattern:

```
*
**
***
****
***
**
*
```

Test the method by asking the user to enter the number of asterisks of
the maximum line (for example, the user should enter 4 in this case).

(3 marks)

## Exercise 2

**If your first name starts with a letter from A-J inclusively:**

Write a short **recursive Java method** that determines if a string s is
a palindrome, that is, it is equal to its reverse. Examples of
palindromes include 'racecar' and 'mom'. Test the method by asking the
user to provide string entries to be checked. **Hint:** Check the
equality of the first and last characters and recur (but be careful to
return the correct value for both odd and even-length strings).

**If your first name starts with a letter from K-Z inclusively:**

Write **a recursive method** to that returns the number of vowels in a
string. Test the method by asking the user to enter a string. **Hint**:
create a special method for checking if a character is a vowel.

(3 marks)

## Exercise 3

**If your first name starts with a letter from A-J inclusively:**

Write **a recursive method** that takes a string as argument and
determines if the string has more vowels than consonants. Test the
method by asking the user to enter a string. **Hint**: Write your
recursive method to first count vowels and consonants.

**If your first name starts with a letter from K-Z inclusively:**

Implement a **recursive method** that takes *(path, filename)* as
arguments and returns all entries of the file system rooted at the given
*path* having the given *file name*. Test the method with a real path,
filename from your file system. **Hint**: Review use of the
*java.io.File* class and the week 5 examples.

(4 marks)

## Appendix

`linear_sum.py`:

```python
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
```

`disk_usage.py`:

```python
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def disk_usage(path):
  """Return the number of bytes used by a file/folder and any descendents."""
  total = os.path.getsize(path)                  # account for direct usage
  if os.path.isdir(path):                        # if this is a directory,
    for filename in os.listdir(path):            # then for each child:
      childpath = os.path.join(path, filename)   # compose full path to child
      total += disk_usage(childpath)             # add child's usage to total

  print ('{0:<7}'.format(total), path)           # descriptive output (optional)
  return total                                   # return the grand total
```
