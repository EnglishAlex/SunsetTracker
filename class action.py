#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, time, timedelta
# test out classes
class DayTest:
    def __init__(self,sunrise,sunset):
        self.sunrise = datetime.strptime(sunrise,'%H:%M')
        self.sunset = datetime.strptime(sunset,'%H:%M')
        self.length = self.sunset - self.sunrise
    def daylength(self):
        '''length of day in printable string'''
        h,m = divmod((daytest.length.seconds/60),60)
        return '{:d}h{:d}m'.format(int(h),int(m))
    
    def timetosunset(self):
        '''printable string of hours and minutes to sunset'''    
        now = datetime.strftime(datetime.now(),'%H:%M')
        now = datetime.strptime(now,'%H:%M')
        ttss = self.sunset - now
        h,m = divmod((ttss.seconds/60),60)
        return '{:d}h{:d}m'.format(int(h),int(m))
    
    def sunelevation(self):
        '''reports sun elevation'''    
#         zero at sunrise prorated to solar noon 
        now = datetime.strftime(datetime.now(),'%H:%M')
        now = datetime.strptime(now,'%H:%M')

    def sunebearing(self):
        '''reports sun's bearing'''    
#       difference of two bearings pro-rated 
        now = datetime.strftime(datetime.now(),'%H:%M')
        now = datetime.strptime(now,'%H:%M')

    


# In[2]:


daytest = DayTest('08:15','17:20')


# In[3]:


daytest.timetosunset()


# In[4]:


daytest.daylength()


# In[5]:


help(DayTest)


# In[ ]:


coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)


# In[ ]:


h,m = divmod(daytest.length.seconds/60,60)

#print(f'{0:d}h{0:d}m'.format(h,m))

