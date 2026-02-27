import streamlit as st
import sympy as sp

# Initialize session state to store history
if 'history' not in st.session_state:
    st.session_state.history = []

st.sidebar.title("History")

# ... (Existing Math Engine Code) ...

if st.button("Solve & Save"):
    # Perform symbolic logic
    expr = sp.sympify(user_query)
    deriv = sp.diff(expr, x)
    
    # Save to history
    st.session_state.history.append(f"f(x)={user_query} | f'(x)={deriv}")

# Display History in the Sidebar
for item in st.session_state.history:
    st.sidebar.write(item)