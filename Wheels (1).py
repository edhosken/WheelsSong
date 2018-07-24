
# coding: utf-8

# In[3]:


#START


# In[4]:


print ("Let's sing the wheels song!")


# In[6]:

#Placeholder for an exit function
variation = ''
while variation != "q" or "quit":
    variation = input ("Please input what variation you wish to perform be entering 'numbers' 'letters' 'numerals' phonetic' or 'q' to quit")

    if variation == 'q' or 'quit':
        break

        #This is pretty useless currently as it only breaks the while loop then continues.  
        #Ideally, the subsequent code would be moved to modules so the active code would all fit into a shorter while loop.


# In[29]:

#User input to select the song pattern
pattern = input ("Now please tell me what pattern to use by entering 'forward', 'backward', 'even', or 'odd'")
print ('OK, here we go:')


# In[8]:


#User input to set the pattern using immutable tuples since changes are not desired


# In[9]:

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)


# In[10]:


letters = ('a ','b ','c ','d ','e ','f ','g ','h ','i ','j ','k ','l ','m ','n ','o ','p ','q ','r ')


# In[11]:


numerals = ('I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII')


# In[12]:


phonetic = ('alpha, bravo, charlie, delta, echo, foxtrot, golf, hotel, india, juliet, kilo, lima, mike, november, oscar, papa, quebec, romeo')


# In[13]:


t = 'dot'
s = 'dash'
m1 = t, s, s, s, s
m2 = t, t, s, s, s
m3 = t, t, t, s, s
m4 = t, t, t, t, s
m5 = t, t, t, t, t
m6 = s, t, t, t, t
m7 = s, s, t, t, t
m8 = s, s, s, t, t
m9 = s, s, s, s, t
m0 = s, s, s, s, s
morse = (m1, m2, m3, m4, m5, m6, m7, m8, m9, m1 + m0, m1 + m1, m1 + m2, m1 + m3, m1 + m4, m1 + m5, m1 + m6, m1 + m7, m1 + m8)


# In[14]:


german = ('eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn')


# In[15]:


pi = (3,'.',1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2)


# In[ ]:


#Now to create a function to print the desired then the variation and pattern to see if it works.
#Instead of printing, what is really needed is to set the value of a new object so it can then be displayed in the final assembled song.
#Assembled order should be modified var (forward, backward, skipping first or second)

# In[31]:


if pattern == 'forward':
    print (variation)
elif pattern == 'backward':
    print (variation)[::-1]
elif pattern == 'even':
    print (variation) [1::]
#Even function could just pop the first item then could be 2

#Asemble the song


# In[ ]:


song1 = "Oh, there are "
varpat = "PLACEHOLDER" 
song2 = " wheels on a big rig truck!"
print (song1, varpat, song2)

# In[ ]:

#Repeat until user quits

