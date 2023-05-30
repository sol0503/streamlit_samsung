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

# # 텍스트 입력 필드 추가
# text_input = my_container.text_input("텍스트 입력")

# 이미지 표시
my_container1.image("chat.png", "안녕하세요!")
my_container1.image("chat.png", "어떤것을 알고 싶으신가요?")




# # 사용자 입력에 따라 응답을 생성하는 함수
# def generate_response(input_text):
#     # 적절한 응답 생성 로직을 구현합니다.
#     response = "안녕하세요! 입력한 메시지는: " + input_text
#     return response

# # Streamlit 애플리케이션 설정

# my_container2 = st.container()

# with my_container2:
#     user_input = st.text_input("", "")


# with my_container2:
#     if st.button("전송"):
#         response = generate_response(user_input)
#         st.text("응답:")
#         st.text(response)

# # 컨테이너 1에 대한 스타일을 적용하는 CSS 클래스 이름
# container1_class = "my-container1"


# 컨테이너 2에 대한 스타일을 적용하는 CSS 클래스 이름
container2_class = "my-container2"

# # 컨테이너 1 생성
# my_container1 = st.container()
# # 컨테이너 1에 클래스 이름을 적용하여 스타일 적용
# my_container1.markdown(
#     f'<div class="{container1_class}">'
#     f'<img src="chat.png" alt="안녕하세요!">'
#     f'<img src="chat.png" alt="어떤것을 알고 싶으신가요?">'
#     f'</div>',
#     unsafe_allow_html=True
# )


# 두 번째 컨테이너 스타일을 적용하는 CSS 클래스
container2_class = "my-container2"
st.markdown(
    f'<div class="{container2_class}">'
    f'<input placeholder="ask something"></input>'
    f'<button>▼</button>'
    f'</div>',
    unsafe_allow_html=True
)