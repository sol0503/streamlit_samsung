import streamlit as st

st.markdown(
    """
    <div class='k'>
        <img src='http://localhost:8501/media/2c939973072ed174b7a579456f57f47a2a8fbdaa87139812c4f4e00a.png' alt='chat.png'/>
        <h3 style='margin-top: 10px;'>디지털 기술2조</h3>
    </div>
    """,
    unsafe_allow_html=True
)
# st.image("chat.png") 
# st.write('### 디지털 기술2조')

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# 사용자 입력에 따라 응답을 생성하는 함수
def generate_response(input_text):
    # 적절한 응답 생성 로직을 구현합니다.
    response = "안녕하세요! 입력한 메시지는: " + input_text
    return response

# Streamlit 애플리케이션 설정

user_input = st.text_input("궁금하신 점을 입력해보세요!", "s")

if st.button("전송"):
    response = generate_response(user_input)
    st.text("응답:")
    st.text(response)