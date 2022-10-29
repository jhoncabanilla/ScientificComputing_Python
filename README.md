# ScientificComputing_Python

Python fundamentals like variables, loops, conditionals and functions to complex data structures, networking, relational databases and data visualization.

[Python for Everybody - Full University Python Course](https://www.youtube.com/watch?v=8DvywoWv6fI)

## Content
- Networking
- Web Services
- Python Objects
- Relational Databases


## Web Services
The two most common ways to send data over the Internet are: JSON and XML.

### XML (eXtensible Markup Language)
- Primary purpose is to help information systems share structured data.
- **Tags** indicate the beginning and ending of elements.
- **Attributes** - Keyword/value pairs on the opening tag of XML.
- **Serialize / De-Serialize** - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independet manner.

### JSON (JavaScript Object Notation)
- JSON represents data as nested "lists" and "dictionaries"

### API (Applicaton Program Interface)
- The API itself is largely abstract in that it specifies an interface and controls the behavior of the objects specified in that interface. The software that provides the funcionality described by an API is said to be an 'implementation' of the API. An API is typically defined in terms of the programming language used to build an application.


## Python Objects
- An object is a bit of self-contained Code and Data
- A key aspect of the Object approach is to break the problem into smaller understandable parts (divide and conquer)
-  Objects have boundaries that allow us to ignore un-needed detail
-  **String Objects, Integer Objects, Dictionary Objects, List Objects**, ...

### Definitions
- Class - a template
- Method - A defined capability of a class
- Attribute - A bit of data in a class
- Object or Instance - A particular instance of a class

### Inheritance
- When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class
- Another form of store and reuse
- Write once - reuse many times
- The new class (child) has all the capabilities of the old class (father) - and then some more



## Relational Databases
### Terminology
- **Database** - contains many tables
- **Relation (or Table)** - contains tuples and attributes
- **Tuple (or Row)** - a set of fields that generally represents an 'object' like a person or a music track
- **Attribute (or Columns / Field)** - one of possibly many elements of data corresponding to the object represented by the row

### SQL
- Structured Query Language is the language we use to issue commands to the database
- Create a table
- Retrieve some data
- Insert data
- Delete data

### Representing Relationships in a Database - Three Kinds of Keys
- **Primary key** - generally an integer auto-increment field
- **Logical key** - what the outside world uses for lookup
- **Foreign key** - generally an integer key pointing to a row in another table



