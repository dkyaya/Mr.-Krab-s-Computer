import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Krabby Computer", layout="wide")

# --- SESSION STATE FOR LOGIN ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN FORM ---
def login():
    st.title("🔒 Krabby Computer Login")
    password = st.text_input("Enter password:", type="password")

    if st.button("Login"):
        if password == "Pearl0315":
            st.session_state.logged_in = True
        else:
            st.error("Incorrect password. Try again.")

# --- DESKTOP VIEW ---
def desktop():
    st.markdown(
        """
        <style>
        .desktop-bg {
            background-image: url('https://via.placeholder.com/1600x900/006400/ffffff?text=They+say+real+treasure+is+printed+on+the+green.');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: start;
            padding: 2rem;
            color: white;
        }
        .desktop-icons {
            margin-top: 2rem;
            display: flex;
            gap: 2rem;
        }
        .icon {
            width: 100px;
            height: 100px;
            background-color: rgba(255,255,255,0.1);
            border: 2px solid white;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 0.9rem;
            text-align: center;
            cursor: pointer;
        }
        </style>
        <div class="desktop-bg">
            <h1>🖥 Krabby Computer</h1>
            <div class="desktop-icons">
                <div class="icon">File Cabinet</div>
                <div class="icon">Expenses</div>
                <div class="icon">Mystery App</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add logout button in sidebar
    if st.sidebar.button("🔓 Log Out"):
        st.session_state.logged_in = False
        st.rerun()

# --- ROUTING ---
if not st.session_state.logged_in:
    login()
else:
    desktop()
