import streamlit as st
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

openai.api_key = st.secrets["OPENAI_API_KEY"]

# api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai.api_key)

def request_chat_completion(prompt, 
                            system_role = "당신은 유용한 도우미입니다.", 
                            model = "gpt-3.5-turbo",
                            stream = False):
    messages = [
        {"role" : "system", "content" : system_role},
        {"role" : "user", "content" : prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response

def stream_response(response):
    message = ""
    placeholder = st.empty()
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            message += delta.content
            placeholder.markdown(message + "▌")
            # print(delta.content, end="", flush=True)
    placeholder.markdown(message)
    return message

def stream_response_console(response):
    message = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            message += delta.content
            print(delta.content, end="")
    return message

def crawl_naver_entertainment(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    article = soup.find("div", class_= "newsct_article _article_body").text.strip()
    return article