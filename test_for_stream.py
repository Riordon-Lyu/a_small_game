import pandas as pd 
import numpy as np 
import streamlit as st 
import time

st.write('This is my app!')

st.write('''
# hello world!
this is my first app. Although I don\'t know the function of it for now, but it's would be a first small step that leads me into the internet world!
''')

x=st.slider('x')

y=x+100

y

a=st.button('时间显示装置')

tm=time.time()

tm=time.localtime(tm)

tm=time.strftime('%Y年%m月%d日 %H:%M:%S',tm)

st.write(tm)

title = st.text_input('Movie title', 'Life of Brian')

if title=='Life of Brian':
    st.write('The current movie title is', title)
else:
    st.write('')

st.write('# 以下显示进度条')

n=st.number_input('请输入完成进度情况（%）',0,100)
my_bar = st.progress(n)

b=st.button('放气球！')
if b:
    st.balloons()

list=[1,2,3]
    
option = st.sidebar.selectbox('Which number do you like best?',list)

if option==2:
    st.balloons()
    '你选择了正确的选项',option
    st.slider('y')













