def is_relevant(code, topic):

    code = code.lower()

    topic_map = {
        "array": ["for", "range", "len", "append", "nums", "list"],
        "string": ["split", "join", "replace", "[::-1]", "str"],
        "dp": ["dp", "memo", "cache"],
        "graph": ["bfs", "dfs", "visited", "adj"],
        "tree": ["node", "left", "right"]
    }

    keywords = topic_map.get(topic, [])

    # count matches instead of simple true/false
    match_score = sum(1 for k in keywords if k in code)

    # 🔥 strict threshold (this is what fixes your issue)
    return match_score >= 2