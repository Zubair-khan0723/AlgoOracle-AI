import streamlit as st
import streamlit.components.v1 as components
import joblib
import time
import base64
from PIL import Image
from streamlit_agraph import agraph, Node, Edge, Config
from utils.nlp_predictor import predict_algorithm_from_text
from utils.prediction import predict_algorithm
from utils.session_manager import initialize_session, reset_session
from utils.question_engine import get_question_text
from utils.dynamic_questions import select_next_question
from utils.ai_assistant import ai_algorithm_assistant
from visualizations.feature_importance import plot_feature_importance
from visualizations.tree_explorer import visualize_tree

from data.algorithm_info import ALGORITHM_INFO
from data.algorithm_code import ALGORITHM_CODE


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(page_title="AlgoOracle", layout="wide")


# ------------------------------------------------
# IMAGE HELPER
# ------------------------------------------------

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

processing_img = img_to_base64("assets/ai_processing.png")
import base64

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("assets/background_ai.png")

# ------------------------------------------------
# BACKGROUND STYLE
# ------------------------------------------------

st.markdown(f"""
<style>

.stApp{{
background-image:url("data:image/png;base64,{bg_image}");
background-size:cover;
background-position:center;
background-attachment:fixed;
animation:movebg 90s linear infinite;
}}

@keyframes movebg{{
0%{{background-position:0% 0%;}}
50%{{background-position:100% 100%;}}
100%{{background-position:0% 0%;}}
}}

.block-container{{
background:rgba(10,15,25,0.75);
backdrop-filter:blur(10px);
border-radius:20px;
padding:2rem;
}}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HEADER
# ------------------------------------------------

logo = Image.open("assets/logo.png")

c1,c2 = st.columns([1,8])

with c1:
    st.image(logo,width=80)

with c2:
    st.title("AlgoOracle")
    st.write("AI system that predicts the best algorithm")


# ------------------------------------------------
# LOAD MODEL
# ------------------------------------------------

model = joblib.load("model/decision_tree.pkl")
encoder = joblib.load("model/label_encoder.pkl")
features = joblib.load("model/features.pkl")

initialize_session(features)


# ------------------------------------------------
# NAVIGATION
# ------------------------------------------------

page = st.radio(
"",
["Home","AI Predictor","Text Predictor","Explainability","Algorithm Map","AI Assistant"],
horizontal=True
)


# ------------------------------------------------
# PREDICTION DISPLAY
# ------------------------------------------------

def show_prediction(pred,conf,probs):

    st.session_state["last_prediction"] = pred
    st.markdown(f"""
    <div class="result-card">
    <h1>{pred}</h1>
    <p>Confidence: {conf*100:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(conf)

    st.subheader("Algorithm Recommendations")

    top3 = sorted(
        zip(encoder.classes_,probs),
        key=lambda x:x[1],
        reverse=True
    )[:3]

    for algo,prob in top3:
        st.write(algo)
        st.progress(prob)

    if pred in ALGORITHM_INFO:

        info = ALGORITHM_INFO[pred]

        st.subheader("Why this algorithm was chosen")
        st.write(info["description"])
        st.write("Time Complexity:",info["time"])

    if pred in ALGORITHM_CODE:

        st.subheader("Example Implementation")
        st.code(ALGORITHM_CODE[pred],language="python")


# ------------------------------------------------
# HOME
# ------------------------------------------------

if page=="Home":

    st.header("Discover the Right Algorithm Instantly")

    col1,col2,col3 = st.columns(3)

    col1.info("AI Predictor\nAnswer questions and AlgoOracle predicts algorithm.")
    col2.info("Text Predictor\nPaste programming problem description.")
    col3.info("Explainability\nExplore how the AI model works.")


# ------------------------------------------------
# AI PREDICTOR
# ------------------------------------------------

elif page=="AI Predictor":

    st.header("AlgoOracle Algorithm Guesser")

    asked=list(st.session_state.answers.keys())
    next_feature=select_next_question(model,features,asked)

    progress=len(asked)/7
    st.progress(min(progress,1.0))

    col1,col2=st.columns([1,2])

    with col1:

        if next_feature:
            st.image("assets/ai_thinking.png",width=300)
        else:
            st.image("assets/ai_happy.png",width=300)

    with col2:

        if next_feature:

            question=get_question_text(next_feature)

            st.markdown(f"""
            <div class="bubble">
            🤖 {question}
            </div>
            """,unsafe_allow_html=True)

            c1,c2,c3=st.columns(3)

            if c1.button("Yes"):
                st.session_state.answers[next_feature]=1
                st.rerun()

            if c2.button("No"):
                st.session_state.answers[next_feature]=0
                st.rerun()

            if c3.button("Not Sure"):
                st.session_state.answers[next_feature]=0
                st.rerun()

        else:

            popup=st.empty()

            popup.markdown(f"""
            <div style="
            position:fixed;
            top:0;
            left:0;
            width:100%;
            height:100%;
            background:rgba(0,0,0,0.7);
            display:flex;
            align-items:center;
            justify-content:center;
            flex-direction:column;
            z-index:9999;
            ">
            <img src="data:image/png;base64,{processing_img}" width="280">
            <h2 style="color:white">AlgoOracle is analyzing...</h2>
            </div>
            """,unsafe_allow_html=True)

            time.sleep(2)
            popup.empty()

            vector=[0]*len(features)

            for i,f in enumerate(features):
                if f in st.session_state.answers:
                    vector[i]=st.session_state.answers[f]

            pred,conf,probs=predict_algorithm(model,encoder,vector)

            col1,col2,col3=st.columns([1,2,1])

            with col2:
                show_prediction(pred,conf,probs)

                st.markdown("<br>", unsafe_allow_html=True)

                if st.button("🔄 Restart Prediction"):
                    reset_session([])
                    st.rerun()


# ------------------------------------------------
# TEXT PREDICTOR
# ------------------------------------------------

elif page=="Text Predictor":

    st.header("Smart Algorithm Predictor")

    problem = st.text_area("Describe your programming problem")

    if st.button("Predict Algorithm"):

        with st.spinner("Analyzing problem description..."):
            time.sleep(1.5)

        prediction, confidence = predict_algorithm_from_text(problem)

        col1,col2,col3 = st.columns([1,2,1])

        with col2:
            show_prediction(prediction,confidence,[confidence])
# ------------------------------------------------
# EXPLAINABILITY
# ------------------------------------------------

elif page=="Explainability":

    st.header("Model Explainability")

    fig=plot_feature_importance(model,features)
    st.plotly_chart(fig)

    st.subheader("Decision Tree Visualization")

    X_train=joblib.load("model/X_train.pkl")
    y_train=joblib.load("model/y_train.pkl")

    viz=visualize_tree(
        model,
        X_train,
        y_train,
        features,
        encoder.classes_
    )

    components.html(viz.view()._repr_svg_(),height=800)


# ------------------------------------------------
# ALGORITHM MAP
# ------------------------------------------------

elif page == "Algorithm Map":

    st.header("Algorithm Knowledge Map")

    predicted_algo = st.session_state.get("last_prediction", "").lower()

    nodes = []
    edges = []

    # Root node
    nodes.append(Node(id="Algorithms", label="Algorithms", size=50))

    categories = {
        "Sorting": ["Merge Sort","Quick Sort","Heap Sort","Bubble Sort","Insertion Sort"],
        "Graph": ["BFS","DFS","Dijkstra","Kruskal","Prim"],
        "Dynamic Programming": ["Knapsack","LIS","Fibonacci DP"],
        "Hashing": ["HashMap","Hash Table"],
        "Search": ["Binary Search","Linear Search"],
        "Backtracking": ["Permutation","Subset","N Queens"]
    }

    # Create graph
    for category, algos in categories.items():

        nodes.append(Node(id=category,label=category,size=35))
        edges.append(Edge(source="Algorithms",target=category))

        for algo in algos:

            size = 25
            color = "#4FC3F7"

            # Glow logic
            if predicted_algo and predicted_algo in algo.lower():

                size = 45
                color = "#ff9800"

            nodes.append(
                Node(
                    id=algo,
                    label=algo,
                    size=size,
                    color=color
                )
            )

            edges.append(Edge(source=category,target=algo))

    config = Config(
        width=900,
        height=600,
        physics=True,
        directed=True,
        nodeHighlightBehavior=True,
        highlightColor="#ff9800"
    )

    agraph(nodes=nodes, edges=edges, config=config)
# ------------------------------------------------
# AI ASSISTANT
# ------------------------------------------------
elif page=="AI Assistant":

    st.header("AlgoOracle AI Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages=[]

    user_input=st.chat_input("Describe your programming problem")

    if user_input:

        st.session_state.messages.append(("user",user_input))

        result=ai_algorithm_assistant(user_input)

        response=""

        if result["algorithm"]!="Unknown":

            response+=f"### Recommended Algorithm\n**{result['algorithm']}**\n\n"

            if result["features"]:
                response+="### Detected Features\n"
                for f in result["features"]:
                    response+=f"✔ {f}\n"

            response+=f"\n### Why?\n{result['explanation']}\n"

            response+=f"\n### Time Complexity\n{result['time']}"

        else:

            response=result["explanation"]

        st.session_state.messages.append(("assistant",response))


    for role,msg in st.session_state.messages:

        if role=="user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)