from bs4 import BeautifulSoup
import requests

# Let's start with a simple html
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

##################
# TAGS
##################

title_obj = soup.title
print(title_obj)

# if there's more than one tag with the same name, the first one is called
h3_obj = soup.h3
print(h3_obj)

# we can navigate to the children and parents like this
h3_obj.b
h3_obj.b.parent  # same as the h3_obj

h3_obj.parent  # takes us to the <body> element

# <h3> and <p> are siblings
h3_obj.next_sibling  # outputs the <p> element

##################
# HTML ATTRIBUTES
##################
h3_child = h3_obj.b
h3_child.attrs  # is a dictionary
h3_child["id"]  # output: 'boldest'
h3_child.get("id")  # output: 'boldest'

h3_child.string
type(h3_child.string)  # bs4.element.NavigableString
unicode_string = str(h3_child.string)
type(unicode_string)  # str

##################
# FILTER
##################

table = "<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html.parser")
print(table_bs.prettify())

### .find_all(name, attrs, recursive, string, limit, **kwargs)

table_rows = table_bs.find_all("tr")
table_rows
type(table_rows)  # bs4.element.ResultSet
len(table_rows)  # 4

first_row = table_rows[0]
print(type(first_row))  # <class 'bs4.element.Tag'>

first_row.td

for i, row in enumerate(table_rows):
    print(f"Row {i} is {row}")

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")
    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
list_input
