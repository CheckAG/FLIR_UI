from pyflycap2.interface import Camera, CameraContext
import streamlit as st


shutter = "shutter"
gain = "gain"

def scan_devices():
    cc = CameraContext()
    cc.rescan_bus()
    return cc.get_gige_cams()

def connect_device(serian_number):
    try:
        cam = Camera(serial=serian_number)
        st.session_state.cam = cam
        st.session_state.cam.connect()
        st.success(f"Connected to device {serian_number} successfully")
        st.session_state.page_0['continue_btn_state'] = False
    except:
        st.error("Error in connecting to device")

def disconnect_device():
    try:
        st.session_state.cam.disconnect()
        st.session_state.cam = None
        st.session_state.page_0['continue_btn_state'] = True
        st.success(f"Disconnected from device {st.session_state.serial_number} successfully")
    except:
        st.error("Error in discoonecting from device")

def update_cam_settings(IT, GAIN):

    st.session_state.cam.set_cam_abs_setting_value(shutter, IT)
    st.session_state.cam.set_cam_abs_setting_value(gain, GAIN)
    st.success("Updated settings!!")