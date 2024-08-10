import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header
from utils import *
import matplotlib.pyplot as plt

user_input = st.container()
# Set a placeholder for the plot
plot_placeholder = st.empty()
# Initialize session state if not already done
if "loop_active" not in st.session_state:
    st.session_state.loop_active = False

def toggle_loop():
    st.session_state.loop_active = not st.session_state.loop_active

with user_input:
    on = st.toggle(label="Live_view", key="live", on_change=toggle_loop)
    number_of_repeats = st.number_input(label="set the number of averages",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key="number_of_repeats",
                    step=1)

    while st.session_state.loop_active:
        img_averaged = np.zeros((2048,))
        for i in range(number_of_repeats):
            st.session_state.cam.start_capture()
            st.session_state.cam.read_next_image()
            image = st.session_state.cam.get_current_image()  # last image
            img_np = np.frombuffer(image['buffer'], dtype=np.uint16).reshape((image['rows'], image['cols']))
            img_averaged += img_np.mean(axis=0)
            st.session_state.cam.stop_capture()
        img_averaged = img_averaged/number_of_repeats
        fig, ax = plt.subplots(figsize=(10, 6))
        # Plot the final average array
        ax.plot(img_averaged)
        ax.set_title('Live View')
        ax.set_xlabel('Pixels')
        ax.set_ylabel('Intensity')
        ax.grid(True)
        plot_placeholder.pyplot(fig)
        if not st.session_state.loop_active:
            break
    img_averaged = np.zeros((2048,))
    for i in range(number_of_repeats):
        st.session_state.cam.start_capture()
        st.session_state.cam.read_next_image()
        image = st.session_state.cam.get_current_image()  # last image
        img_np = np.frombuffer(image['buffer'], dtype=np.uint16).reshape((image['rows'], image['cols']))
        img_averaged += img_np.mean(axis=0)
        st.session_state.cam.stop_capture()
    img_averaged = img_averaged/number_of_repeats
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot the final average array
    ax.plot(img_averaged)
    ax.set_title('Live View')
    ax.set_xlabel('Pixels')
    ax.set_ylabel('Intensity')
    ax.grid(True)
    plot_placeholder.pyplot(fig)