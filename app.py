import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Title of the application
st.title("Streamlit Research Study Dashboard")
# Create a sample data frame
data = pd.DataFrame({
"x": np.arange(1, 101),
"y": np.random.normal(0, 1, 100)
})
# Add a slider to select a subset of the data
subset_size = st.slider("Select the number of data points", 10, 100, 50)
st.text(subset_size)

# Display a line plot based on the selected subset size
plt.plot(data["x"][:subset_size], data["y"][:subset_size], "-o")
st.pyplot(plt)
# Add a text input for comments or notes
notes = st.text_area("Add your comments or notes here")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
