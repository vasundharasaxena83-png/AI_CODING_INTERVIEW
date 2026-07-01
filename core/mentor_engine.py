def advanced_ai_feedback(question, code, structure, algo_type, complexity):

    feedback = []

    # 🟢 HANDLE TRIVIAL CODE FIRST
    if algo_type in ["trivial", "basic"]:
        return "🟢 Simple output detected — no algorithmic logic required."

    feedback.append(f"🧠 Pattern: {algo_type}")
    feedback.append(f"📊 Complexity: {complexity}")

    if structure.get("loops", 0) == 0:
        feedback.append("⚠️ No loops detected")

    if structure.get("functions", 0) == 0:
        feedback.append("⚠️ No function defined")

    if structure.get("recursion"):
        feedback.append("🔁 Recursion detected (verify correctness)")

    feedback.append("🔥 Improve structure for interview readiness")

    return "\n".join(feedback)