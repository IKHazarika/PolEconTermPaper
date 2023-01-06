#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sympy as sp
import numpy as np


# In[ ]:


#policy space [-1, 1]
#beliefs: uniformly distributed
#ideal points F: [-1, 1] -> [0, 1] -(x-1)(x+1)(cx+(0.2(3.75-c)), c is degree of polarisation
#affiliation A1: -p to -q, A2: r, s (to be randomly chosen)
#cost function uniform

#optimal policy: [(theta_bar - theta) * pi_i * E(x|i)] / [theta + (theta_bar - theta) * pi_i]


# In[55]:


ps = []
qs = []
rs = []
ss = []
cs = []
alpha1s = []
alpha2s = []
tubars = []
tlbars = []
xLs = []
xRs = []

for i in range(1000):
    
    #Distribution of affiliation
    p = np.random.uniform(-1, 0)
    q = np.random.uniform(p, 0)
    r = np.random.uniform(0, 1)
    s = np.random.uniform(r, 1)
    
    c = np.random.uniform(0, 3.75)
    
    alpha1 = np.random.uniform(0.1, 0.5)
    alpha2 = np.random.uniform(0.1, 0.5)
    
    tubar = np.random.uniform(0, 1)
    tlbar = np.random.uniform(0, tubar)
    
    pTemp = []
    qTemp = []
    rTemp = []
    sTemp = []
    xLTemp = []
    xRTemp = []
    
    for t in range(25):
        piL = (-0.75 + 0.2 *c) *p + (0.25 - 0.4 *c) *p**3 + 0.2 *c *p**5 + q *(0.75 - 0.25 *q**2 + c *(-0.2 + 0.4 *q**2 - 0.2 *q**4))
        piR = (-0.75 + 0.2 *c) *r + (0.25 - 0.4 *c) *r**3 + 0.2 *c *r**5 + s *(0.75 - 0.25 *s**2 + c *(-0.2 + 0.4 *s**2 - 0.2 *s**4))
        
        exL = (-0.375 + 0.1 *c) *p**2 + (0.1875 - 0.3 *c) *p**4 + 0.166667 *c *p**6 + q**2 *(0.375 - 0.1875 *q**2 + c *(-0.1 + 0.3 *q**2 - 0.166667 *q**4))
        exR = (-0.375 + 0.1 *c) *r**2 + (0.1875 - 0.3 *c) *r**4 + 0.166667 *c *r**6 + s**2 *(0.375 - 0.1875 *s**2 + c *(-0.1 + 0.3 *s**2 - 0.166667 *s**4))
        
        xL = ((tubar - tlbar) * piL * exL) / (tlbar + (tubar - tlbar)* piL)
        xR = ((tubar - tlbar) * piR * exR) / (tlbar + (tubar - tlbar)* piR)
        
        p = max(xL - alpha1, -1)
        q = min(xL + alpha1, 0)
        r = max(xR - alpha2, 0)
        s = min(xR + alpha2, 1)
        
        pTemp.append(p)
        qTemp.append(q)
        rTemp.append(r)
        sTemp.append(s)
        xLTemp.append(xL)
        xRTemp.append(xR)
        
    ps.append(pTemp)
    qs.append(qTemp)
    rs.append(rTemp)
    ss.append(sTemp)
    xLs.append(xLTemp)
    xRs.append(xRTemp)

    cs.append(c)
    alpha1s.append(alpha1)
    alpha2s.append(alpha2)
    tubars.append(tubar)
    tlbars.append(tlbar)


# In[36]:


import pandas as pd


# In[58]:


print(xLs[150])
print(cs[150])
print(alpha1s[150])
print(alpha2s[150])
print(ps[150])
print(qs[150])
print(tubars[150])
print(tlbars[150])


# In[ ]:


#To graph:
# xL, xR with time
# p, q, r, s with time

#Comparative statics
# With c, alpha, tubar, trbar how are xL, xR


# In[79]:


#To graph

#xLs, xRs, p, q, r, s

avxls = []
avxrs = []
avps = []
avqs = []
avrs = []
avss = []

for t in range(25):
    smxls = 0
    smxrs = 0
    smps = 0
    smqs = 0
    smrs = 0
    smss = 0
    
    for i in range(1000):
        smxls += xLs[i][t]
        smxrs += xRs[i][t]
        smps += ps[i][t]
        smqs += qs[i][t]
        smrs += rs[i][t]
        smss += ss[i][t]
    
    avxls.append(smxls/10)
    avxrs.append(smxrs/10)
    avps.append(smps/1000)
    avqs.append(smqs/1000)
    avrs.append(smrs/1000)
    avss.append(smss/1000)

avrgs = [avxls, avxrs, avps, avqs, avrs, avss]
avrgs = np.array(avrgs)
avrgs = avrgs.transpose()

dfTime = pd.DataFrame(avrgs, columns = ['LeftPolicy','RightPolicy','LLAf', 'LRAf', 'RLAf', 'RRAf'])
dfTime.to_csv('E:/Semester 3/Political Economics/Term paper/timeSeriesData.csv')
df


# In[80]:


#Comparative statics
# With c, alpha, tubar, trbar how are xL, xR, p, q, r, s

dataSet = []

for i in range(1000):
    rowData = []
    rowData.append(cs[i])
    rowData.append(alpha1s[i])
    rowData.append(alpha2s[i])
    rowData.append(tubars[i])
    rowData.append(tlbars[i])
    rowData.append(xLs[i][24])
    rowData.append(xRs[i][24])
    rowData.append(ps[i][24])
    rowData.append(qs[i][24])
    rowData.append(rs[i][24])
    rowData.append(ss[i][24])
    
    dataSet.append(rowData)

dfCS = pd.DataFrame(dataSet, columns = ['Polarisation','CostLevelL', 'CostLevelR','InfoA', 'InfoNA', 'LeftPolicy', 'RightPolicy', 'LLAf', 'LRAf', 'RLAf', 'RRAf'])
dfCS.to_csv('E:/Semester 3/Political Economics/Term paper/crossSectionData.csv')
df

