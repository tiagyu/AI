from openai import OpenAI
from getpass import getpass
import os
from dotenv import load_dotenv

# api key
env_path = os.path.join(os.path.dirname(__file__),"..",".env")
load_dotenv(env_path)

openai_api_key = os.getenv("OPENAI_API_KEY")

print(openai_api_key)

client = OpenAI(api_key=openai_api_key)

# 생성할 파일명
speech_file_path = 'speech_test.mp3'

with client.audio.speech.with_streaming_response.create(
    model='tts-1',
    voice='coral',
    input="오늘은 날이 춥고 챔피언스리그 경기를 하는 날입니다!"
) as response:
    response.stream_to_file(speech_file_path)