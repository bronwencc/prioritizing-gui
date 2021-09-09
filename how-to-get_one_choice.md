The following code is instructions for using the `get_one_choice` method which can be added to the easygui_qt.py source file located in the easygui_qt directory or folder where easygui_qt is installed. In miniconda 3, the file path is ...miniconda3\Lib\site-packages\easygui_qt\.

Since you are modifying the easygui_qt code, you should be aware this is done under the same License as [the original](https://github.com/aroberge/easygui_qt/blob/master/LICENSE): a BSD 3-Clause "New" or "Revised" License which allows for modifications. Also, redistribution must retain the copyright notice and the names of the software nor the creators can be used to promote anything without "specific prior written permission".

First, in the `__all__` list, add the string: 'get_one_choice'.

Then in the #====InputDialogs====# or your preferred message box section, copy-paste the following function:

```def get_one_choice(message="Select one item", title="Pick one", choices=None):
    """Simple dialog to ask a user to select one of two options by clicking the appropriately labeled button.

       :param message: Message displayed to the user in the box
       :param title: Window title text
       :param choices: iterable (2-item list or tuple) containing two Strings; the two items that could be chosen

       >>> import easygui_qt as eg
       >>> choices = ["CPython","Jython"]
       >>> choice = easy.get_one_choice(message="Which is preferred?", choices=choices)
       
       :returns: the first item in choices or the second item in choices.
    """
    #This function was based on the get_choice, get_yes_or_no and get_continue_or_cancel methods
    if choices is None:
        choices = ["Item 1", "Item 2"]

    app = SimpleApp()

    #creates a QMessageBox with no icon (an icon would be a warning or question mark)
    #and with the title and message text
    box = qt_widgets.QMessageBox(qt_widgets.QMessageBox.NoIcon, title, message, qt_widgets.QMessageBox.NoButton)
    
    #"Accept" button and "Reject" button are added, labeled with the text from choices
    #Underlying the buttons are AcceptRole (first item in choices) and RejectRole buttons (second item in choices)
    box.addButton(choices[0], qt_widgets.QMessageBox.AcceptRole)
    box.addButton(choices[1], qt_widgets.QMessageBox.RejectRole)

    box.show()
    box.raise_()

    reply = box.exec_()
    app.quit()

    if reply==qt_widgets.QMessageBox.Cancel:
        return None
    elif reply == qt_widgets.QMessageBox.AcceptRole:
        return choices[0]
    else:
        return choices[1]```