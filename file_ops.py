#methods to read in and save a .CSV file
import csv
import easygui_qt as eg

def getfile():
    #get CSV file name from file picker
    filepath, filetype = eg.get_file_name(title="Choose an existing CSV file")
    if filepath == None: #selected Cancel or message box was closed
        return None, None #exit the function and return None
    else:
    #try: #read in CSV file to list of lists
        readlist = []
        with open(filepath,'r') as f:
            reading = csv.reader(f)
            for row in reading:
                readlist.append(row)
    #except: # if not a CSV file
    #    eg.show_message(f"File does not appear to be in expected CSV format. Check file extension and try again.")
    #    return filepath, None #return input file name and null

    return filepath, readlist

def savecsv(listofitems):
    #requests name of file & directory to be saved to, must include extension
    savefilepath, filetype = eg.get_save_file_name()
    if savefilepath=='':#if window was closed or Cancel, does not save file
        return None
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        for each in listofitems:
            writer.writerow(each)
            
def savelist(listofitems):
    #requests name of file & directory to be saved to, must include extension
    savefilepath, filetype = eg.get_save_file_name()
    if savefilepath=='':#if window was closed or Cancel, does not save file
        return None
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        writer.writerow(listofitems)