import streamlit as st

st.title("🔄 Sorting Algorithm Visualizer")

st.write("""
Welcome to the Sorting Algorithm Visualizer! This app is designed to help users 
understand and learn about various sorting algorithms through interactive visualizations. 
Here's what you can expect:
""")

# Features of the App
st.header("🌟 Features")
st.write("""
- **👁️ Interactive Visualizations**: Watch how different sorting algorithms organize data in real-time.
- **📊 Compare Algorithms**: Easily compare the efficiency and methodology of various algorithms.
- **☁️ Deployed on Cloud**: The Application can run at scale.
- **📚 Educational Insights**: Learn about the complexity and use-cases of each algorithm.
- **👍 User-Friendly Interface**: Whether you're a student, educator, or enthusiast, the app is designed for ease of use.
""")

# How to Use the App
st.header("📖 How to Use")
st.write("""
Simply select an algorithm from the list and adjust the settings as desired. 
The visualization will display how the algorithm sorts a set of random numbers and has an explanation for the algorithm.
""")

# Technical Background (Optional)
st.header("💻 Technical Background")
st.write("""
This app is built using Python and Streamlit.
It was deployed on the AWS cloud using <ADD DETAILS>
""")

# Footer
st.sidebar.info("Created by Disha with ❤️")
