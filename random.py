import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import math

# Sidebar content
with st.sidebar:
    st.title("Math multi-calculator")
    st.markdown('''
                ## About
                This app is an Math multi-calculator:
                - [Streamlit]
                        
                ''')
    add_vertical_space(5)
    st.write('Made with love')

class Circle:
    def __init__(self, radius):
        self._radius = radius
        
    def get_circunference(self):
        return self._radius*math.pi*2
        
    def get_area(self):
        return math.pi*self._radius**2

radius = st.text_input("Enter a circle radius: ")

if st.button("Calculate circle area and circunference"):
    st.write("Calculating...")

    c = Circle(float(radius))
    area = c.get_area()
    circunference = c.get_circunference()

    st.write(f'Area: {area}')
    st.write(f'Circunference: {circunference}')
