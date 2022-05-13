# Modules
import cv2
import streamlit as st
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# QR Code
import qrcode
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=14)

# Load image
from PIL import Image
def load_image(img):
    im = Image.open(img)
    return im

# Application
def main():
    menu = ["Home", "Decode QR", "Kelompok Y"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        
        # Text input
        with st.form(key='myqr_form'):
            raw_text = st.text_area("Text here")
            submit_button = st.form_submit_button("Generate")

        # Layout
        if submit_button:         
            col1, col2 = st.columns(2)            
            with col1:                
                # Add data
                qr.add_data(raw_text)
                
                # Generate QR
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')
                
                # Filename
                img_filename = 'QR_image_{}.png'.format(timestr)
                
                # Save file
                path_for_image = os.path.join('image_folder', img_filename)
                img.save(path_for_image)
            
                final_img = load_image(path_for_image)
                st.image(final_img)
            
            with col2:
                st.info("Original Text")
                st.write(raw_text)
        
    elif choice == "Decode QR":
        st.subheader("Decode QR")

        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
        
        if image_file is not None:            
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
        st.title("Kelompok Y")
        st.write("1. Handoko Bimawidjaya - 152163240100-512")
        st.write("2. Handoyo Wahyu Utomo - 152163240100-889")

if __name__ == '__main__':
    main()
