import streamlit as st

st.set_page_config(
    page_title = "chatGPT API 서비스 개발",
    page_icon = "https://static.vecteezy.com/system/resources/thumbnails/021/059/827/small_2x/chatgpt-logo-chat-gpt-icon-on-white-background-free-vector.jpg"
)

st.title("✍️ AI 카피라이터터")
st.subheader("AI를 이용해서 손쉽게 마케팅 문구를 작성해보세요!")

with st.form("form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        product_name = st.text_input("제품명")
    with col2:
        max_length = st.number_input(
            label = "최대 단어 수",
            min_value = 5,
            max_value = 20,
            step = 1,
            value = 10
            )
    with col3:
        num = st.number_input(
            label = "생성할 문구 수",
            min_value = 1,
            max_value = 10,
            step = 1,
            value = 5
            )
    product_desc = st.text_input("제품 설명")
    
    st.text("포함할 키워드를 최대 3개까지 입력해주세요")
    col1, col2, col3 = st.columns(3)
    with col1:
        keyword_1 = st.text_input(
            label="keyword_1",
            label_visibility='collapsed',
            placeholder="키워드 1"
        )
    with col2:
        keyword_2 = st.text_input(
            label="keyword_2",
            label_visibility='collapsed',
            placeholder="키워드 2"
        )
    with col3:
        keyword_3 = st.text_input(
            label="keyword_3",
            label_visibility='collapsed',
            placeholder="키워드 3"
        )
    submit = st.form_submit_button("Submit")
if submit:
    print("click_submit")
    st.success("제출!")