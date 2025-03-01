import streamlit as st 
import pandas as pd
import time

st.title("Startup Dashboard")
st.header("I am Learning Streamlit")
st.subheader("I am Loving it")
st.write("I am writing")

# Mark Down: https://www.markdownguide.org/ ( like jupyter markdown)
st.markdown("""
### This is a markdown
- markdown 1            
- markdown 2            
- markdown 3       
""")


#Displaying code:
st.code("""
def Square(input):
    return input**2
        
square(4)
""")

# Latex: For displaying mathematical term or equations.
st.latex('x^2 + y^2 = 0')

# Displaying dataframe:
df = pd.DataFrame({
    'name': ["Vedant","Nitish","Girish"],
    'marks': [80,90,100],
    'package':[12,34,32]
    })

st.dataframe(df)

# Metrics:
st.metric('Revenue','Rs.3.10L','+3%')

#Displaying JSON:

st.json({
    'name': ["Vedant","Nitish","Girish"],
    'marks': [80,90,100],
    'package':[12,34,32]
    })

#-------------------------#
#Displaying Media:

#st.image
#st.video()

#-------------------------#
#Creating Layouts:

#1. Sidebar
st.sidebar.title("Side bar Section")

# Creating column

col1, col2 = st.columns(2)
with col1:
    st.write("Col 1")
with col2:
    st.write("col 2")


# progress status:
st.error("Login error")

st.success('success')
st.info('info')
st.warning('warning')

#Progress bar:

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

# Taking user input:

email = st.text_input('Enter email')
number = st.number_input("Enter Age")
date = st.date_input("Enter date")