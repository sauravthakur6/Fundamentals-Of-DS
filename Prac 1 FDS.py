#!/usr/bin/env python
# coding: utf-8

# # Practical 1: Data Collection ,Modelling,Compilation

# In[5]:


my_dict={'name':["Saurav","Suraj","Chatainya"],"age":[21,22,23],"dept":["DSAI","IT","CS"]}
import pandas as pd
import numpy as np
df=pd.DataFrame(my_dict)
df


# In[6]:


df.to_csv("Csv Example")
df


# In[9]:


df=pd.read_csv("Csv Example")
df


# In[10]:


student=pd.read_csv("student-mat.csv - student-mat.csv.csv")   


# In[11]:


student.head()


# In[12]:


name=["Saurav","Nishant","Vikram","Suraj","Shyam"]
grades=[76,96,75,99,43]
bscdegrees=[0,1,1,1,1]
mscdegrees=[0,0,1,1,0]
phddegrees=[0,0,0,0,1]
Degrees=zip(name,grades,bscdegrees,mscdegrees,phddegrees)
columns=['Names','Grades',"Bsc",'Msc','Phd']
df=pd.DataFrame(data=Degrees,columns=columns)
df


# In[13]:


grade=pd.read_csv("gradedata - gradedata.csv.csv")
grade.head()


# In[20]:


name=["Saurav","Nishant","Vikram","Suraj","Shyam"]
grades=[7,8,9,9,1]
Gradelist=zip(name,grades)
df=pd.DataFrame(Gradelist,columns=["Names","Grades"])
writer=pd.ExcelWriter('dataframe.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name="Sheet1")
writer.save()


# Load data from sqllite

# In[6]:


import sqlite3
df=sqlite3.connect("portal_mammals.sqlite")
cur=df.cursor()
for row in cur.execute('SELECT * FROM species;'):
    print(row)
df.close()


# In[9]:


import pandas as pd
import sqlite3
con=sqlite3.connect("portal_mammals.sqlite")
df=pd.read_sql_query("SELECT * from surveys",con)
print(df.head())
con.close()


# In[13]:


#saving data
from pandas import DataFrame
Cars={'Brand':['Maruti',"Honda","Ferari","Benz"] ,'Price':[22000,21110,540001,60000]}
df=DataFrame(Cars,columns=['Brand',"Price"])
print(df)


# In[15]:


import sqlite3
conn=sqlite3.connect('testDB1.db')
c=conn.cursor()


# In[16]:


c.execute('CREATE TABLE CARS(Brand text,Price number)')
conn.commit()


# In[17]:


df.to_sql('CARS',conn,if_exists='replace',index=False)
df


# In[20]:


c.execute('''
SELECT Brand,max(Price) from CARS
''')


# In[21]:


df=DataFrame(c.fetchall(),columns=['Brand','Price'])
df


# # EXAMPLE1

# In[23]:


import pandas as pd
import os
import sqlite3 as lite
from sqlalchemy import create_engine


# In[1]:


studentId=['rj1','rj2','rj3','rj4']
sname=['Saurav',"Suraj","Chaitanya","Himansh"]
lname=["thakur","gupta",'sakariya',"kohli"]
dept=["bsc","msc","kuchbhi","ds"]
email=["bla@gmail.com","ok@gmail.com","thik@gmail.com","hmm@gmail.com"]


# studata=zip(studentId,sname,lname,dept,email)

# In[27]:


df=pd.DataFrame(data=studata,columns=['studentId','sname','lname','dept','email'])
df


# In[28]:


df1=df.to_csv('studentdata.csv',index=False,header=True)
df1


# In[29]:


df2=df.to_excel('studentdata2.xlsx',index=False,header=True)
df2


# In[30]:


db_filename=r'studentdata.db'
con=lite.connect(db_filename)
df.to_sql('student',
         con,
         schema=None,
         if_exists='replace',
         index=True,
         index_label=None,
         chunksize=None,
         dtype=None)
con.close()


# In[31]:


db_file=r'studentdata.db'
engine=create_engine(r"sqlite:///{}".format(db_file))
sql='SELECT * from student'

studf=pd.read_sql(sql,engine)
studf


# In[33]:


#Data PreProcessing
import numpy as np
import pandas as pd


# In[34]:


state=pd.read_csv("US_violent_crime.csv - US_violent_crime.csv.csv")
state.head()


# In[35]:


def some_func(x):
    return x*2
state.apply(some_func) #0r
state.apply(lambda n: n*2)


# In[36]:


state.transform(func=lambda x: x*10)


# In[38]:


mean_purchase=state.groupby('State')["Murder"].mean().rename("User_mean").reset_index()
print(mean_purchase)


# In[39]:


mer=state.merge(mean_purchase)
mer


# In[40]:


print(state.isnull().sum())


# # EXAMPLE2

# In[3]:


import pandas as pd
import numpy as np
cols=['col0','col1','col2','col3','col4']
rows=['row0','row1','row2','row3','row4']
data=np.random.randint(0,100,size=(5,5))
df=pd.DataFrame(data,columns=cols,index=rows)
df.head()


# In[4]:


df.iloc[4,2]


# In[5]:


#dealing with 0 and nan
df.iloc[3,3]=0
df.iloc[1,2]=np.nan
df.iloc[4,0]=np.nan
df['col5']=0
df['col6']=np.nan
df.head()


# In[6]:


df.loc[:,df.all()]


# In[8]:


df.loc[:,df.any()]


# In[10]:


df.loc[:,df.isnull().any()]


# In[12]:


df.loc[:,df.notnull().all()]


# In[13]:


df.dropna(how="all",axis=1)


# In[15]:


df.fillna(df.max())


# In[16]:


df.fillna(df.sum())


# In[18]:


def fn(n):
    return n+50
df.apply(fn)


# In[19]:


df['new_col']=df['col3'].apply(lambda n: n*2)


# In[20]:


df


# In[23]:


import pandas as pd
import numpy as np
df=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=["a","b","c"])


# In[24]:


df


# In[25]:


df.apply(lambda n:n*10)


# In[28]:


import pandas as pd
import numpy as np
import random
data=pd.DataFrame({
    "C":[random.choice(("a","b","c")) for i in range(1000000)],
    "A":[random.randint(1,10)for i in range (1000000)],
    "B":[random.randint(1,10)for i in range(1000000)]
})
data


# In[31]:


v=data.groupby('C')["A"].mean().rename("D").reset_index()
v


# In[33]:


df_1=data.merge(v)
df_1


# In[42]:


import pandas as pd
import numpy as np
airline=pd.read_csv("airline_stats.csv - airline_stats.csv.csv")
airline.head()


# In[43]:


airline.isnull().sum()


# In[44]:


df=airline.fillna(airline.mean(),inplace=True)
df


# In[45]:


airline.isnull().sum()


# In[47]:


z=airline.groupby("pct_atc_delay")["pct_weather_delay"].mean().rename("user").reset_index()


# In[48]:


z


# In[49]:


airline.merge(z)


# In[51]:


z.apply(lambda x:x*2)


# In[ ]:




