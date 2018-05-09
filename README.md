python-edu-search-system
===
Exercise: Create a Python script that searches the file system for text the user passes in as a paramater.

Setup
---
Using the command line, navigate to the root of this project.  Run the following command:
```bash
pip install -e .[dev]
```
Let's quickly walk through what this means because the Python packaging world is dark and full of terrors:

`pip` is the package manager for Python used to pull in packaged up code.

`install -e` installs with editable flag.  Normally when you `pip install package` the package is stored in your `site-packages` directory, but by using `-e` we'er telling Python to always load this package from the project instead of `site-packages`.  

`.[dev]` When we say `pip install .` pip will search the current directory for a file named `setup.py`.  Python packages are able to maintain multiple sets of requirements, commonly used for splitting out runtime requirements and development requirements, defined in `setup.py`.  


Acceptance Criteria
---
* Must accept the following params
    * String we are searching for
    * List of file types to check
* Able to find multiple matches
* It should print the following information:
    * Matching line content
    * Matching line number
    * Character position in line
    
Tests 
---
Run tests by running:
```bash
pytest
```