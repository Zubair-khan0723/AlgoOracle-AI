import streamlit as st

def initialize_session(features):

    if "answers" not in st.session_state:
        st.session_state.answers = {f: None for f in features}

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0


def reset_session(features):

    st.session_state.answers = {f: None for f in features}
    st.session_state.current_question = 0