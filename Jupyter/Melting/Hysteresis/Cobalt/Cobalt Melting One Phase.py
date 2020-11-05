#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
##get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib widget
# sns.set()
plt.rcParams['figure.figsize'] = [11, 7]
# import mplcursors
# %matplotlib nbagg
# %pylab
# mplcursors.cursor(hover=True)
sns.set_style("white")


# In[39]:


# file_fcc =r"melt_Au.dat"
# file_bcc = r"AlBCC.dat"


# In[40]:


columns =['step', 'temp','press','vol','ke','pe','density']
columns_ = ['step', 'temp','press','vol','ke','pe','density','cpu','cpuremain']
# def last_4chars(x):
#     return(x[-4:])


# In[41]:


temp_heat = []; temp_cool =[]
vol_heat = []; vol_cool = []
for dirpath, dirnames, filenames in sorted(os.walk(os.getcwd())):
#     filenames.sort()
    for file in sorted(filenames, key = len):
            if file.endswith('.txt'):
                if file.startswith('one_phase_heating'):
#                     print(file)
#                 display(file)
                    df = pd.read_csv(file, header=None, skiprows = 1, delimiter ="\s+" , names = columns)
                    temp_heat.append(df.temp.mean())
                    vol_heat.append(df.vol.mean())
#                     display(df.describe())
                else:
#                     print(file)
#                     if file.startswith('cool'):
                    df = pd.read_csv(file, header=None, skiprows = 1, delimiter ="\s+")
                    if df.shape[1] == 7:
                        df.columns = columns
                    else: 
                        df.columns = columns_
                    temp_cool.append(df.temp.mean()) 
                    
                    vol_cool.append(df.vol.mean())
#                     display(df.describe())
# df_bcc = pd.read_csv(file_bcc, header=None, skiprows = 0, delimiter ="\s+" , names = columns)
# mn_row_fcc = df_fcc[df_fcc["Cohesive Energy"]==df_fcc["Cohesive Energy"].min()]
# mn_row_bcc = df_bcc[df_bcc["Cohesive Energy"]==df_bcc["Cohesive Energy"].min()]

# print(float(mn_row["a"]))
# print(df.loc[df[df["Cohesive Energy"]==df["Cohesive Energy"].min()].index]["a"])
# cor = df.index.value()
# print(cor)
temp_heat.sort()
temp_cool.sort()
vol_heat.sort()
vol_cool.sort()


# In[42]:


##display(*zip(temp_heat,vol_heat))


# In[43]:


##display(*zip(temp_cool,vol_cool))


# In[44]:


# temp.sort()
# vol.sort()
# %pylab
# print(temp)
plt.plot(temp_heat, vol_heat, color ="r", marker ="^", label="Heating")
plt.plot(temp_cool, vol_cool, color ="b", marker ="s",label="Cooling")
# plt.xlim([0,2800])
# plt.title('$Melting \;Temperature\; of\; Co=2100+1195-\sqrt{2100*1195} = 1710.86 K$')
# # plt.title(f'$\mu_P={df.iloc[df["Cohesive Energy"]]["a"]},E_c={df["Cohesive Energy"]}$')
# plt.xticks(range(0,2800,100),rotation=90)
plt.ylabel("Volume")
plt.xlabel("Temperature")
# plt.tight_layout()
plt.legend()

# plt.annotate()
# plt.annotate()
# # plt.xticks(rotation=90)
plt.annotate('$T_-=1195 \;K$', xy=(1200, 16650),xytext=(800, 17200),
            arrowprops=dict(arrowstyle="fancy",
#                              ec="none",
#                             patchB=el,
                            connectionstyle="angle3,angleA=0,angleB=-90",color="b"));
plt.annotate('$T_+=2097 \;K$', xy=(2100, 16880),xytext=(2250, 16100),
            arrowprops=dict(arrowstyle="fancy",
#                              ec="none",
#                             patchB=el,
                            connectionstyle="angle3,angleA=0,angleB=-90",color="r"));
# mplcursors.cursor(hover=True)
plt.savefig("melting.png",dpi=500)
plt.show()


# In[45]:


# df = df_bcc
# plt.plot(df["a"], df["Cohesive Energy"], label ="Cohesive Energy", color ="g", marker ="o")
# plt.title(f'$Aluminium[bcc], a={float(mn_row_bcc["a"])},E_c={df["Cohesive Energy"].min()}$')
# # plt.title(f'$\mu_P={df.iloc[df["Cohesive Energy"]]["a"]},E_c={df["Cohesive Energy"]}$')

# plt.ylabel("Cohesive Energy")
# plt.xlabel("Lattice Constant")
# plt.savefig("AlBCC.png",dpi=300)
# # plt.xticks(rotationb=90)
# plt.show()


# In[46]:


#  	step 	temp 	press 	vol 	ke 	pe 	density
# count 	1.010000e+02 	101.000000 	101.000000 	101.000000 	101.000000 	101.000000 	101.000000
# mean 	4.100000e+06 	1302.393436 	-183.712991 	8987.367005 	115.318082 	-2796.943455 	5.430793
# std 	2.930017e+04 	40.154300 	5236.967495 	48.009311 	3.555390 	5.238488 	0.029002
# min 	4.050000e+06 	1218.653332 	-14633.214207 	8869.623325 	107.903465 	-2811.858675 	5.355323
# 25% 	4.075000e+06 	1267.681441 	-3996.367876 	8956.064004 	112.244570 	-2800.528772 	5.409587
# 50% 	4.100000e+06 	1308.265188 	712.416964 	8983.987137 	115.837985 	-2798.144637 	5.432683
# 75% 	4.125000e+06 	1328.003546 	3406.694788 	9022.342655 	117.585683 	-2792.967146 	5.449621
# max 	4.150000e+06 	1397.815601 	13368.865296 	9113.764764 	123.767065 	-2783.157257 	5.502731


# In[ ]:





# In[ ]:




