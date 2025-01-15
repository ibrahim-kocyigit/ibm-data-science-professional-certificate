# PYTHON FOR DATA SCIENCE, AI, AND DEVELOPMENT

## Table of Contents
1. [Module 1: Python Basics](#module-1)
2. [Module 2: Python Data Structures](#module-2)
3. [Module 3: Python Programming Fundamentals](#module-3)
4. [Module 4: ](#module-4)
5. [Module 4: ](#module-5)

# Module 1: Python Basics <a name="module-1"></a>

### Types
Python uses types to represent different kinds of data. Understanding types is crucial for working with data effectively.

**Common Data Types:**  
* Integers (`ìnt`): Whole numbers (e.g., 11, -5, 0). Python has a large but finite range for integers.
* Floating-Point Numbers (`float`): Real numbers with decimal points (e.g., 21.213, -3.14, 0.0). Floats have a high level of precision but are still limited by the computer's representation.
* Strings (`str`): Sequences of characters (e.g., "Hello", "Python", "123"). Used to represent text.
* Boolean Type (`bool`): Represents truth values, with only two possible values: True and False.


**Checking Data Types:** Use the `type()` function to determine the type of a variable or expression.

**Typecasting:** Converting data from one type to another.  
* int to float: No information is lost (e.g., 2 becomes 2.0).
* float to int: Can result in loss of information (e.g., 1.1 becomes 1).
* str to int or float: Possible if the string contains a valid numerical value.
* int or float to str: Converts the number into its string representation.

**Typecasting with Booleans:**  
* True is equivalent to 1 when cast to an integer or float.
* False is equivalent to 0.
* 1 casts to True, and 0 casts to False.

_Check the lab folder for more detail_

### Expressions and Variables

#### Expressions
Operations that Python performs to produce a result. These can include arithmetic operations, comparisons, and logical operations.

**Operators and Operands:**  
* Operands: The values or variables on which the operation is performed (e.g., numbers in an addition operation).
* Operators: The symbols that represent the operation (e.g., + for addition, - for subtraction, * for multiplication, / for division).

**Arithmetic Operations:**  
* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`): In Python 3, division always results in a float.
* Integer Division (`//`): Divides and rounds down to the nearest integer.

**Order of Operations:** Python follows mathematical conventions for the order of operations (PEMDAS/BODMAS).

#### Variables
Used to store values in Python.

* Assignment Operator (`=`): Used to assign a value to a variable.
* Variable Names: Should be meaningful and descriptive.

**Working with Variables:**  
* You can store the results of expressions in variables.
* You can perform operations on variables and store the results in new variables or update existing ones.
* The `type()` function can also be used with variables to check their data type.

_Check the lab folder for more detail_

### String Operations
**Strings as sequences:** In Python, strings are sequences of characters. This means they have an order, and you can access individual characters or substrings using their position (index) within the string.

#### Indexing
* **Positive Indexing:** Starts from 0 for the first character, 1 for the second, and so on.
* **Negative Indexing:** Start from -1 for the last character, -2 for the second-to-last, and so on.
* **Slicing:** Allows you to extract a portion of the string (e.g., `my_string[2:5]` extracts characters from index 2 to 4. --not 5!)
* **Striding:** Allows you to extract characters at regular intervals (e.g., `my_string[::2]` extracts every second character).

#### String Operations
* **Concatenation (`+`):** Combines two or more strings.
* **Replication (`*`):** Repeats a string a specified number of times.

**Immutability:** Strings are immutable, meaning you cannot change their characters in place. However, your can create new strings by modifying the existing ones.

**Escape sequences:** Special characters that are represented using a backslash (`\`).  
* `\n`: New line
* `\t`: Tab
* `\\`: Backslash

#### String Methods
Strings have built-in methods for various operations. For example:
* `upper()`: Converts the string to uppercase
* `replace()`: Replaces a substring with another string.
* `find()`: Returns the index of the first occurrence of a substring.

_Check the lab folder for more detail_

### Format Strings in Python

#### String interpolation (f-strings)
Introduced in Python 3.6, f-strings are a new way to format strings in Python. They are prefixed with 'f' and use curly braces {} to enclose the variables that will be formatted. For example:

> name = "John"  
> age = 30  
> print(f"My name is {name} and I am {age} years old.")  

f-strings are generally considered the most modern and preferred way to format strings in Python due to their readability and performance. They are also able to evaluate expressions inside the curly braces, which can be very handy. For example: 

> x = 10  
> y = 20  
> print(f"The sum of x and y is {x+y}.")  

#### str.format()
This is another way to format strings in Python. It uses curly braces `{}` as placeholders for variables which are passed as arguments in the `format()` method. For example:

> name = "John"  
> age = 50  
> print("My name is {} and I am {} years old.".format(name, age))  

#### % operator
This is one of the oldest ways to format strings in Python. It uses the `%` operator to replace variables in the string. For example:

> name = "John"  
> age = 50  
> print("My name is %s and I am %d years old." % (name, age))  

#### Raw String (r")
In Python, raw strings are a powerful tool for handling textual data, especially when dealing with escape characters. By prefixing a string literal with the letter 'r', Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences.

Consider the following examples:

> regular_string = "C:\new_folder\file.txt"  
> print("Regular String:", regular_string)  

This will output:

> Regular String:  C:   
> ew_folderile.txt   

In the regular string regular_string variable, the backslashes (\n) are interpreted as escape sequences. Therefore, \n represents a newline character, which would lead to an incorrect file path representation.

To solve this issue:

> raw_string = r"C:\new_folder\file.txt"  
> print("Raw String:", raw_string)  

This will output:

> Raw String: C:\new_folder\file.txt  

# Module 2: Python Data Structures <a name="module-2"></a>

### Lists and Tuples 

#### Tuples
* In Python, we often use tuples to group related data together.Tuples refer to ordered and immutable collections of elements.
* Tuples are usually written as comma-separated elements in parentheses “()".
* You can include strings, integers, and floats in tuples and access them using both positive and negative indices.
* You can perform operations such as combining, concatenating, and slicing on tuples.
* Tuples are immutable, so you need to create a new tuple to manipulate it.
* Tuples, termed nesting, can include other tuples of complex data types.
* You can access elements in a nested tuple through indexing.

_Check the lab folder for more detail_

#### Lists
* Lists in Python contain ordered collections of items that can hold elements of different types and are mutable, allowing for versatile data storage and manipulation.
* A list is an ordered sequence, represented with square brackets "[]".
* Lists possess mutability, rendering them akin to tuples.
* A list can contain strings, integers, and floats; you can nest lists within it.
* You can access each element in a list using both positive and negative indexing.
* Concatenating or appending a list will result in the modification of the same list.
* You can perform operations such as adding, deleting, splitting, and so forth on a list.
* You can separate elements in a list using delimiters.
* Aliasing occurs when multiple names refer to the same object.
* You can also clone a list to create another list.

_Check the lab folder for more detail_

### Dictionaries
* Dictionaries in Python are key-value pairs that provide a flexible way to store and retrieve data based on unique keys.
* Dictionaries consist of keys and values, both composed of string elements.
* You denote dictionaries using curly brackets.
* The keys necessitate immutability and uniqueness.
* The values may be either immutable or mutable, and they allow duplicates.
* You separate each key-value pair with a comma, and you can use color highlighting to make the key more visible.
* You can assign dictionaries to a variable.
* You use the key as an argument to retrieve the corresponding value.
* You can make additions and deletions to dictionaries.
* You can perform an operation on a dictionary to check the key, which results in a true or false output.
* You can apply methods to obtain a list of keys and values in a dictionary.

_Check the lab folder for more detail_

### Sets
* Sets in Python are collections of unique elements, useful for tasks such as removing duplicates and performing set operations like union and intersection. Sets lack order.
* Curly brackets "{}" are helpful for defining elements of a set.
* Sets do not contain duplicate items.
* A list passed through the set function generates a set containing unique elements.
* You use “Set Operations” to perform actions such as adding, removing, and verifying elements in a set.
* You can combine sets using the ampersand "&" operator to obtain the common elements from both sets.
* You can use the Union function to combine two sets, including both the common and unique elements from both sets.
* The sub-set method is used to determine if two or more sets are subsets.

_Check the lab folder for more detail_

# Module 3: Python Programming Fundamentals <a name="module-3"></a>

### Conditions and Branching

_Check the lab folder for more detail_

### Loops
