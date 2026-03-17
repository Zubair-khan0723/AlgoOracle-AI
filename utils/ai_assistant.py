import re

ALGORITHM_KNOWLEDGE = {

"Dijkstra":{
"keywords":["shortest path","distance","weighted graph","minimum distance"],
"features":["Graph","Weighted edges","Shortest path"],
"explanation":"Dijkstra finds the shortest path in weighted graphs.",
"time":"O(E log V)"
},

"BFS":{
"keywords":["shortest path unweighted","level traversal","minimum edges"],
"features":["Graph","Unweighted edges","Shortest path"],
"explanation":"BFS finds shortest paths in unweighted graphs.",
"time":"O(V+E)"
},

"DFS":{
"keywords":["explore graph","dfs","depth first"],
"features":["Graph traversal"],
"explanation":"DFS explores nodes deeply before backtracking.",
"time":"O(V+E)"
},

"Sorting":{
"keywords":["sort","ascending","descending","order numbers"],
"features":["Array","Ordering"],
"explanation":"Sorting arranges elements efficiently.",
"time":"O(n log n)"
},

"Binary Search":{
"keywords":["sorted array","find element","binary search"],
"features":["Sorted array","Search"],
"explanation":"Binary search divides the array repeatedly.",
"time":"O(log n)"
},

"Backtracking":{
"keywords":["permutation","subset","combination","n queens"],
"features":["Combinatorial search"],
"explanation":"Backtracking explores all possible solutions.",
"time":"Exponential"
},

"Dynamic Programming":{
"keywords":["optimal substructure","dp","overlapping subproblems"],
"features":["Optimization"],
"explanation":"Dynamic programming solves problems with memoization.",
"time":"Varies"
},

"Hashing":{
"keywords":["hash","dictionary","key value","lookup"],
"features":["Key-value mapping"],
"explanation":"Hash tables provide constant time lookup.",
"time":"O(1)"
}

}


def ai_algorithm_assistant(text):

    text=text.lower()

    best_algo=None
    best_score=0

    for algo,data in ALGORITHM_KNOWLEDGE.items():

        score=0

        for k in data["keywords"]:
            if re.search(k,text):
                score+=1

        if score>best_score:
            best_score=score
            best_algo=algo

    if best_algo is None:

        return {
        "algorithm":"Unknown",
        "features":[],
        "explanation":"Try describing the problem in more detail."
        }

    data=ALGORITHM_KNOWLEDGE[best_algo]

    return {
    "algorithm":best_algo,
    "features":data["features"],
    "explanation":data["explanation"],
    "time":data["time"]
    }