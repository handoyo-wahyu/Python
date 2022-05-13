import streamlit as st
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import cv2

import qrcode
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=14)

from PIL import Image
def load_image(img):
    im = Image.open(img)
    return im

def main():
    menu = ["Home", "DecodeQR", "Kelompok Y"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        
        with st.form(key='myqr_form'):
            raw_text = st.text_area("Text here")
            submit_button = st.form_submit_button("Generate")

        if submit_button:
            
            col1, col2 = st.columns(2)
            
            with col1:
                
                qr.add_data(raw_text)
                
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')
                img_filename = 'QRimage_{}.png'.format(timestr)
                path_for_image = os.path.join('image_folder', img_filename)
                img.save(path_for_image)
            
                final_img = load_image(path_for_image)
                st.image(final_img)
            
            with col2:
                st.info("Original Text")
                st.write(raw_text)
        
    elif choice == "DecodeQR":
        st.subheader("DecodeQR")

        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
        
        if image_file is not None:
            # Method 1
            #img = load_image(image_file)
            #st.image(img)
            
            # Method 2
            file_bytes = np.asarray(bytearray(image_file.read()),dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes,1)
            
            c1, c2 = st.columns(2)
            with c1:
                st.image(opencv_image)
                
            with c2:
                st.info("Decode QR Code")
                det = cv2.QRCodeDetector()
                retval,points,straight_qrcode = det.detectAndDecode(opencv_image)

                st.write(retval)
            
    else:
        st.subheader("Kelompok Y")
        
if __name__ == '__main__':
    main()
