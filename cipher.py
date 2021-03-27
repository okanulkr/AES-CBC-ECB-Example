#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from Cryptodome.Cipher import AES
from Cryptodome import Random
import pandas
import argparse


# In[8]:


# getting image path from command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f")
parser.add_argument("-i", default="photo.jpg")
args = parser.parse_args()


# In[3]:


image = img.imread(args.i)


# In[4]:


#converting image to string to be encrypted
image_as_array = np.asarray(image, dtype=int)
msg = image_as_array.tostring()


# In[5]:


#Encryption (ECB)
key = "CENG474SECRETKEY".encode("utf-8")
cipher_ecb = AES.new(key, AES.MODE_ECB)
msg_ecb = cipher_ecb.encrypt(msg)


# In[6]:


#Encryption (CBC)
IV = Random.new().read(AES.block_size)
cipher_cbc = AES.new(key, AES.MODE_CBC, IV)
msg_cbc = cipher_cbc.encrypt(msg)


# In[7]:


# rearranging the ecb-encrypted image
msg_ecb = np.frombuffer(msg_ecb,dtype=int)
msg_ecb = np.asarray(msg_ecb, dtype=np.float32)
msg_ecb = msg_ecb.reshape(image.shape)
msg_ecb = (msg_ecb).astype(np.uint8)

# rearranging the cbc-encrypted image
msg_cbc = np.frombuffer(msg_cbc,dtype=int)
msg_cbc = np.asarray(msg_cbc, dtype=np.float32)
msg_cbc = msg_cbc.reshape(image.shape)
msg_cbc = (msg_cbc).astype(np.uint8)

f, axarr = plt.subplots(1, 3, figsize=(20, 20))
axarr[0].set_title('Original')
axarr[0].imshow(image)
axarr[1].set_title('ECB Encrypted')
axarr[1].imshow(msg_ecb)
axarr[2].set_title('CBC Encrypted')
axarr[2].imshow(msg_cbc)
plt.show()

# In[ ]:




