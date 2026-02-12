import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Digster SOS", layout="wide", page_icon="🚨")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .emergency-side { background-color: #fff1f1; padding: 40px; border-radius: 25px; border: 3px solid #ff4b4b; text-align: center; height: 500px; }
    .account-side { background-color: #ffffff; padding: 40px; border-radius: 25px; border: 1px solid #ddd; height: 500px; }
    .sos-button { 
        background: red; color: white; border-radius: 50%; width: 160px; height: 160px; 
        line-height: 160px; font-size: 35px; font-weight: bold; margin: 20px auto; 
        box-shadow: 0 0 25px rgba(255,0,0,0.6); cursor: pointer;
    }
    </style>
""", unsafe_allow_mention=True)

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🚨 Digster: نظام الطوارئ الذكي</h1>", unsafe_allow_mention=True)

# تقسيم الشاشة
col_left, col_right = st.columns([1, 1], gap="large")

# الجهة اليسرى (الحساب)
with col_left:
    st.markdown('<div class="account-side">', unsafe_allow_mention=True)
    st.header("👤 بوابة المستخدم")
    st.write("سجل دخولك ليتم مراجعة طلبك من قبل أستاذ عبيد.")
    if st.button("🔵 تسجيل الدخول عبر Google", use_container_width=True):
        st.info("جاري التحقق... طلبك قيد المراجعة الآن.")
    st.write("---")
    st.warning("حالة الحساب: 🟡 بانتظار الموافقة")
    st.markdown('</div>', unsafe_allow_mention=True)

# الجهة اليمنى (الطوارئ)
with col_right:
    st.markdown('<div class="emergency-side">', unsafe_allow_mention=True)
    st.header("🆘 استغاثة فورية")
    st.markdown('<div class="sos-button">SOS</div>', unsafe_allow_mention=True)
    st.write("### اتصل الآن")
    c1, c2 = st.columns(2)
    c1.button("🚑 إسعاف", use_container_width=True)
    c2.button("🚓 شرطة", use_container_width=True)
    st.markdown('</div>', unsafe_allow_mention=True)

# لوحة المدير (مخفية بالأسفل)
with st.expander("🔐 لوحة تحكم المدير (Abed)"):
    pw = st.text_input("كلمة السر", type="password")
    if pw == "abed2026":
        st.success("أهلاً بك يا مدير! لديك 1 طلب بانتظار التفعيل.")
        st.button("✅ تفعيل حساب user_test@gmail.com")
