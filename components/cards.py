import streamlit as st

def dashboard_cards():

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric(
            "Questions",
            "248",
            "+12"
        )

    with c2:
        st.metric(
            "Accuracy",
            "92%",
            "+4%"
        )

    with c3:
        st.metric(
            "XP",
            "4520",
            "+180"
        )

    with c4:
        st.metric(
            "Rank",
            "#41",
            "+8"
        )