import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Sidebar')


#サイドバー

text = st.text_input('貴方の趣味を教えて下さい。')
condition = st.slider('貴方の今の調子は？',0,100,50) 

'貴方の趣味は、',text
'コンディション',condition

#２カラムレイアウト