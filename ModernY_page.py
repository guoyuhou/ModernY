import streamlit as st
import time
import os
st.title(':blue[ModernY] :sunglasses:')
def stream_data(text):
    for word in text.split(' '):
        yield word + ' '
        time.sleep(0.02)
text = '''Welcome! This web is created by Alexander. It is used to store something useful 
        and share my life. I am happy that you could access this web! And I hope that 
        this web can be useful for you!'''


if st.button('Click here!'):
    st.write_stream(stream_data(text))

st.write('__Welcome! This app is created by Alexander which named ModernY, the left'
         'siderbar contains more content about the app__')
