import PyPDF2 as ppdf
import numpy as np
import datetime as dt
from textblob import TextBlob
import os
import pandas as pd

def getcontent(filename):
    pdf_file = open(filename, 'rb')
    read_pdf = ppdf.PdfFileReader(pdf_file)
    num_pages = read_pdf.getNumPages()
    file_text = ""
    for i in np.arange(num_pages):
        page = read_pdf.getPage(i)
        page_text = page.extractText()
        file_text = (file_text + page_text)
    content = file_text.split('\n')
    return(content)

def getnums(filename):
    pdf_file = open(filename, 'rb')
    read_pdf = ppdf.PdfFileReader(pdf_file)
    num_pages = read_pdf.getNumPages()
    return(num_pages)

def gettitle(filename):
    """
    Gets title of NYT article
    """
    content = getcontent(filename)
    return(content[0])

def getdate(filename):
    """
    Returns date of NYT article in [D,M,Y] format
    """
    content =getcontent(filename)
    counter = 0
    index = 0
    date_line = " "
    for i in content:
        if 'New York Times' in i and counter == 0:
            if 'Draft' in content[index+1]:
                date_line = content[index+2].split(" ")
            else:
                date_line = content[index+1].split(" ")
            counter = 1
        index = index+1
    date_str = date_line[1]
    date = int(date_str[:-1])

    month = 0
    if date_line[0]=='January':
        month = 1
    elif date_line[0]=='February':
        month = 2
    elif date_line[0]=='March':
        month = 3
    elif date_line[0]=='April':
        month = 4
    elif date_line[0]=='May':
        month = 5
    elif date_line[0]=='June':
        month = 6
    elif date_line[0]=='July':
        month = 7
    elif date_line[0]=='August':
        month = 8
    elif date_line[0]=='September':
        month = 9
    elif date_line[0]=='October':
        month = 10
    elif date_line[0]=='November':
        month = 11
    elif date_line[0]=='December':
        month = 12
        
    year = int(date_line[2])
    date_arr = [date,month,year]
    return(date_arr)

def getbody(filename):
    """
    Gets body content of NYT article
    """
    content = getcontent(filename)
    body_start = content.index('Body')
    text_after_body = content[body_start+1:]

    body_end = 0
    for i in np.arange(len(text_after_body)):
        if 'http' in text_after_body[i]:
            body_end = i
        else:
            body_end = len(text_after_body)

    clipped = text_after_body[:body_end]
    pagenums = getnums(filename)
    body_text = ""
    for i in np.arange(len(clipped)):
        if ("Page" in clipped[i]) == False and (("of "+str(pagenums)) in clipped[i]) == False:
            body_text = body_text + clipped[i]
    return(body_text)

#replace 'path' with the directory in which your NexisUni files are stored
files_folder = 'path'
file_names = os.listdir(files_folder)

titles = []
for file in file_names:
    try:
        titles.append(gettitle(files_folder+file))
    except:
        titles.append(np.nan)

dates = []
months = []
years = []
for file in file_names:
    try:
        d = getdate(files_folder+file)[0]
        m = getdate(files_folder+file)[1]
        y = getdate(files_folder+file)[2]
        dates.append(dt.datetime(y,m,d))
    except:
        dates.append(np.nan)

bodies = []
for file in file_names:
    try:
        bodies.append(getbody(files_folder+file))
    except:
        bodies.append(np.nan)



data = {'Article Title':titles,'Date':dates,'Text':bodies}
df = pd.DataFrame(data)
