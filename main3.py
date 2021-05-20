import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('２カラムレイアウト')

#２カラムレイアウト
left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('これは右カラム')

# Expander

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')  

expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')  

expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')  



# text = st.text_input('貴方の趣味を教えて下さい。')
# condition = st.slider('貴方の今の調子は？',0,100,50) 

# '貴方の趣味は、',text
# 'コンディション',condition

