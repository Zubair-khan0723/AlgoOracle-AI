def extract_features_from_text(text, features):

    text = text.lower()

    vector = []

    for f in features:

        value = 0

        # Sorting related
        if f == "sorting":
            if any(word in text for word in [
                "sort","sorting","sorted",
                "ascending","descending",
                "order","arrange"
            ]):
                value = 1

        # Arrays often used in sorting
        elif f == "uses_array":
            if any(word in text for word in [
                "array","list","numbers","elements"
            ]):
                value = 1

        # Divide and conquer
        elif f == "divide_conquer":
            if "divide and conquer" in text:
                value = 1

        # Graph problems
        elif f == "uses_graph":
            if any(word in text for word in [
                "graph","node","edge","network","city"
            ]):
                value = 1

        # Shortest path
        elif f == "shortest_path":
            if any(word in text for word in [
                "shortest path",
                "minimum distance",
                "route",
                "distance"
            ]):
                value = 1

        # Searching
        elif f == "search":
            if any(word in text for word in [
                "search","find element","lookup"
            ]):
                value = 1

        # Recursion
        elif f == "recursion":
            if any(word in text for word in [
                "recursion","recursive"
            ]):
                value = 1

        # Greedy
        elif f == "greedy":
            if "greedy" in text:
                value = 1

        # Backtracking
        elif f == "backtracking":
            if any(word in text for word in [
                "permutation","subset","backtracking"
            ]):
                value = 1

        vector.append(value)

    return vector