#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Oscar A
# DATE CREATED: 9/12/2020                            
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import re

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = {}
    for filename in listdir(image_dir):
        if not ignore_file(filename):
            value = results_dic.get(filename, [])
            value.append(get_pet_label(filename))
            results_dic[filename] = value
    
    return results_dic

def get_pet_label(image_filename):
    """
    Takes a valid image filename and removes the file extension first (e.g. .txt, .jpg)
    and proceeds to remove underscores and digits. The remaining words are joined with
    a space in between and made all lower case.
    Parameters:
     image_filename - valid image filename (assumes that files starting with . are ignored
                   prior to calling this function)
    Returns:
     (string) - a string containing an all lower case label. If multiple words were 
                   encountered the string will contain one space in between
    """
    without_file_extension = image_filename.lower().split(".")[0]
    return " ".join(filter(lambda s: len(s) > 0, re.split('[0-9]+|_+', without_file_extension)))

def ignore_file(filename):
    """
    Contains any logic to be used to ignore the processing of a file name
    Parameters:
      filename - a string containing the file name to be processed
      
    Returns:
      boolean - True if current file name should be ignored for processing; False otherwise
    """
    return filename[0] == '.'

    
