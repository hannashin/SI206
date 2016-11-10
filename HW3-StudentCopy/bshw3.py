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
import requests 


link = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html_link = urlopen(link).read() #opening the link

soup1 = BeautifulSoup(html_link, 'html.parser')

#html life
file1 = str(soup1)


#replacing every word student with AMAZING student

# for words in soup1.find_all(class_="menu"):
# 	if words.a:
# 		print (words.text.replace("student", "AMAZING student"))

# for words in soup1.find_all(class_="field-item even"):
# 	if words.p: #each paragraph
# 		print (words.text.replace('student', 'AMAZING student'))


stringfile1= file1.replace('student', 'AMAZING student') #step 1
stringfile2 = stringfile1.replace('logo2.png', 'media/logo.png') #step 3
stringfile3 = stringfile2.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'media/me.png') #image of myself in media folder


#lol si 106
direct_file = "bshw3.html"
d = open(direct_file, 'w')
d.write(stringfile3)
d.close()



# for pics in soup1.find_all(class='field-item even'):
# 	if pics.get('src'):
# 		pics.get('src').replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'media/me.png')
