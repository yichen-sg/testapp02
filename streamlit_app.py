import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Set page config first
st.set_page_config(page_title="Visible Dot", layout="centered")

# Initialize with very simple state
if 'state' not in st.session_state:
    st.session_state.state = {
        "x": 300,  # Exact center X
        "y": 200,  # Exact center Y
        "dx": 1,   # Movement step
        "running": False
    }

# Update position function
def update_pos():
    st.session_state.state["x"] += st.session_state.state["dx"]
    # Bounce off edges
    if st.session_state.state["x"] < 20 or st.session_state.state["x"] > 580:
        st.session_state.state["dx"] *= -1

# Create simple dot drawing - explicit coordinates
def get_dot():
    return {
        "version": "4.4.0",
        "objects": [{
            "type": "circle",
            "left": st.session_state.state["x"] - 20,  # 40px diameter
            "top": st.session_state.state["y"] - 20,
            "width": 20,
            "height": 20,
            "radius": 10,
            "fill": "green",  # The desired green color
            "stroke": None,
            "strokeWidth": 1,
        }]
    }

# Controls
st.title("VISIBLE RED DOT")

col1, col2 = st.columns(2)
with col1:
    if st.button("Start Movement"):
        st.session_state.state["running"] = True
with col2:
    if st.button("Stop"):
        st.session_state.state["running"] = False

# Display canvas with high contrast
st_canvas(
    background_color="#FFFFFF",  # Pure white background
    height=400,
    width=600,
    initial_drawing=get_dot(),
    key="canvas",
    drawing_mode="transform",
    display_toolbar=False
)

# Animation loop with minimal delay
if st.session_state.state["running"]:
    update_pos()
    st.rerun()

# Debug info
st.write("Dot position:", st.session_state.state["x"], st.session_state.state["y"])
