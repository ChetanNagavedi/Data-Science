#!/usr/bin/env python
# coding: utf-8

# ## web scraping

# In[1]:


import bs4
import requests


# In[2]:


res = requests.get('https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_books_home_all?pf_rd_p=5616b610-d8a0-451b-8e54-f26322075cc4&pf_rd_s=center-1&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=SJR91585KFZ35HDHAK2T&pf_rd_r=SJR91585KFZ35HDHAK2T&pf_rd_p=5616b610-d8a0-451b-8e54-f26322075cc4')


# In[3]:


content = res.content


# In[4]:


soup = bs4.BeautifulSoup(content)


# In[5]:


complete_data =[]
for i in soup.findAll('div',attrs={'class' : 'a-section a-spacing-none aok-relative'}):
    book_name = i.find('a', attrs= {'class' : 'a-link-normal'})
    name = book_name.find_all('img', alt= True)
    author = i.find('div', attrs= {'class' : 'a-row a-size-small'})
    rating = i.find('span', attrs= {'class' : 'a-icon-alt'})
    no_rating = i.find('a', attrs={'class' : 'a-size-small a-link-normal'})
    price = i.find('span', attrs={'class' : 'a-size-base a-color-price'})
    
    myList =[]
    
    if name is not None:
        myList.append(name[0]['alt'])
    else:
        myList.append("Unknown")
        
    if author is not None:
        myList.append(author.text) 
    else:
        myList.append('No author found')
    
    if rating is not None:
        myList.append(rating.text)
    else:
        myList.append('No ratings')
        
    if no_rating is not None:
        myList.append(no_rating.text)
    else:
        myList.append('No ratings given')
        
    if price is not None:
        myList.append(price.text)
    else:
        myList.append('No price')
        
    print(myList)
    
    complete_data.append(myList)


# In[6]:


import pandas as pd
df = pd.DataFrame({"name": complete_data}) 
df


# In[7]:


df.to_csv("D:/Chetan/Python/Perceptrons/webscraping/amazon.csv")


# In[8]:


import numpy as np


# In[9]:


df =np.array(complete_data)
type(df)
df


# In[10]:


data = []
for list in df:
            
    data.append(list)

data


# In[11]:


final = pd.DataFrame(data)
final


# In[12]:


final.to_csv('Final')


# In[13]:


final.to_csv("D:/Chetan/Python/Perceptrons/webscraping/amazonFinal.csv")


# In[ ]:




