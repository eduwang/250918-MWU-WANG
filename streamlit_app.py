# Streamlit 예시 앱
import streamlit as st

st.title("Streamlit 요소 데모")

st.header("1. 텍스트와 마크다운")
st.write("이것은 write 함수로 출력한 텍스트입니다.")
st.markdown("**마크다운** _스타일링_도 지원합니다!")

st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=20)
agree = st.checkbox("동의합니다")

st.header("3. 버튼과 상호작용")
if st.button("인사하기"):
    st.success(f"안녕하세요, {name if name else '익명'}님! 나이: {age}")

st.header("4. 선택 위젯")
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "초록", "파랑"])
st.write(f"선택한 색: {color}")

st.header("5. 슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"슬라이더 값: {value}")

st.header("6. 데이터프레임")
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)

st.header("7. 차트")
st.line_chart(df)

st.header("8. 파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("업로드된 파일 이름:", uploaded_file.name)

st.header("9. 사이드바")
st.sidebar.title("사이드바 예시")
sidebar_option = st.sidebar.radio("옵션 선택", ["옵션1", "옵션2"])
st.sidebar.write(f"선택: {sidebar_option}")
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
