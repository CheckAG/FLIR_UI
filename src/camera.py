from pyflycap2.interface import Camera, CameraContext
shutter = "shutter"
gain = "gain"

class FlirCamera(object):
    def __init__(self, serial) -> None:
        
        self.serial = serial
        self.cam = Camera(serial=serial)
    
    def connect(self):
        self.cam.connect()
    
    def disconnect(self):
        self.cam.disconnect()

    def update_cam_settings(self, IT, GAIN):
        self.cam.set_cam_abs_setting_value(shutter, IT)
        self.cam.set_cam_abs_setting_value(gain, GAIN)