# 🧠 FAANG Interview Simulator & AI DSA Mentor

A premium, SaaS-level interview preparation platform built with **Streamlit** and optimized with a glassmorphism dark theme. This application simulates rigorous technical interviews for top-tier tech companies (Google, Amazon, Meta, etc.), provides real-time data-driven analytics on DSA topics, tracks user readiness, and leverages an advanced AI engine for deep, granular code analysis and feedback.

---

## 🚀 Key Features

*   **Premium SaaS UI:** Fully responsive glassmorphism dark theme with custom styled elements, interactive charts, and a clean user workflow.
*   **Dynamic Question Engine:** Serves company-specific DSA questions with real-time probability mapping based on actual historical interview data.
*   **Live Interactive Dashboards:** 
    *   📊 *DSA Topic Distribution* via Plotly bar charts.
    *   🎯 *Interview Readiness Gauge* tracking your likelihood of clear.
    *   🍩 *Topic Share* distribution via interactive pie charts.
*   **Built-in Code Execution & Analysis:** Features a live solution block that runs Python code safely, analyzes structural efficiency, estimates algorithmic complexity, and catches logical or semantic relevance issues.
*   **AI Mentor Feedback:** Provides comprehensive, actionable mentor reviews detailing performance, syntax, optimizations, and algorithmic improvements.

---

## 📂 Project Architecture

The project follows a strictly modular structure to separate presentation layers from core business logic:

```text
├── assets/
│   └── style.css                 # Custom CSS overrides
├── components/
│   ├── ui_theme.py               # Core SaaS Glassmorphism injection (load_theme)
│   ├── hero.py                   # Dynamic landing banner
│   ├── cards.py                  # Analytical metric blocks
│   ├── company_card.py           # Company selection layout
│   └── badges.py                 # Status and topic tagging
├── core/
│   ├── question_engine.py        # Fetches target coding problems
│   ├── analytics_data.py         # Formulates topic dataframes
│   ├── question_probability.py   # Computes specific target company odds
│   ├── code_runner.py            # Executes/validates standard Python runtime
│   ├── code_analyzer.py          # Extracts structural tokens from code
│   ├── algo_detector.py          # Identifies matching underlying algorithms
│   ├── complexity_engine.py      # Estimates Big-O notation metrics
│   ├── evaluator.py              # Grades general execution parameters
│   ├── match_engine.py           # Evaluates task context validity
│   ├── solution_engine.py        # Generates fallback/reference approaches
│   └── mentor_engine.py          # Coordinates advanced generative feedback
├── auth.py                       # User onboarding flow (Login/Signup layers)
└── app.py                        # Central core orchestration script
