import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Samar's Math Logic Engine", page_icon="🎌")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    stTextInput>div>div>input { color: #00FFCC; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Symbolic Math Logic Engine")
st.caption("Bridging JEE Advanced Mathematics to Japanese Engineering Standards")
st.sidebar.header("📚 Engineering Toolkit")
show_formula = st.sidebar.checkbox("Show EJU/JEE Formula Sheet")

if 'history' not in st.session_state:
    st.session_state.history = []

#main
user_query = st.text_input("Enter a mathematical function (use Python syntax like x**2, sin(x), exp(x))", "x**3 - 3*x**2 + 2")
x = sp.Symbol('x')

try:
    expr = sp.sympify(user_query)
    deriv = sp.diff(expr, x)
    integ = sp.integrate(expr, x)
    
    st.write("### 🔍 Symbolic Analysis")
    c1, c2 = st.columns(2)
    with c1:
        st.info("First Derivative")
        st.latex(f"f'(x) = {sp.latex(deriv)}")
    with c2:
        st.success("Indefinite Integral")
        st.latex(f"\\int f(x)dx = {sp.latex(integ)} + C")
    if expr.is_polynomial(x):
        roots = sp.solve(expr, x)
        st.write(f"**Real Roots:** { [r.evalf(3) for r in roots if r.is_real] }")

    st.write("### 📈 Visual Proof")
    f_num = sp.lambdify(x, expr, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    
    #math errors
    try:
        y_vals = f_num(x_vals)
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x_vals, y_vals, color='#00FFCC', label="f(x)")
        ax.axhline(0, color='white', linewidth=0.5)
        ax.axvline(0, color='white', linewidth=0.5)
        ax.set_facecolor('#0e1117')
        fig.patch.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        ax.legend()
        st.pyplot(fig)
    except:
        st.warning("Visualization suppressed: Function out of real-number bounds for plotting.")

    if st.button("Save to Portfolio History"):
        st.session_state.history.append(f"f(x) = {user_query}")

except Exception as e:
    st.error(f"Logic Error: Please ensure you are using valid Python operators (e.g., * for multiplication).")

#sidebar Formula
if show_formula:
    st.sidebar.markdown("""
    ---
    **Calculus Basics:**
    - $\\frac{d}{dx} \sin(x) = \cos(x)$
    - $\\int \frac{1}{x} dx = \ln|x|$
    - Euler's: $e^{i\\theta} = \cos\\theta + i\sin\\theta$
    """)

if st.session_state.history:
    st.sidebar.write("### 🕒 Recent Solves")
    for h in st.session_state.history[-5:]:
        st.sidebar.text(h)
