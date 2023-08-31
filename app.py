# Save this as "app.py" in your Colab directory
import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Among 3 Numbers")
st.write("Enter three numbers and find the largest one.")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    largest = find_largest(num1, num2, num3)
    st.write(f"The largest number is: {largest}")
