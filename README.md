# Prioritizing Repo

I wrote this code to rank items by providing a pop-up comparing two strings and asking the user to pick one. I envisioned using message boxes to return the input. In remembering tkinter could be useful, I found [EasyGUI_Qt](https://easygui-qt.readthedocs.io/en/latest/api.html) based on Tkinter and created by user [aroberge](https://github.com/aroberge/easygui_qt), who was inspired by EasyGUI (created by Stephen Ferg).

The code was written to take in .CSV files or allow for one-by-one user input with input message boxes.

## Contents
This repository contains the code in a few `.py` Python files, written with version 3.8+. It also has two folders, one for saving a list of given or existing items and the other for saving the prioritizing ranking results as a .CSV file.

### Python files
There is one main Python file `prioritize.py` that relies on methods contained in other Python files.

#### `prioritize.py`
This contains the main method with code asking for inputting data, asking for input by looping through combination pairs, displaying the results as a dictionary, and saving to files.

#### `file_ops.py`
This contains the function `getfile` which brings up a file-picker and then reads in the given file with the `csv` Python package to a list of lists. The function returns the file path and the list resulting from being read in.
The functions `savecsv` and `savelist` are also in this file, both of which prompt for a file name (expected to include .csv extension) and use csv writer to save the provided list. The former `savecsv` saves a list of lists-type of data with each list on a new line. The latter `savelist` saves a list-type in one line.

#### `comparing.py`
This contains a function `comparelists` to find items in common between two lists. This function is used in the method `infer` which compares four lists to draw a conclusion that one item associated with one pair of lists would be chosen over the item associated with the other pair of lists.

#### `combine.py`
This contains the function `combos` which uses `itertools.combinations` to return a list of combinations of the given size (or defaults to 2) from a given array-like.

### Folders
#### item-lists
This folder is where sample priority-ranking input data is stored.
#### results
This folder contains the sample output dictionaries converted to lists, then saved as .CSV files.