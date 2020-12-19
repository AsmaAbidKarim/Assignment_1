#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def get_filepaths(directory):
    file_paths = []  
    for root, directories, folders in os.walk(directory):
        for files in folders:
            file_path = os.path.join(root, files)
            file_paths.append(file_path)  
            ##print(file_path)     
    return file_paths  # Self-explanatory.
def file_Size(file):
    file_stats = os.stat(file)
    a=file_stats.st_size
    return a
def Arrange(file_paths):
    for i in range(len(file_paths)):
        for j in range(len(file_paths)):
            if(file_Size(file_paths[i])>file_Size(file_paths[j])):
                temp=file_paths[j]
                file_paths[j]=file_paths[i]
                file_paths[i]=temp
    return file_paths
        
    
    
Path=""
# Run the above function and store its results in a variable. 
Path =input("Enter the path.....")
full_file_paths = get_filepaths(Path)
print("""-------------------------Files before sorting-----------------------""")
for i in range(len(full_file_paths)):
    print(full_file_paths[i],"\n")
full_path=Arrange(full_file_paths)
print("""\n----------------------files in descending order of their respective sizes--------------\n""")
for i in range(len(full_file_paths)):
    print(full_path[i],"\n")


# In[6]:


import requests
from bs4 import BeautifulSoup
import os
URL="https://www.facebook.com/"
Handle="Enter the handle"
list_likes=["Likes"]
list_Handles=["Handle"]
def print_likes_Handles():
    for i in range(len(list_likes)):
        print(list_Handles[i],"       ||     ",list_likes[i],"\n")
while(URL!=""):
    Handle=input("Enter The URL Or Press Enter To terminate....https://www.facebook.com/")
    URL= URL+Handle
    if(Handle!=""):
        response=requests.get(URL)
        str=response.content.decode()
        soup = BeautifulSoup(str,'lxml')
        ##The likes are in span tag inside class "_4-u3 _5sqi _5sqk
        f= soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
        likes=f.find('span',attrs={'class':'_52id _50f5 _50f7'}) 
        #finding span tag inside class
        ##lik=str(likes)
        list_Handle = os.path.join(Handle)
        list_Handles.append(list_Handle)
        list_like = os.path.join(likes.text)
        list_likes.append(list_like)
        print(likes.text)
        print_likes_Handles()
        URL="https://www.facebook.com/"
    
    else:
        break
    
    


# In[ ]:




