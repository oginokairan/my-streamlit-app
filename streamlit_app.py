import streamlit as st
import squadbase.streamlit as sq

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Get Squadbase user information
user_info = sq.auth.get_user()

# Store in session state for reuse
st.session_state['user_info'] = user_info

# Access user data
st.write(f"Welcome, {user_info.get('firstName', '')} {user_info.get('lastName', '')}")

st.write("---")

st.write(user_info)
