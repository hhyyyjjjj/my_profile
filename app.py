import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="유진 프로필", page_icon="🌷")

# 제목
st.title("🙋‍♀️ 프로필")

# 이미지 1
st.image("profile_yujin.JPG", width=200)

# 자기소개
st.subheader("👩 into 👋")
st.write("""
❤️ 1993년생, ESTJ, 천칭자리, A형  
🫡 33세! 군인으로 13년(GOP부대 6년, 교관 6년), 아내로 4년, 엄마로 9개월  
👶 육아난이도 최상, 9개월 아들과 강아지 두마리 애개육아중 🧟‍♀️  
🧯 건양대학교 대학원 재난안전소방학과 재학 중  
🚴 자전거, 달리기, 등산, 골프가 취미었다가 요즘은 아기꾸미기가 취미인 사람 ❤️  
      
육아 + 일 + 취미 + 자기개발까지 다 챙기는 잡동사니 라이프  
스트레스는 **맥주🍺**와 **쇼핑🛍️**으로 해소함
""")

# 사진첩
st.subheader("📸 사진첩")

# 이미지 파일 리스트 (이름은 실제 파일명으로 바꾸세요!)
image_files = [
    "profile_gpt.JPG", "profilebaby.jpg", "profilesidar.JPG",
    "profilecrown.jpg", "profile9month.jpg","profileian1.JPG", 
    "profileaegae.jpg", "profilegop.JPG","profileinst.JPG", 
    "profilerun.JPG", "profilebike.JPG", "profilehike.JPG",
]

# 3 x 3 배열로 사진 보여주기
for i in range(0, len(image_files), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(image_files):
            with cols[j]:
                st.image(image_files[i + j], use_column_width=True)


# SNS 링크
st.subheader("🔗 소통을 사랑합니다 ❤️")
st.markdown("어른 둘, 아기 하나, 강아지 둘이 함께하는 일상🤍")
st.markdown("[📷 인스타그램](https://www.instagram.com/ujineeda/)")
