import streamlit as st
import requests
from bs4 import BeautifulSoup
from common import crawl_naver_entertainment, request_chat_completion, stream_response

st.set_page_config(
    page_title = "chatGPT API 서비스 개발",
    page_icon = "https://static.vecteezy.com/system/resources/thumbnails/021/059/827/small_2x/chatgpt-logo-chat-gpt-icon-on-white-background-free-vector.jpg"
)

prompt_template_v3 = """
최신 경제 뉴스 기사가 주어집니다
뉴스 기사를 참고해서 유튜브 쇼츠 대본을 작성해주세요
흥미롭고 자극적으로 작성해주세요
아래 포맷으로 작성해주세요.
10대 소녀가 친구에게 말하는 듯한 말투로 작성해주세요

[제목] <제목 텍스트>\n\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사> \n
[대본] <나레이션 방식의 대본>\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사> \n
[대본] <나레이션 방식의 대본>\n
....

---
뉴스기사 : {article}
---
""".strip()

st.title("AI 유튜브 쇼츠 대본 생성기")
st.subheader("기사 URL을 입력하면 쇼츠 대본을 만들어줍니다")

example_url = "https://n.news.naver.com/mnews/article/374/0000429845"

auto_complete = st.toggle("예제로 채우기")

with st.form("form"):
    url = st.text_input(
        "기사 URL",
        value=example_url if auto_complete else "",
        placeholder=example_url)
    submit = st.form_submit_button("제출하기!")
    
if submit:
    if not url:
        st.error("기사 URL을 입력해주세요!")
    elif not url.startswith("https://n.news.naver.com/mnews"):
        st.error("처리할 수 없는 url입니다")
    else:
        article = crawl_naver_entertainment(url)
        prompt = prompt_template_v3.format(
            article = article
        )
        system_role = "당신은 유튜브 쇼츠 대본 생성 전문가입니다."
        response = request_chat_completion(
            prompt=prompt,
            stream=True,
            system_role=system_role
        )
        message = stream_response(response)
        st.subheader("파싱된 대본 부분")
        scripts = [x.strip() for x in message.split("\n") if not x.startswith("[")]
        for script in scripts:
            if script:
                st.markdown(script)
        