import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('Data Frame')

#表

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40] 
})

st.dataframe(df.style.highlight_max(axis=0), width=300,height=400) 

st.table(df.style.highlight_max(axis=0)) 

#マジックコマンド

"""
# 章
## 節
### 項

```Python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#チャート

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#マップ  新宿付近

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.map(df)

#画像

from PIL import Image

st.write('Display Image')

img = Image.open('匡崇.png')
st.image(img,caption="匡崇",use_column_width=True)     # レイアウトに合わせる

#インターラクティブなウィジェット

#チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('匡崇.png')
    st.image(img,caption="匡崇",use_column_width=True)     # レイアウトに合わせる

#セレクトボックス
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)

'あなたが好きな数字は、',option,'です。'

#テキスト入力
st.write('Interactive Widget')

text = st.text_input('貴方の趣味を教えて下さい。')
'貴方の趣味は、',text

#スライダー
condition = st.slider('貴方の今の調子は？',0,100,50)     ※最小値、最大値、ディフォルト
'コンディション',condition