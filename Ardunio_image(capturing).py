#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python opencv-python-headless


# In[2]:


import cv2
import numpy as np


# In[3]:


# Load image 
img = cv2.imread('image3.jpg')


# In[4]:


# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[5]:


# Apply GaussianBlur to Reduce noise and improve contour detection
blurred = cv2.GaussianBlur(gray, (5,5),0)


# In[6]:


# Apply Canny edges detection 
edges = cv2.Canny(blurred, 50, 150)


# In[7]:


# Find contours in the edges image 
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# In[8]:


# Filers contours based on area to identify potential vehicle regions
min_contour_area = 500
vehicle_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]


# In[9]:


# Draw contours on the original image 
cv2.drawContours(img, vehicle_contours, -1, (0, 225,0), 2)


# In[21]:


# Count vehicles 1
vehicle_count = len(vehicle_contours)


# In[ ]:


# Disply the result 
cv2.imshow("Image2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


# Print the vehicles count
print("Number of vehicles:", vehicle_count)


# In[ ]:




