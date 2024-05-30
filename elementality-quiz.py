import streamlit as st
import re
import time

# Initialize session state variables
if "animation_shown" not in st.session_state:
    st.session_state.animation_shown = False
    st.session_state.full_response = ""
    st.session_state.current_question = 0
    st.session_state.answers = [None] * 10
    st.session_state.show_results = False

# Functions to handle navigation
def next_question():
    if st.session_state.current_question < len(questions) - 1:
        st.session_state.current_question += 1

def previous_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1

def show_results():
    st.session_state.show_results = True

# Header and introduction
st.header('''
  Elementality: The Quiz''')
st.subheader("Which group of the periodic table are you?")
st.markdown('Made by: Rashmi Nair, MYP 3A', unsafe_allow_html=True)

# Animation
if not st.session_state.animation_shown:
    with st.chat_message("ai"):
        message_placeholder = st.empty()
        ai_response = ("Hey there! I'm Rashmi, a student of MYP 3A.\n"
                       "We learnt about the Periodic Table in our first unit of Chemistry.\n"
                       "To apply my knowledge, I've designed this quiz.\n"
                       "Answer these 10 questions to find out which group of the Periodic Table you are. Have fun!")
        full_response = ""
        for chunk in re.split(r'\s+', ai_response):
            full_response += chunk + " "
            time.sleep(0.07)
            message_placeholder.markdown(full_response + "➤")
        st.session_state.full_response = full_response
        st.session_state.animation_shown = True
else:
    st.chat_message("ai").markdown(st.session_state.full_response + "➤")

# Questions and options
questions = [
    ("Party animal or solo wanderer?", ["Party animal, the more the merrier! :partying_face:", "Solo wanderer, I like spending time alone recharging :person_in_lotus_position:"]),
    ("Pressure or peace?", ["Can handle pressure :weight_lifter:", "Serene and steady, those are the environments that I love :relieved:"]),
    ("Attention or none?", ["Center of attention, always! :tada:", "Quiet, but confident, observer :eyes:"]),
    ("Dynamic or static?", ["Dynamic, I live a fast-paced life :fast_forward:", "Static, I like sticking to routines :double_vertical_bar:"]),
    ("Group or individual?", ["Team player :handshake:", "Solo :technologist:"]),
    ("Emotional or not?", ["Emotional, I feel emotions intensely :gift_heart:", "Monotonous, I stay calm and think before reacting :tv:"]),
    ("Seeking knowledge?", ["Seeker, I love learning new things :mag:", "Contented, I'm happy with what I already know :brain:"]),
    ("Trends or utility?", ["Trendy, I express myself through the newest trends :dress:", "Comfort, I prioritize comfort and functionality over looks :tshirt:"]),
    ("Open or private?", ["Open, I love sharing my thoughts and feelings :unlock:", "Private, I often keep to myself :closed_lock_with_key:"]),
    ("Restless or collected?", ["Energetic, I have a lot of energy and live a fast-paced life :zap:", "Collected, I like relaxing and taking it slow :mountain:"])
]

# Display the current question
question, options = questions[st.session_state.current_question]
st.divider()
st.subheader(question)
st.session_state.answers[st.session_state.current_question] = st.radio(
    "",
    options,
    index=0 if st.session_state.answers[st.session_state.current_question] is None else options.index(st.session_state.answers[st.session_state.current_question])
)

# Navigation buttons
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.session_state.current_question > 0:
        st.button(":arrow_left:", on_click=previous_question, key="previous")
with col2:
    pass
with col3:
    if st.session_state.current_question < len(questions) - 1:
        st.button(":arrow_right:", on_click=next_question)
    else:
        st.button("Your group ➤", on_click=show_results, use_container_width=True)

# Check conditions based on answers
def check_cond1():
    return (st.session_state.answers[0] == "Party animal :partying_face:" and
            st.session_state.answers[2] == "Center of attention, always! :tada:" and
            st.session_state.answers[7] == "Trendy :dress:" and
            st.session_state.answers[8] == "Open :unlock:" and
            st.session_state.answers[9] == "Energetic :zap:")

def check_cond2():
    return (st.session_state.answers[1] == "Can handle pressure :weight_lifter:" and
            st.session_state.answers[3] == "Dynamic :fast_forward:" and
            st.session_state.answers[4] == "Team :handshake:")

def check_cond3():
    return (st.session_state.answers[1] == "Serene and steady :relieved:" and
            st.session_state.answers[4] == "Team :handshake:" and
            st.session_state.answers[5] == "Emotional :gift_heart:")

def check_cond4():
    return (st.session_state.answers[3] == "Dynamic :fast_forward:" and
            st.session_state.answers[6] == "Contented :brain:" and
            st.session_state.answers[7] == "Trendy :dress:")

def check_cond5():
    return (st.session_state.answers[3] == "Static :double_vertical_bar:" and
            st.session_state.answers[6] == "Contented :brain:" and
            st.session_state.answers[9] == "Collected :mountain:")

def check_cond6():
    return (st.session_state.answers[1] == "Serene and steady :relieved:" and
            st.session_state.answers[4] == "Solo :technologist:" and
            st.session_state.answers[8] == "Private :closed_lock_with_key:" and
            st.session_state.answers[9] == "Collected :mountain:")

if st.session_state.show_results:
    if check_cond1():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("alkalis.jpg", use_column_width=True)
            st.header("You're an alkali metal!")
            st.markdown("You're extroverted, the life of the party, and quite **eye-catching**!")
            st.balloons()
        with col3:
            st.divider()
    elif check_cond2():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("transition metals.jpeg", use_column_width=True)
            st.header("You're a transition metal!")
            st.markdown("You're hard working, **adaptable**, and tough, but dependable!")
            st.balloons()
    elif check_cond3():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("halogens.jpeg", use_column_width=True)
            st.header("You're a halogen!")
            st.markdown("You're independent, competitive, and keep to yourself, but are quite **dangerous if provoked**!")
            st.balloons()
    elif check_cond4():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("metalloids.jpg", use_column_width=True)
            st.header("You're a metalloid!")
            st.markdown("You're **different, but unique**!")
            st.balloons()
    elif check_cond5():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("non-metals.jpg", use_column_width=True)
            st.header("You're a non-metal!")
            st.markdown("You value alone time, but are **unique** and easygoing!")
            st.balloons()
    elif check_cond6():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.image("noble gases.jpeg", use_column_width=True)
            st.header("You're a noble gas!")
            st.markdown("You're calm and collected, have **everything sorted out**, and hate drama!")
            st.balloons()
    else:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.divider()
        with col2:
            st.divider()
            st.header("You're a mix!")
            st.markdown("You're **a mix** of many groups!")
            st.balloons()
