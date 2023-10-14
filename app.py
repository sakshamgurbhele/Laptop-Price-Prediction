import streamlit as st
import pickle
import numpy as np

# import the model
# pipe = pickle.load(open('pipe.pkl', 'rb'))
# df = pickle.load(open('df.pkl', 'rb'))

# Set the page title and favicon
st.set_page_config(page_title="Laptop Price Predictor", page_icon=":computer:")

# Add a title and description
st.title("Laptop Price Predictor")
st.write("Select the specifications of the laptop to predict its price.")

# Sidebar title and branding
st.sidebar.title("Laptop Specifications")
company = st.sidebar.selectbox('Brand', df['Company'].unique())
type = st.sidebar.selectbox('Type', df['TypeName'].unique())

# Main content for laptop specifications
st.write("## Laptop Specifications")
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.slider('Weight of the Laptop', min_value=0.0, max_value=10.0, step=0.1)
touchscreen = st.radio('Touchscreen', ['No', 'Yes'])
ips = st.radio('IPS', ['No', 'Yes'])
screen_size = st.number_input('Screen Size', min_value=10.0, max_value=20.0, step=0.1)
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('CPU', df['Cpu brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df['Gpu brand'].unique())
os = st.selectbox('OS', df['os'].unique())

# Prediction button and results
# if st.button('Predict Price'):
#     if touchscreen == 'Yes':
#         touchscreen = 1
#     else:
#         touchscreen = 0

#     if ips == 'Yes':
#         ips = 1
#     else:
#         ips = 0

#     X_res = int(resolution.split('x')[0])
#     Y_res = int(resolution.split('x')[1])
#     ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
#     query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

#     query = query.reshape(1, 12)
#     predicted_price = int(np.exp(pipe.predict(query)[0]))

    # # Display the predicted price
    # st.write("## Predicted Price")
    # st.success(f"The predicted price of this configuration is **${predicted_price:,}**")
