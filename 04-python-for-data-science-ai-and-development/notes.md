# PYTHON FOR DATA SCIENCE, AI, AND DEVELOPMENT

## Table of Contents
1. [Module 1: ](#module-1)
2. [Module 2: ](#module-2)
3. [Module 3: ](#module-3)
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


