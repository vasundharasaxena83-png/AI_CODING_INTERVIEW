import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from components.ui_theme import load_theme   # ✅ OK here
from components.hero import hero
from components.cards import dashboard_cards
from components.company_card import company_cards
from components.badges import badges

from auth import login, signup
from core.question_engine import get_question
from core.analytics_data import get_topic_dataframe
from core.question_probability import get_probability
from core.code_runner import run_python_code
from core.code_analyzer import analyze_code_structure
from core.algo_detector import detect_algorithm_type
from core.complexity_engine import estimate_complexity
from core.evaluator import evaluate
from core.mentor_engine import advanced_ai_feedback
from core.match_engine import is_relevant
from core.solution_engine import get_reference_solution

def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="FAANG Interview Simulator",
    layout="wide"
)

load_theme()
# -----------------------------------------
# SESSION STATE
# -----------------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "question" not in st.session_state:
    st.session_state.question = None

# -----------------------------------------
# LOGIN / SIGNUP PAGE
# -----------------------------------------
if st.session_state.user is None:

    st.markdown('<div class="title">🧠 AI FAANG Interview Simulator</div>', unsafe_allow_html=True)

    st.markdown("### Login or Create a New Account")

    mode = st.radio(
        "Select Option",
        ["Login", "Sign Up"],
        horizontal=True
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if mode == "Sign Up":

        if st.button("Create Account", use_container_width=True):

            ok, msg = signup(username, password)

            if ok:
                st.success(msg)
            else:
                st.error(msg)

    else:

        if st.button("Login", use_container_width=True):

            ok, msg = login(username, password)

            if ok:
                st.session_state.user = username
                st.rerun()

            else:
                st.error(msg)

# -----------------------------------------
# MAIN APPLICATION
# ----------------------------------------
else:

    hero()

    dashboard_cards()

    company_cards()

    badges()

    st.title(f"🏆 Welcome, {st.session_state.user}")

    # -------------------------------------
    # SIDEBAR
    # -------------------------------------
    st.sidebar.title("📊 Dashboard")

    company = st.sidebar.selectbox(
        "🏢 Company",
        [
            "Google",
            "Amazon",
            "Meta",
            "Microsoft"
        ]
    )

    difficulty = st.sidebar.selectbox(
        "🎯 Difficulty",
        [
            "easy",
            "medium",
            "hard"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("📈 DSA Analytics")

    df = get_topic_dataframe(company)

    st.sidebar.dataframe(
        df,
        use_container_width=True
    )

    if st.sidebar.button(
        "🎯 Start Interview",
        use_container_width=True
    ):
        st.session_state.question = get_question(
            company,
            difficulty
        )

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):
        st.session_state.user = None
        st.session_state.question = None
        st.rerun()

    # -------------------------------------
    # INTERVIEW PAGE
    # -------------------------------------

    if st.session_state.question is None:

        st.info(
            "👈 Select a company and click **Start Interview** from the sidebar."
        )

    else:

        q = st.session_state.question

        st.subheader("🧠 Interview Question")
        st.success(q["title"])

        probability = get_probability(
            q["title"],
            company)

        st.info(
        f"🎯 Probability of being asked in {company}: **{probability}%**"
    )

    # -------- DSA BAR CHART --------

    st.subheader("📊 DSA Topic Distribution")

    fig = px.bar(
        df,
        x="Topic",
        y="Probability (%)",
        color="Probability (%)",
        color_continuous_scale="Turbo",
        text="Probability (%)",
        template="plotly_dark",
        title=f"{company} DSA Topic Distribution"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        title_x=0.5,
        height=500,
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------- GAUGE --------

    st.subheader("🎯 Interview Readiness")

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=87,
        title={"text": f"{company} Readiness"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#4F46E5"},
            "steps": [
                {"range": [0, 50], "color": "#EF4444"},
                {"range": [50, 75], "color": "#F59E0B"},
                {"range": [75, 100], "color": "#22C55E"}
            ]
        }
    ))

    gauge.update_layout(
        template="plotly_dark",
        height=350
    )

    st.plotly_chart(gauge, use_container_width=True)

    # -------- PIE --------

    st.subheader("🍩 DSA Topic Share")

    pie = px.pie(
        df,
        names="Topic",
        values="Probability (%)",
        hole=0.6,
        template="plotly_dark",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    pie.update_layout(title_x=0.5)

    st.plotly_chart(pie, use_container_width=True)
# -------------------------
# CODE EDITOR
# -------------------------
    st.subheader("💻 Write Your Solution")

    user_code = st.text_area(
        "Code Editor",
        height=250,
        placeholder="Write your Python solution here..."
    )
# ---------------------------------------------------
# SUBMIT ANSWER
# ---------------------------------------------------

    if st.button("🚀 Submit Answer", use_container_width=True):
        if not user_code.strip():
            st.warning("⚠️ Please write your solution first.")
            st.stop()

        # -------------------------
        # Execute Code
        # -------------------------
        result = run_python_code(user_code)

        st.subheader("⚙️ Execution Output")

        if result.get("success", True):
            st.code(result["output"])
        else:
            st.error(result["output"])

        # -------------------------
        # Analyze Code
        # -------------------------
        structure = analyze_code_structure(user_code)
        algorithm = detect_algorithm_type(user_code)
        complexity = estimate_complexity(structure)

        st.subheader("🔍 Code Structure")
        st.json(structure)

        st.subheader("📌 Algorithm Detected")
        st.success(algorithm)

        st.subheader("📈 Estimated Time Complexity")
        st.info(complexity)

        # -------------------------
        # Check Relevance
        # -------------------------
        relevant = is_relevant(user_code, q["topic"])

        if not relevant:
            st.error("❌ Your solution does not appear to solve the interview question.")

            solution = get_reference_solution(q["title"])

            st.subheader("💡 Recommended Approach")
            st.info(solution["approach"])

            st.subheader("✅ Reference Solution")

            st.code(
                solution["code"],
                language="python"
            )
        else:
            # -------------------------
            # Score
            # -------------------------
            score = evaluate(
                structure,
                complexity,
                algorithm
            )

            st.subheader("🏆 Interview Score")

            st.progress(score / 100)

            st.success(f"{score}/100")

            # -------------------------
            # AI Feedback
            # -------------------------
            feedback = advanced_ai_feedback(
                q["title"],
                user_code,
                structure,
                algorithm,
                complexity
            )

            st.subheader("🧠 AI Mentor Feedback")

            st.write(feedback)

        # -------------------------
        # Interview Summary
        # -------------------------
            st.subheader("📋 Interview Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Algorithm",algorithm)

                st.metric("Complexity",complexity)

            with col2:
                st.metric("Interview Score",f"{score}/100")

                st.metric( "Company",company)

        # -------------------------
        # Final Verdict
        # -------------------------
            st.subheader("🎯 Final Verdict")

            if score >= 90:
               st.success("🌟 Excellent! This solution is interview-ready.")

            elif score >= 75:
               st.info("👍 Good solution. Minor improvements are recommended.")

            elif score >= 50:
               st.warning("⚠️ Average solution. Work on optimization and coding style.")

            else:
               st.error("❌ Needs significant improvement. Review the problem and try again.")