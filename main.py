import streamlit as st
import pandas as pd
import json
# Import necessary functions or modules
from functions import radio_select, text_input, export_to_csv

st.set_page_config(layout="wide")

# Load proposal sections from the JSON file
with open("proposal_sections.json", "r") as json_file:
    st.session_state.proposal_sections = json.load(json_file)


# Define the main function to render different sections based on sidebar selection
def main():
    st.sidebar.title("Clients Details")
    client_name = st.sidebar.text_input("Enter client name:", placeholder="Please enter client name here", value=st.session_state.get("client_name", ""))
    # Store client's name in session state
    st.session_state.client_name = client_name

    # Initiate solution option if not already set
    if 'selected_solution' not in st.session_state:
        # If selected_solution is not yet stored in session state, initialize it with the default value
        selected_solution = st.sidebar.selectbox("Select proposal solution:", ["ILA", "Gen AI"], placeholder="Choose an option")
        # Store the selected solution in session state
        st.session_state.selected_solution = selected_solution
    else:
        # Display the selectbox with the default value
        selected_solution = st.sidebar.selectbox("Select proposal solution:", ["ILA", "Gen AI"], placeholder="Choose an option", index=["ILA", "Gen AI"].index(st.session_state.selected_solution ))  
        # Store the selected solution in session state
        st.session_state.selected_solution = selected_solution

    page = st.sidebar.selectbox("Go to", ["Key Challenges", "Solutions Aspect", "Summary"])

    if page == "Main Menu":
        render_page_1()
    elif page == "Key Challenges":
        render_page_2()
    elif page == "Solutions Aspect":
        render_page_3()
    elif page == "Summary":
        render_page_4()

# Define functions to render each page
def render_page_1():
    st.title("Clients Details:")
    # Initiate client name
    client_name = st.text_input("Enter client name:", placeholder="Please enter client name here", value=st.session_state.get("client_name", ""))
    # Store client's name in session state
    st.session_state.client_name = client_name

    # Initiate solution option if not already set
    if 'selected_solution' not in st.session_state:
        # If selected_solution is not yet stored in session state, initialize it with the default value
        selected_solution = st.selectbox("Select proposal solution:", ["ILA", "Gen AI"], placeholder="Choose an option")
        # Store the selected solution in session state
        st.session_state.selected_solution = selected_solution
    else:
        # Display the selectbox with the default value
        selected_solution = st.selectbox("Select proposal solution:", ["ILA", "Gen AI"], placeholder="Choose an option", index=["ILA", "Gen AI"].index(st.session_state.selected_solution ))  
        # Store the selected solution in session state
        st.session_state.selected_solution = selected_solution
    
    if st.button("Next"):
        print("Hello next button pressed")

def render_page_2():
    # Retrieve solution option from session state
    selected_solution = st.session_state.selected_solution

    if 'selected_options' not in st.session_state:
        st.session_state.selected_options = {}

    # Retrieve client's name from session state
    client_name = st.session_state.client_name

    # Retrieve proposal_sections from session state
    proposal_sections = st.session_state.proposal_sections

    # Initialize DataFrame to store user inputs
    if 'user_inputs' not in st.session_state:
        st.session_state.user_inputs = pd.DataFrame(columns=['Solution','Category', 'Sub-Category', 'Importance', 'User Input'])

    st.title(f"Key Challenges - *{st.session_state.selected_solution}* for *{st.session_state.client_name}*")
    radio_select(selected_solution, proposal_sections[st.session_state.selected_solution]["Key Challenges"])

    capture_key_challenges = st.session_state.user_inputs[(st.session_state.user_inputs['Category'] == 'Key Challenges') & (st.session_state.user_inputs['Solution'] == selected_solution)]

    # Display the captured data DataFrame
    with st.expander("See Captured data"):
        st.write(capture_key_challenges)

def render_page_3():
    # Retrieve solution option from session state
    selected_solution = st.session_state.selected_solution

    if 'selected_options' not in st.session_state:
        st.session_state.selected_options = {}

    # Retrieve client's name from session state
    client_name = st.session_state.client_name

    # Retrieve proposal_sections from session state
    proposal_sections = st.session_state.proposal_sections

    # Initialize DataFrame to store user inputs
    if 'user_inputs' not in st.session_state:
        st.session_state.user_inputs = pd.DataFrame(columns=['Solution','Category', 'Sub-Category', 'Importance', 'User Input'])

    st.title(f"Solutions Aspect - *{st.session_state.selected_solution}* for *{st.session_state.client_name}*")
    text_input(selected_solution, proposal_sections[st.session_state.selected_solution]["Solution Aspect"])

    capture_solution_aspects = st.session_state.user_inputs[(st.session_state.user_inputs['Category'] == 'Solutions Aspect') & (st.session_state.user_inputs['Solution'] == selected_solution)]

    # Display the captured data DataFrame
    with st.expander("See Captured data"):
        st.write(capture_solution_aspects)

def render_page_4():
    # Retrieve solution option from session state
    selected_solution = st.session_state.selected_solution

    # Retrieve user inputs DataFrame from session state
    user_inputs = st.session_state.user_inputs[st.session_state.user_inputs['Solution'] == selected_solution]

    # Page title
    st.title("Solutions Overview")

    # Display user inputs DataFrame
    st.write(user_inputs)

    # Export to CSV button
    if st.button("Export to CSV"):
        export_to_csv(user_inputs)

# Entry point of the application
if __name__ == "__main__":
    main()
