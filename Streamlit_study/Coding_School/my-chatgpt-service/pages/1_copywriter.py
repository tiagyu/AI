import streamlit as st

st.set_page_config(
    page_title = "chatGPT API 서비스 개발",
    page_icon = "https://static.vecteezy.com/system/resources/thumbnails/021/059/827/small_2x/chatgpt-logo-chat-gpt-icon-on-white-background-free-vector.jpg"
)

st.title("✍️ AI 카피라이터터")
st.subheader("AI를 이용해서 손쉽게 마케팅 문구를 작성해보세요!")
auto_complete = st.toggle("예시로 채우기")

example = {
    "product_name" : "카누",
    "product_desc" : "집에서도 카페 맛이나는 커피믹스",
    "keywords" : ["브라질", "향기", "공유"]
}

with st.form("form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        product_name = st.text_input(
            "제품명",
            placeholder=example['product_name'],
            value = example["product_name"] if auto_complete else "")
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
    product_desc = st.text_input(
        "제품 설명",
        placeholder=example["product_desc"],
        value=example["product_desc"] if auto_complete else ""
        )
    
    st.text("포함할 키워드를 최대 3개까지 입력해주세요")
    col1, col2, col3 = st.columns(3)
    with col1:
        keyword_1 = st.text_input(
            label="keyword_1",
            label_visibility='collapsed',
            placeholder="키워드 1",
            value=example["keywords"][0] if auto_complete else ""
        )
    with col2:
        keyword_2 = st.text_input(
            label="keyword_2",
            label_visibility='collapsed',
            placeholder="키워드 2",
            value=example["keywords"][1] if auto_complete else ""
        )
    with col3:
        keyword_3 = st.text_input(
            label="keyword_3",
            label_visibility='collapsed',
            placeholder="키워드 3",
            value=example["keywords"][2] if auto_complete else ""
        )
    submit = st.form_submit_button("Submit")
if submit:
    if not product_name:
        st.error("제품명을 추가해 주세요")
    elif not product_desc:
        st.error("제품설명을 추가해주세요")
    else:
        print("click_submit")
        st.success("마케팅 문구를 생성할 수 있습니다!")