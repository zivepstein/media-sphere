
# coding: utf-8

# In[1]:

import cv2


# In[2]:

vidcap = cv2.VideoCapture('sara-fulldome/A.mov')


# In[3]:

success,image = vidcap.read()


# In[5]:

count = 0;
while success:
    success,image = vidcap.read()
    cv2.imwrite("slice/sara-A/frame_%d.jpg" % count, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1


# In[24]:

count


# In[ ]:



