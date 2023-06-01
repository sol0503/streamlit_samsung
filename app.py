import streamlit as st

st.markdown(
    """
    <div class='k'>
        <img src='https://www.figma.com/file/y2yBdvsnj1mXCqkbz6bS8U/Aria-Chat-Bot-%7C-Case-Study-(Community)?type=design&node-id=213-113&t=efeYi6V9u7UScXZl-4' alt='chat'/>
        <h3 style='margin-top: 10px;'>삼성증권 챗봇이</h3>
    </div>
    """,
    unsafe_allow_html=True
)
# st.image("chat.png") 
# st.write(' 디지털 기술2조')


with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)



# 커스텀 레이아웃 생성
my_container1 =  st.container()

# 이미지 표시
my_container1.image("chat.png", "안녕하세요!")
my_container1.image("chat.png", "어떤것을 알고 싶으신가요?")





# 사용자 입력에 따라 응답을 생성하는 함수
def generate_response(input_text):
    # 적절한 응답 생성 로직을 구현합니다.
    response = input_text
    return my_container1.image("person.png", response)





user_input = st.text_input("", "")

if st.button("전송"):
    response = generate_response(user_input)
