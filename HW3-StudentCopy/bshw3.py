# Use http://collemc.people.si.umich.edu/data/bshw3StarterFile.html
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

from urllib.request import urlopen
from bs4 import BeautifulSoup

link = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html_link = urlopen(link).read() #opening the link

soup1 = BeautifulSoup(html_link, 'html.parser')

#html life
file_link = "bshw3.html"
x = open(file_link, 'w')
x.write(soup1.prettify())
x.close()

#replacing every word student with AMAZING student
for words in soup1.find_all(class_="field-item even"):
	if words.p:
		words.text.replace('student', 'AMAZING student')


#replacing main picture with a picture of myself
#need to put image in seperate folder (how?)