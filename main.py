import streamlit as st
st.title('나의 찻 웹 서비스 만들기!')
name=st.text__input('이름을 입력해주세요!')
if st.button('인사말 생성'):
  st.write(name+'님! 안녕하세요')
