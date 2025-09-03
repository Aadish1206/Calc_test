import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            color: #333;
            font-family: 'Segoe UI', sans-serif;
        }
        .calculator-box {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border: none;
            border-radius: 5px;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- App Title ----------
st.title("🧮 Professional Calculator")

st.markdown("Use the calculator below to perform basic operations.")

# ---------- Calculator UI ----------
with st.container():
    with st.form("calc_form"):
        st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Enter first number", format="%.4f")
        with col2:
            num2 = st.number_input("Enter second number", format="%.4f")

        operation = st.selectbox(
            "Select operation",
            ("Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"),
        )

        submitted = st.form_submit_button("Calculate")

        result = None
        error = None

        if submitted:
            try:
                if operation == "Addition":
                    result = num1 + num2
                elif operation == "Subtraction":
                    result = num1 - num2
                elif operation == "Multiplication":
                    result = num1 * num2
                elif operation == "Division":
                    if num2 == 0:
                        error = "Error: Division by zero"
                    else:
                        result = num1 / num2
                elif operation == "Exponentiation":
                    result = num1 ** num2
            except Exception as e:
                error = f"An error occurred: {str(e)}"

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Display Result ----------
if submitted:
    st.subheader("Result:")
    if error:
        st.error(error)
    else:
        st.success(f"The result of {operation.lower()} is: **{result:.4f}**")
