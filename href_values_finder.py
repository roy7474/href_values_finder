
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
'''
The program will use urllib to read the HTML from the data files below, 
extract the href= vaues from the anchor tags, scan for a tag that is in a 
particular position relative to the first name in the list, follow that link 
and repeat the process a number of times and report the last name you find.

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this
 process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Owain.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this 
process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: S
Strategy
The web pages tweak the height between the links and hide the page after a few 
seconds to make it difficult for you to do the assignment without writing a 
Python program. But frankly with a little effort and patience you can overcome 
these attempts to make it a little harder to complete the assignment without 
writing a Python program. But that is not the point. The point is to write a 
clever Python program to solve the program.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #input('Enter - ')
# iterations = input('Please enter the number of iterations or how many times you would like to repeat this process: ')
iterations = 4

# This function extracts the link from the url

while 0 < iterations:
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links_lst = []

# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        links_lst.append(tag.get('href'))
    link_desired = links_lst[2] 
    pattern = r'by_([A-Za-z]+)'                  # Pattern before last name
    last_name = re.findall(pattern, link_desired)
    print(link_desired)
    

#print the last name without quotation marks
    for item in last_name:
        print(item)
    url = link_desired
    iterations -= 1




