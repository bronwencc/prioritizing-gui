# Code copyright 2021 by Github user bronwencc
#import python packages
import easygui_qt as eg
import csv
import numpy as np
import os, sys

#code in this repository:
import file_ops
import combine
import comparing


def increm(val): #simple add-one function
    #change to 1 if val is null
    if val == None:
        return 1
    else: #otherwise, increment by 1
        return val+1


def main():
    #use existing data or enter input
    useprior = eg.get_yes_or_no("Are you using data from an existing CSV file?")
    datadict = {}
    if useprior==True: #if Yes
        filepath, datalists = file_ops.getfile()
        for datalist in datalists: #nested for loops are O^2!
            for data in datalist:  #look into reducing
                datadict[data]=[0,[],[]]#number of times chosen, items that were chosen over it,
    #items that it was chosen over
    else: #answered No (or closed window or hit Cancel); get information through input
        data=""
        while data!=None:
            data = eg.get_string("Please enter one item at a time. Hit Cancel after submitting the last item.")
            if data==None:
                break
            else:
                datadict[data]=[0,[],[]]#number of times chosen, items that were chosen over it,
    #items that it was chosen over

    if len(datadict)<=1: #if only one item in the dictionary or no items
        eg.show_message(f"There was only one item: {datadict}") #show the datadict contents as result
        sys.exit("Exiting program.") #end program
    else: #make list of items to combine into pairs
        combos_list = combine.combos(list(datadict.keys())) #sends list of keys, the default returned is pairs (combinations of 2's)
        for combo in combos_list:#compare options
            #first check for items in common using dictionary info
            #to logically infer relationship
            if len(combo)==2:#to be sure each combo is only two items
                info0 = datadict[combo[0]]
                info1 = datadict[combo[1]]
                relation = comparing.infer(info0,info1)
                
                if relation == None: #ask user for input on comparison
                    chosen_option = eg.get_one_choice(choices = combo) #may at some point return only the index number instead of complete text from combo directly
                    #and then would rely on using the index number to get the item name/string
                    if chosen_option==combo[0]:
                        #other_option is set to the other of the pair
                        other_option = combo[1]
                    elif chosen_option==combo[1]:
                        other_option = combo[0]
                    else:
                        sys.exit("Exiting program")

                elif relation==True:#then combo[0] should rank higher
                    chosen_option = combo[0]
                    other_option = combo[1]
                else: #relation is False, combo[1] should rank higher
                    chosen_option = combo[1]
                    other_option = combo[0]    
                #get information from datadict
                total_c,above_c,below_c = datadict[chosen_option]
                total_o,above_o,below_o = datadict[other_option]
                eg.show_message(f"chosen {chosen_option}: {above_c}{below_c} <br> <br> other {other_option}: {above_o}{below_o}")
                
                #update datadict appropriately
                below_c.append(other_option) #other_option ranks below chosen_option
                datadict[chosen_option] = [increm(total_c),above_c,below_c]
                
                above_o.append(chosen_option) #chosen_option ranks above other_option
                datadict[other_option] = [total_o,above_o,below_o]
        #end combo frequency loop
        eg.show_message(str(datadict)) #show message box with entire dictionary
        
        file_ops.savelist(datadict.keys()) #write datadict keys to csv file
        
        #put keys in list in order based on totals (highest value first)
        sortedlist = sorted(datadict.items(), key = lambda keyval: keyval[1][0], reverse=True)
        file_ops.savecsv(sortedlist)#write sortedlist of datadict items to file
        
# main function call
if __name__=="__main__":     
    main()