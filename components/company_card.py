import streamlit as st

def company_cards():

    c1,c2,c3,c4=st.columns(4)

    companies=[
        "🟦 Google",
        "🟧 Amazon",
        "🔵 Meta",
        "🟩 Microsoft"
    ]

    probs=[
        "82%",
        "79%",
        "76%",
        "71%"
    ]

    for col,name,p in zip(
        [c1,c2,c3,c4],
        companies,
        probs
    ):

        with col:

            st.info(name)

            st.progress(int(p[:-1])/100)

            st.caption(
                f"Readiness {p}"
            )