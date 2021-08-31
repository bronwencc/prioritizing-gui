# Prioritizing Repo

I wrote this code to rank items by providing a pop-up comparing two strings and asking the user to pick one. I envisioned using message boxes to return the input. In remembering tkinter could be useful, I found [EasyGUI_Qt](https://easygui-qt.readthedocs.io/en/latest/api.html) based on Tkinter and created by user [aroberge](https://github.com/aroberge/easygui_qt), who was inspired by EasyGUI (created by Stephen Ferg).

The code was written to take in .CSV files or allow for one-by-one user input with input message boxes.

## Contents
This repository contains the code in a few `.py` Python files, written with version 3.8+. It also has two folders, one for saving a list of given or existing items and the other for saving the prioritizing ranking results as a .CSV file.

### Python files
I wanted to try a more modular style of importing necessary functions from other files, so there is one main Python file relying on methods contained in others.
#### `prioritize.py`
This contains the main method and code doing the bulk of the work asking for input, looping through combination pairs, making logical comparisons and saving the results to a file.

#### `readfile.py`
This contains the function `getfile` which brings up a file-picker and then reads in the given file with the `csv` Python package to a list of lists. The function returns the file path and the list resulting from being read in.

#### `combine.py`
This contains the function `combos` which uses `itertools.combinations` to return a list of combinations of the given size (or defaults to 2) from a given array-like.

### Folders
#### data-lists
This folder is where sample priority-ranking input data is stored.
#### freq-dicts
This folder contains the sample output dictionaries converted to dataframes, then saved as .CSV files.