################################################################################

# Fintech Finder

################################################################################
# Imports

import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Import functions from the `crypto_wallet.py` file:
from crypto_wallet import w3, generate_account, get_balance, send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $2,740
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Mark": ["Mark", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/mark.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Mark", "Jo", "Kendall"]


def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Set page configuration
st.set_page_config(page_title="FinTech Finder", page_icon="👔", layout="wide")

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code
# Account details

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Create a HD wallet and Ethereum account
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Call `get_balance` function and pass account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3, account.address))

##########################################
# Streamlit Sidebar Code (continued)
# Find candidate

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Sign and Execute a Payment Transaction

# Calculate total `wage` for the candidate
wage = hours*candidate_database[person][3]

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

# Create `send transaction` button
if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function
    transaction_receipt= send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Receipt")

    # Write the returned transaction receipt to the screen
    st.sidebar.write(transaction_receipt)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()

#####################################################
# Hide Streamlit Style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

################################################################################
# Inspect the Transaction

# Launch the Streamlit application on the integrated terminal with `streamlit run fintech_finder.py`.

# On the resulting webpage, select a candidate that you would like to hire from the appropriate drop-down menu. 
# Then, enter the number of hours that you would like to hire them for.

# Click the Send Transaction button to sign and send the transaction with your Ethereum account information. 
# If the transaction is successfully communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit application sidebar.