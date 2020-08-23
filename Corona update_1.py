#!/usr/bin/env python
# coding: utf-8

# # Desktop Notifier for COVID-19

# In[1]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[7]:


header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers = header)
html = urlopen(req)


# In[8]:


html.status


# In[9]:


obj = bs(html, feature='lxml')


# In[15]:


new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]


# In[22]:


death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]


# ### Notifier

# In[23]:


notifier = ToastNotifier()


# In[24]:


message  = "New Cases - "+ new_cases+"\nDeath - "+death


# In[25]:


message


# In[26]:


notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path=r"virus.ico")
