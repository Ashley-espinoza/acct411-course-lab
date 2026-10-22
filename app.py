"""Streamlit entry point for the ACCT 411 archery game.

Streamlit displays the standalone browser game stored in game.html.
The animation and keyboard controls run in JavaScript inside the iframe.
"""
from pathlib import Path
import streamlit as st

# Basic page settings: wide layout gives the game enough horizontal room.
st.set_page_config(
    page_title="Archery: Cupid Has Been Fired",
    page_icon="🏹",
    layout="wide",
)

# Keep the page simple and explain where the game controls are.
st.title("🏹 Archery: Cupid Has Been Fired")
st.caption("ACCT 411 Game Lab · Version 1.0 · A very serious archery competition")
st.write("**Controls:** W = aim up · X = aim down · Spacebar = shoot · R = restart")
st.write("Click inside the game first so it receives your keyboard input.")

# Find game.html relative to this Python file rather than relying on the
# current working directory. This makes the app more reliable on Streamlit Cloud.
game_file = Path(__file__).parent / "game.html"

# Stop with a helpful message if the HTML game file was not uploaded.
if not game_file.exists():
    st.error("I cannot find game.html. Please upload game.html beside app.py in GitHub.")
else:
    # st.iframe reads a local HTML file and embeds it with its JavaScript intact.
    # The height gives the canvas and controls enough room to be visible.
   # Display the archery game inside the Streamlit page.
st.iframe(game_file, height=610)

st.caption("Version 1.0 · Targets and points are fictional. No actual chickens were harmed.")
