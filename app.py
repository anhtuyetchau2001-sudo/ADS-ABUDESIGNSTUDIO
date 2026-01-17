import streamlit as st

# 1. CẤU HÌNH
TEN_CONG_TY = "ABU DESIGN STUDIO"
LINK_LOGO = "https://scontent.fsgn5-5.fna.fbcdn.net/v/t39.30808-6/578496584_122181028760495578_2760060216837748891_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=rJ1AxAhz1yMQ7kNvwHgboY6&_nc_oc=Adk08fnm-6_IUBgzYQ5YputiXgMeGQMVTc3F3nXaaatHWlt0u3CzEedbmzRS3q_RttE&_nc_zt=23&_nc_ht=scontent.fsgn5-5.fna&_nc_gid=6QYeyUArxzcm8uxErlOIOA&oh=00_Afo1Zbb3VOMf577XBchHGSyLOSZbuKNZK7bk7KNaZ8fZhA&oe=6970DCB4"

st.set_page_config(page_title=TEN_CONG_TY, layout="wide")

# 2. GIAO DIỆN
st.markdown("""
    <style>
    .stApp { background-color: #0b0b0b; color: #ffffff; }
    h1 { color: #ffc107 !important; font-family: 'Segoe UI'; font-weight: bold; }
    .project-box { border: 1px solid #333; padding: 10px; border-radius: 5px; background: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
col1, col2 = st.columns([1, 5])
with col1:
    st.image(LINK_LOGO, width=120)
with col2:
    st.title(TEN_CONG_TY)
    st.write("### TƯ VẤN VÀ THIẾT KẾ KIẾN TRÚC")

st.markdown("---")

# 4. DỰ ÁN TIÊU BIỂU
st.write("## 🏗️ DỰ ÁN THIẾT KẾ")
c1, c2, c3 = st.columns(3)

with c1:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=500")
    st.markdown("<div class='project-box'><b>NHÀ PHỐ HIỆN ĐẠI</b><br>Q.7, TP. HCM</div>", unsafe_allow_html=True)

with c2:
    st.image("https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?q=80&w=500")
    st.markdown("<div class='project-box'><b>BIỆT THỰ TÂN CỔ ĐIỂN</b><br>Bình Dương</div>", unsafe_allow_html=True)

with c3:
    st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?q=80&w=500")
    st.markdown("<div class='project-box'><b>NỘI THẤT CHUNG CƯ</b><br>Vinhomes Central Park</div>", unsafe_allow_html=True)

# 5. LIÊN HỆ
st.markdown("---")
st.write("## 📞 LIÊN HỆ TƯ VẤN")
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.text_input("Họ tên của bạn")
    st.text_input("Số điện thoại")
with contact_col2:
    st.text_area("Yêu cầu tư vấn thiết kế")
if st.button("GỬI YÊU CẦU"):
    st.success("Cảm ơn bạn! ABU DESIGN STUDIO sẽ liên hệ sớm nhất.")
