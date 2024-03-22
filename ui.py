import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title='Interactive Course Builder', page_icon='📊')
st.title('📊 Interactive Course Builder')


# Add motion to the logo
st.markdown("""
    <style>
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        img {
            animation: spin 2s linear infinite;
        }
    </style>
""", unsafe_allow_html=True)

# Logo with motion
st.image("https://icons.veryicon.com/png/o/miscellaneous/life-linear-icon/gear-29.png", width=100)


with st.expander('About this app'):
    st.markdown('**What can this app do?**')
    st.info(
        'This application helps ease the process of planning university courses by selecting the most suitable courses based on your academic/career goals in IT.')
    st.markdown('**How to use the app?**')
    st.warning(
        'To engage with the app, simply select your IT area(s) of interest from the available options.')

st.subheader('What will your university courses look like?')

# Genres selection
## Input widgets
default_genres = ['Software Development', 'Artificial Intelligence/Machine Learning', 'Cybersecurity', 'Business', 'Robotics', 'Data Science', 'Networks and Telecommunications', 'Cloud Computing']
genres_selection = st.multiselect('Select your area of interest', default_genres, default_genres)

# Course data
course_data = [
     {'Course Code': 'ECE1508H', 'Course Name': 'Special Topics in Communications: Multiuser Information Theory', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1508H-S1', 'Course Name': 'Special Topics in Communications: Network Softwarization: Technologies and Enablers', 'Disciplines': ['Networks and Telecommunications', 'Software Development']},
    {'Course Code': 'ECE1508H-S2', 'Course Name': 'Special Topics in Communications: Applied Deep Learning', 'Disciplines': ['Artificial Intelligence/Machine Learning']},
    {'Course Code': 'ECE1513H', 'Course Name': 'Introduction to Machine Learning', 'Disciplines': ['Artificial Intelligence/Machine Learning', 'Robotics']},
    {'Course Code': 'ECE1528H', 'Course Name': 'Special Topics in Data Communications: Internet of Things - From Protocols to Applications', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1543H', 'Course Name': 'Mobile Communication Systems', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1548H', 'Course Name': 'Advanced Network Architectures (Network Softwarization: Principles and Foundations)', 'Disciplines': ['Networks and Telecommunications', 'Software Development']},
    {'Course Code': 'ECE1551H', 'Course Name': 'Mobile Broadband Radio Access Network', 'Disciplines': ['Networks and Telecommunications', 'Software Development']},
    {'Course Code': 'ECE516H1', 'Course Name': 'Intelligent Image Processing', 'Disciplines': ['Software Development', 'Artificial Intelligence/Machine Learning']},
    {'Course Code': 'ECE568H1', 'Course Name': 'Computer Security', 'Disciplines': ['Cybersecurity']},
    {'Course Code': 'ECE1718H', 'Course Name': 'Special Topics in Computer Hardware Design: Hardware-Accelerated Digital Systems', 'Disciplines': ['Software Development', 'Networks and Telecommunications']},
    {'Course Code': 'ECE1718H-S3', 'Course Name': 'Special Topics in Computer Hardware Design: Advanced Computer Architecture', 'Disciplines': ['Software Development', 'Networks and Telecommunications']},
    {'Course Code': 'ECE1724H', 'Course Name': 'Special Topics in Software Systems: Artificial Intelligence', 'Disciplines': ['Software Development', 'Artificial Intelligence/Machine Learning', 'Robotics']},
    {'Course Code': 'ECE1755H', 'Course Name': 'Parallel Computer Architecture and Programming', 'Disciplines': ['Software Development', 'Networks and Telecommunications']},
    {'Course Code': 'ECE1762H', 'Course Name': 'Algorithms and Data Structures', 'Disciplines': ['Software Development', 'Robotics']},
    {'Course Code': 'ECE1770H', 'Course Name': 'Trends in Middleware Systems – Blockchain Technology', 'Disciplines': ['Software Development', 'Cybersecurity']},
    {'Course Code': 'ECE1776H', 'Course Name': 'Computer Security, Cryptography and Privacy', 'Disciplines': ['Cybersecurity']},
    {'Course Code': 'ECE1777H', 'Course Name': 'Computer Methods for Circuit Simulation', 'Disciplines': ['Software Development']},
    {'Course Code': 'ECE1779H', 'Course Name': 'Introduction to Cloud Computing', 'Disciplines': ['Software Development', 'Cloud Computing']},
    {'Course Code': 'ECE1782H', 'Course Name': 'Programming Massively Parallel Multiprocessors and Heterogeneous Systems', 'Disciplines': ['Software Development']},
    {'Course Code': 'ECE1785H', 'Course Name': 'Empirical Software Engineering', 'Disciplines': ['Software Development']},
    {'Course Code': 'ECE1228H', 'Course Name': 'Electromagnetic Theory', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1229H', 'Course Name': 'Advanced Antenna Theory', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1252H', 'Course Name': 'Introduction to Computational Electrodynamics', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1255H', 'Course Name': 'Special Topics in Electromagnetics: Integral Equation Methods for Computational Electromagnetism', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1256H', 'Course Name': 'Microwave Circuits', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1243H', 'Course Name': 'Topics in EM Waves: Advanced EM Theory', 'Disciplines': ['Networks and Telecommunications']},
    {'Course Code': 'ECE1724H', 'Course Name': 'Special Topics in Software Engineering: Bio-inspired Algorithms for Smart Mobility', 'Disciplines': ['Software Development']},
    {'Course Code': 'ECE1724H-F1', 'Course Name': 'Special Topics in Computing: Wearable AI – Building Superintelligence for People', 'Disciplines': ['Artificial Intelligence/Machine Learning', 'Software Development', 'Business']},
    {'Course Code': 'ECE1724H-F2', 'Course Name': 'Special Topics in Software Systems: Designing Modern Web-Scale Applications', 'Disciplines': ['Software Development']},
    {'Course Code': 'ECE568H1', 'Course Name': 'Computer Security', 'Disciplines': ['Cybersecurity']},
    {'Course Code': 'ECE1756H', 'Course Name': 'Reconfigurable Computing and FPGA Architecture', 'Disciplines': ['Robotics', 'Cloud Computing']},
    {'Course Code': 'ECE1779H', 'Course Name': 'Introduction to Cloud Computing', 'Disciplines': ['Cloud Computing']},
]

# Filter courses based on selected disciplines
filtered_courses = [course for course in course_data if any(discipline in course['Disciplines'] for discipline in genres_selection)]

# Display filtered courses
if filtered_courses:
    filtered_courses_df = pd.DataFrame(filtered_courses)
    st.dataframe(filtered_courses_df)
else:
    st.write('No courses found for the selected disciplines.')
