import pandas as pd
import os
from bs4 import BeautifulSoup
import csv
import xml
import re


def clean_html(html_file, isString):
    '''
    Receives the html file and removes unecessery parts, as header, footer, etc.
    '''

    # List of elements that are going to be removed from the html
    remove_list = ["head", "header", "footer" , "polygon", "path", "script",
                    "symbol", "meta", "link", "title", "style", "nav", "form"]
    remove_class = ["sidebar-inner","breadcrumb", "share", "navegacao",
                    "skiptranslate", "goog-te-spinner-pos","social-list",
                    "social-icon", "copyright", "id_assist_frame",
                    "fbc-badge-tooltip"]
    remove_id = ["boxes", "mySidenav", "chat-panel"]

    # Check if the html_file is a string with the page or a path to the file
    if not isString:
        soup = ""
        f = open(html_file, encoding="ISO-8859-1")
        soup = BeautifulSoup(f, 'html.parser')
        f.close()
    if isString:
        f = html_file
        soup = BeautifulSoup(f, 'html.parser')

    # Remove any tag present in remove_list
    for tag in soup.find_all():
        if tag.name.lower() in remove_list:
            tag.extract()
    # Remove any div with the class in remove_class
    for div in soup.find_all("div", {'class':remove_class}):
        div.extract()
    # Remove any div with the id in remove_id
    for div in soup.find_all("div", {'id':remove_id}):
        div.extract()

    html_file = str(soup)



    return html_file



def check_div(html_file):
    '''
    Receives a html file and returns booleans indicating if the content is in
    a table or div
    '''

    # Boolean variables to indicate if the content is in table or div format
    table_content = False
    div_content = False

    # List of elements that are going to be removed from the html
    table_tag = ["table"]
    div_tag = ["p", "h1", "h2", "h3"]

    # Open the string with BeautifulSoup
    f = html_file
    soup = BeautifulSoup(f, 'html.parser')

    # Check the remaining tags
    for tag in soup.find_all():
        if tag.name.lower() in table_tag:
            table_content = True
        elif tag.name.lower() in div_tag:
            div_content = True

    return table_content, div_content



def html_detect_content(html_file, output_file = None):
    '''
    Receives an html file path, converts the html to csv and saves the file on
    disk.

    :param html_file : str (A file-like object, or a raw string containing
    HTML.)
    :param output_file : str, optional (Name and path of the output csv file)
    '''

    # Check if html file exists
    if (os.path.isfile(html_file)):
        # Create output file based on the input file name
        output_file = html_file.split('.html')[0]+".csv"
        # set isString to false, since the HTML is in a html_file
        isString = False
    # Ckeck if the html was passed as string
    elif (' ' in html_file) and (len(html_file)>2):
        # If a name for the output is not given, the file is set to output.csv
        if output_path is None:
            output_file = "output.csv"
        # set isString to true, since the HTML is in a string
        isString = True
    # If the file does not exist and is not a raw string
    else:
        raise Exception('The given HMTL file does not exist.')

    # Clean the html file
    html_file = clean_html(html_file,isString)
    # Check the content
    table_content, div_content = check_div(html_file)
    # Call the indicated parsing
    if table_content:
        print('HAS A TABLE')
    else:
        print('NO TABLE')
    if div_content:
        print('HAS A DIV')
    else:
        print('NO DIV')
