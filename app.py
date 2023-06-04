import streamlit as st
import mysql.connector
import os
st.markdown(
    """
    <div class='k'>
        <img src='https://play-lh.googleusercontent.com/gdWh1q1H6CXO1B1IpB_FmqUAKs8uEZq8tRWzSPlYSwAVVK-BAB4pnhL4UhTzaIbZlSs=s48-rw' alt='chat'/>
        <h3 style='margin-top: 10px;'>삼성증권 챗봇이</h3>
    </div>
    """,
    unsafe_allow_html=True
)

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# 커스텀 레이아웃 생성
my_container1 =  st.container()

# 이미지 표시
my_container1.image("Img/chat.png", "안녕하세요!")
my_container1.image("Img/chat.png", "어떤것을 알고 싶으신가요?")


# 사용자 입력을 SQL 쿼리로 변환하는 함수
def generate_query(input_text):
    # 입력된 질문에 따라 적절한 SQL 쿼리를 생성합니다.
    if input_text == '현대차의 EPS는?':
        query = f"SELECT EPS FROM stock_data WHERE CODE = '005380'"
        return query
    else:
        return


user_input = st.text_input("", "")

if st.button("전송"):
    query = generate_query(user_input)
    if query:
        # MySQL 연결 설정 및 실행
        host = 'localhost'
        user = 'root'
        password =os.environ['PASSWORD']
        database = 'samsung'

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        # 결과 출력 등 필요한 로직을 추가합니다.
        print(result)

        my_container1.image("Img/person.png", user_input)
        my_container1.image("Img/chat.png", str(result[0][0].replace(',', '')))

        # 연결 종료
        connection.close()
        user_input = ""
    else:
        my_container1.image("Img/person.png", user_input)
        my_container1.image("Img/chat.png", "올바른 질문을 입력해주세요.")