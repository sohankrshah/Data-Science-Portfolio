import streamlit as st
from header import create_sidebar, get_current_page

# Configure Streamlit page
st.set_page_config(
    page_title="KARTS BAZAR",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS to hide Deploy button and status widget
st.markdown("""
<style>
.stDeployButton {
    display: none !important;
}
[data-testid="stStatusWidget"] {
    display: none !important;
}
.page-content {
    margin-left: 220px; /* Match sidebar width */
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

def main():
    # Render sidebar navigation
    create_sidebar()

    # Main content container
    st.markdown('<div class="page-content">', unsafe_allow_html=True)
    current_page = get_current_page()

    # Example content based on current page
    if current_page == "Home":
        st.title("🏠 Welcome to KARTS BAZAR")
        st.write("This is the home dashboard.")
    elif current_page == "Overview":
        st.title("📊 Overview")
        st.write("Here’s a summary of your activity.")
    elif current_page == "Portfolio":
        st.title("💼 Portfolio")
        st.write("Your portfolio details go here.")
    elif current_page == "Contact":
        st.title("📞 Contact Us")
        st.write("Reach out to us anytime.")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
