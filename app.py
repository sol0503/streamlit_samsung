import streamlit as st
import mysql.connector
import os

st.markdown(
    """
    <div class='k'>
        <img src='https://play-lh.googleusercontent.com/gdWh1q1H6CXO1B1IpB_FmqUAKs8uEZq8tRWzSPlYSwAVVK-BAB4pnhL4UhTzaIbZlSs=s48-rw' alt='chat'/>
        <h3 style='margin-top: 10px; margin'>삼성증권 챗봇이</h3>
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
my_container1.image("Img/chat.png", "안녕하세요!")
my_container1.image("Img/chat.png", "어떤것을 알고 싶으신가요?")





# 사용자 입력에 따라 응답을 생성하는 함수
def generate_response(input_text):
    # 적절한 응답 생성 로직을 구현합니다.
    response = input_text
    return my_container1.image("Img/person.png", response)





user_input = st.text_input("", "")

if st.button("전송"):
    response = generate_response(user_input)


# MySQL 연결 설정
host = 'localhost'
user = 'root'
password =os.environ['PASSWORD']
database = 'samsung'

# MySQL 연결
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# MySQL 쿼리 실행 및 결과 표시
cursor = connection.cursor()
cursor.execute('SELECT * FROM stock_data')
result = cursor.fetchall()

for row in result:
    print(row)

# 연결 종료
connection.close()