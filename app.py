import streamlit as st

# 1. MUST BE FIRST: Page Configuration
st.set_page_config(page_title="Owl AI Portal", page_icon="🦉", layout="wide")

# 2. Custom Styling (The "Overlay" Logic)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    [data-testid="stSidebar"] { background-color: #161b22; }
    
    /* 1. The Container for the Banner */
    .hero-container {
        position: relative;
        width: 100%;
        height: 300px;
        margin-bottom: 30px;
    }

    /* 2. The Image Styling */
    .hero-container img {
        width: 100%;
        height: 300px;
        object-fit: cover;
        border-radius: 15px;
        filter: brightness(60%); /* Dims image so text is easy to read */
    }

    /* 3. The Text Overlay Styling */
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        width: 100%;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.6);
        pointer-events: none; /* Allows clicks to pass through to the image if needed */
        font-family: 'Inter', sans-serif;
    }

    .nav-header { font-size: 24px; font-weight: bold; color: #1f77b4; text-align: center; }
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation Bar
with st.sidebar:
    st.markdown('<p class="nav-header">🦉 OWL AI MENU</p>', unsafe_allow_html=True)
    choice = st.radio("Go to:", ["🏠 Home", "📄 Offer Letter", "📋 Tasks", "📤 Submission"])
    st.markdown("---")
    st.info("Log: January Intern Session")

# 4. Logic to switch between "Pages"
if choice == "🏠 Home":
    # --- HERO SECTION START ---
    # We use a single markdown block to create the image and the text overlap
    st.markdown(f'''
        <div class="hero-container">
            <img src="https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1200">
            <div class="hero-text">Welcome to the Owl AI Portal</div>
        </div>
    ''', unsafe_allow_html=True)
    # --- HERO SECTION END ---

    st.write("### Instructions")
    st.write("Please search for your name and download your offer letterin the Drive folder given below. After downloading, open the Tasks section to review your assigned tasks. Read all information on the site carefully and ensure you understand the details..")

elif choice == "📄 Offer Letter":
    st.title("Download Offer Letter")
    name = st.text_input("Enter your full name to verify:")
    if name:
        st.success(f"Verification successful for {name}!")
        st.link_button("Click here to Download PDF", "https://your-google-drive-link.com")

elif choice == "📋 Tasks":
    st.title("January Internship Tasks")
    st.info("Select your specific internship domain below to view your assigned tasks.")

    # Custom CSS to make these specific buttons match your screenshot's blue style
    st.markdown("""
        <style>
        div.stLinkButton > a {
            background-color: #1f77b4 !important;
            color: white !important;
            width: 100% !important;
            border-radius: 5px !important;
            height: 3em !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            margin-bottom: 10px !important;
            text-decoration: none !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # Task Category Buttons
    st.link_button("DATA ANALYST INTERN TASKS", "https://your-link-here.com")
    st.link_button("AIML INTERN TASKS", "https://your-link-here.com")
    st.link_button("PYTHON DEVELOPER INTERN TASKS", "https://your-link-here.com")
    st.link_button("FULL STACK DEVELOPMENT INTERN TASKS", "https://your-link-here.com")
    st.link_button("JAVA DEVELOPER INTERN TASKS", "https://your-link-here.com")
    st.link_button("FRONT END DEVELOPER INTERN TASKS", "https://your-link-here.com")
    st.link_button("DATA STRUCTURES AND ALGORITHMS INTERN TASKS", "https://your-link-here.com")

elif choice == "📤 Submission":
    st.title("Project Submission")
    st.write("Please upload your final project links below.")
    st.link_button("Open Submission Form", "https://your-google-form-link.com")