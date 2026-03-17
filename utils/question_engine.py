FEATURE_QUESTIONS = {
    "uses_array": "Does the problem rely heavily on arrays?",
    "uses_graph": "Does the problem involve graphs?",
    "uses_hashmap": "Does it require hash maps?",
    "uses_heap": "Does it require a heap or priority queue?",
    "recursion": "Does the solution involve recursion?",
    "dynamic_programming": "Does it use dynamic programming?",
    "divide_conquer": "Does it use divide and conquer?",
    "shortest_path": "Is it a shortest path problem?",
    "mst": "Does it involve minimum spanning trees?",
    "topological": "Does it require topological sorting?",
    "sorting": "Is sorting a key part of the solution?",
    "search": "Does it involve searching?",
    "sliding_window": "Does it use sliding window?",
    "greedy": "Does it use a greedy approach?",
    "backtracking": "Does it require backtracking?",
    "graph_problem": "Is it generally a graph problem?",
    "optimization_problem": "Is it an optimization problem?",
    "string_problem": "Does it involve string manipulation?"
}

def get_question_text(feature):
    return FEATURE_QUESTIONS.get(feature, "")