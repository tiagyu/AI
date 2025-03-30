import streamlit as st
from common import print_messages
from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os

st.set_page_config(page_title="GPT", page_icon="data:image/png;base64,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")
st.title("GPT 만들어보기")

# API KEY 설정
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state["messages"] = []

print_messages()

## 메모리
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {} # 세션 기록을 저장할 딕셔너리

# 세션 ID를 기반으로 세션 기록을 가져오는 함수
def get_session_history(session_ids: str) -> BaseChatMessageHistory:
    print(session_ids)
    if session_ids not in store: # 세션 ID가 store에 없는 경우
        # 새로운 ChatMessageHistory 객체를 생성하여 store에 저장
        store[session_ids] = ChatMessageHistory()
    return store[session_ids] # 해당 세션 ID에 대한 세션 기록 반환

chain_with_memory = (
    RunnableWithMessageHistory( # RunnableWithMessageHistory 객체 생성
        runnable, # 실행할 Runnable 객체
        get_session_history, # 세션 기록을 가져오는 함수
        input_messages_key="input", # 입력 메시지의 키
        history_messages_key="history", # 기록 메시지의 키
    )
)


if user_input := st.chat_input("메세지를 입력해주세요", 
                               accept_file=False, 
                               file_type = ["jpg", "jpeg", "png"]):
    # 사용자가 입력한 내용
    st.chat_message("user").write(user_input)
    # st.session_state["messages"].append(("user", user_input))
    st.session_state["messages"].append(ChatMessage(role="user", content=user_input))
    
    # LLM을 사용하여 AI의 답변을 생성
    prompt = ChatPromptTemplate.from_template("""
                                     질문에 대해서 간결하게 답변해 주세요
                                     {question}
                                     """)
    
    chain = prompt | ChatOpenAI() | StrOutputParser()
    response = chain.invoke({"question" : user_input})
    msg = response.content
    
    
    
    # AI의 답변
    with st.chat_message("assistant"):
        st.write(msg)
        # st.session_state["messages"].append(("assistant", msg))
        st.session_state["messages"].append(ChatMessage(role="assistant", content=msg))
