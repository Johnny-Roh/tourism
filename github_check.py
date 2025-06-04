import streamlit as st
import requests

# GitHub 정보
GITHUB_USER = st.secrets['user']
REPO_NAME = st.secrets['name']
FOLDER_PATH = st.secrets['path']
TOKEN = st.secrets['token']

# GitHub API URL
url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FOLDER_PATH}'

# 인증 헤더 추가
headers = {
    "Authorization": f"token {TOKEN}"
}

# API 요청
response = requests.get(url, headers=headers)

# Streamlit 앱 출력
st.title("수행평가 제출 확인(하투하투)")

if response.status_code == 200:
    files = response.json()
    if isinstance(files, list):
        file_names = [file['name'] for file in files]
        st.write("파일 목록:", ", ".join(file_names))
    else:
        st.write("폴더가 비어 있습니다.")
else:
    st.error(f"폴더를 가져오는 데 실패했습니다. 😢\n응답 코드: {response.status_code}\n내용: {response.text}")
