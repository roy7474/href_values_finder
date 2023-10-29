
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
url = input('Enter the url: ') #  
iterations = int(input('Enter the number of iterations: '))
url_position = int(input('Enter the position of the link that you need: '))
# This function extracts the link from the url
last_name= []
while 0 < (iterations + 1):   # +1 since I need to extract the first last name
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links_lst = []

# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        links_lst.append(tag.get('href'))
    link_desired = links_lst[url_position - 1]              # extract the link
    pattern = r'by_([A-Za-z]+)'                             # Pattern before last name
    # Add last name to the list
    last_name.append(re.findall(pattern, url))
    url = link_desired
    iterations -= 1

# print the last name without quotation marks
for names in last_name:
    for name in names:
        print(name)




