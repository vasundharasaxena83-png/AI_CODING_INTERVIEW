import streamlit as st

def badges():

    st.subheader("🏅 Achievements")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.success("🥉 Beginner")

    with c2:
        st.success("🥈 DSA Explorer")

    with c3:
        st.success("🥇 Interview Pro")

    with c4:
        st.success("👑 Google Ready")