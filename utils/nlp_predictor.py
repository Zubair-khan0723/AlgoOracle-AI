import re

ALGO_PATTERNS = {

"Dijkstra": {
"keywords":[
"shortest path",
"shortest distance",
"minimum distance",
"weighted graph",
"distance between nodes"
],
"weight":3
},

"BFS": {
"keywords":[
"shortest path unweighted",
"minimum edges",
"level order traversal"
],
"weight":3
},

"DFS": {
"keywords":[
"depth first",
"explore graph",
"dfs traversal"
],
"weight":2
},

"Graph Traversal":{
"keywords":[
"graph",
"node",
"edge",
"visit nodes"
],
"weight":1
},

"Sorting":{
"keywords":[
"sort",
"arrange",
"ascending",
"descending",
"order numbers"
],
"weight":2
},

"Binary Search":{
"keywords":[
"sorted array",
"find element quickly",
"log n search",
"binary search"
],
"weight":3
},

"Backtracking":{
"keywords":[
"permutation",
"subset",
"combination",
"n queens",
"generate all"
],
"weight":3
},

"Dynamic Programming":{
"keywords":[
"optimal substructure",
"overlapping subproblems",
"dp solution"
],
"weight":2
},

"Knapsack":{
"keywords":[
"knapsack",
"capacity",
"maximize value",
"weight limit"
],
"weight":3
},

"Hashing":{
"keywords":[
"hash",
"dictionary",
"key value",
"lookup table"
],
"weight":2
}

}


def predict_algorithm_from_text(text):

    text = text.lower()

    scores = {}

    for algo,data in ALGO_PATTERNS.items():

        score = 0

        for keyword in data["keywords"]:

            if re.search(keyword,text):

                score += data["weight"]

        scores[algo] = score


    best_algo = max(scores,key=scores.get)

    confidence = scores[best_algo] / 10

    return best_algo, confidence