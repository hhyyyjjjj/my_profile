import streamlit as st
import os

# 페이지 기본 설정
st.set_page_config(page_title="유진 프로필", page_icon="🌷")

# 제목
st.title("🙋‍♀️ 프로필")

# 이미지 1 (대표 이미지)
st.image("profile_yujin.JPG", width=200)

# 자기소개
st.subheader("👩 intro 👋")
st.write("""
❤️ 1993년생, ESTJ, 천칭자리, A형  
🫡 33세! 군인으로 13년 (GOP부대 6년, 교관 6년), 아내로 4년, 엄마로 9개월  
👶 육아난이도 최상, 9개월 아들과 강아지 두 마리 애개육아 중 🧟‍♀️  
🧯 건양대학교 대학원 재난안전소방학과 재학 중  
🚴 자전거, 달리기, 등산, 골프가 취미였다가 요즘은 아기 꾸미기가 취미인 사람 ❤️  
      
육아 + 일 + 취미 + 자기개발까지 다 챙기는 잡동사니 라이프  
스트레스는 **맥주🍺**와 **쇼핑🛍️**으로 해소함
""")

# 사진첩
st.subheader("📸 사진첩")

# 자동으로 이미지 파일 불러오기 (대소문자 포함 확장자)
image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
image_files = [f for f in os.listdir() if f.endswith(image_extensions) and f != "profile_yujin.JPG"]

# 3x3 그리드로 표시
for i in range(0, len(image_files), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(image_files):
            with cols[j]:
                st.image(image_files[i + j], use_container_width=True)

# SNS 링크
st.subheader("🔗 소통을 사랑합니다 ❤️")
st.markdown("어른 둘, 아기 하나, 강아지 둘이 함께하는 일상🤍")
st.markdown("[📷 인스타그램](https://www.instagram.com/ujineeda/)")
