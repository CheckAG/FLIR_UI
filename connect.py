import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.colored_header import colored_header
from utils import *

st.set_page_config(page_title="Flir Setup", page_icon="🔭")
st.session_state.update(st.session_state)
st.title(":blue[Welcome to Flir Setup]")

st.session_state
user_input = st.container()
if 'page_0' not in st.session_state:
    st.session_state.page_0 = {
        'continue_btn_state' : True
    }
    st.session_state["cam"] = None

with user_input:
    st.subheader("Please select the Serial port to connect")
    serial_number = st.selectbox(label="_**Available ports_**",
                                 key="serial_number",
                                 options=scan_devices())
    col1, col2 = st.columns(2)
    with col1:
        connect_btn = st.button(label="Connect", 
                                help="Click to connect to camera",
                                on_click=connect_device, args=[serial_number])
    with col2:
        disconnect_btn = st.button(label="Disconnect", 
                                help="Click to disconnect from camera",
                                on_click=disconnect_device)
    if st.session_state.cam is not None:
        st.subheader("Please set the values for camera")
        IT = st.slider(label="_**set integration time (in seconds)_**",
                       min_value=st.session_state.cam.get_cam_abs_setting_range(shutter)[0],
                       max_value=st.session_state.cam.get_cam_abs_setting_range(shutter)[1],
                       key="IT",
                       value=st.session_state.cam.get_cam_abs_setting_value(shutter),
                       step=0.1)
        GAIN =  st.slider(label="_**set gain_**",
                       min_value=st.session_state.cam.get_cam_abs_setting_range(gain)[0],
                       max_value=st.session_state.cam.get_cam_abs_setting_range(gain)[1],
                       key="gain",
                       value=st.session_state.cam.get_cam_abs_setting_value(gain),
                       step=0.5)
        st.button(label="Update",
                  help="Update the camera settings",
                  on_click=update_cam_settings(IT, GAIN))
        
    continue_btn = st.button("Continue", help="Click to sumbit and navigate to next page", disabled=st.session_state.page_0['continue_btn_state'])

    if continue_btn:
        switch_page("Live")
        

    
