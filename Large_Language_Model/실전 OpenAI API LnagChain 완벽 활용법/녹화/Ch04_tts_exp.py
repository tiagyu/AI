from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# api key 선택
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 폴더 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))

# 생성할 파일명
speech_file_path = os.path.join(current_dir, "speech.mp3")

with client.audio.speech.with_streaming_response.create(
    model = "tts-1",
    voice = "alloy",
    input = "오늘 날씨의 미세먼지는 좋지 않습니다. 마스크를 쓰고 나가세요"
) as response:
    response.stream_to_file(speech_file_path)