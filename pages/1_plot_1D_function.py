import streamlit as st
import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, sqrt, log
import pandas as pd
import matplotlib.pyplot as plt

import mpld3
import streamlit.components.v1 as components


st.set_page_config(
    page_title = 'Plot 1D functions',
    page_icon = "📝",
    layout = "centered"
    )
    
if 'rows' not in st.session_state:
    st.session_state['rows'] = 0
if 'fig_html' not in st.session_state:
    st.session_state.fig_html = ''
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")
    
def display_input_row(index):
    col1, col2= st.columns([1, 10])
    col1.subheader("")
    col1.write("f(x) = ")
    col2.text_input(f'Function {index} : enter an expression with x :', 'x + 20', key=f'Function_{index}')

def increase_rows():
    st.session_state['rows'] += 1
def decrease_rows():
    st.session_state['rows'] -= 1

def form_callback():
    if st.session_state['rows'] > 0 :
        x = np.linspace(st.session_state.x_min, st.session_state.x_max, 100)
        for i in range(st.session_state['rows']):
            try :
                # st.write("y="+st.session_state[f'Function_{i}'])
                exec("y="+st.session_state[f'Function_{i}'])
            except:
                st.write(f'Function_{i} is not valid')
            else : 
                ax.plot(x, locals()['y'], label=f'Function {i}')
        ax.legend()
        st.session_state.fig_html = mpld3.fig_to_html(fig)


with st.container():
    st.markdown(
        """
        # Plot 1D functions $y=f(x)$
        ## Here you can enter expressions of functions, valid expressions are :

        - Usual expressions : +, -, *, /
        - Power law : **
        - Trigonometric functions : cos(), sin(), tan(), arccos(), arcsin(), arctan()
        - Exponential & logarithmic functions : exp(), log()
        - Square function : sqrt()
        
        ---
    """
    )

    st.subheader('👇Push the following button to add/delete a function')

    col1, col2 = st.columns(2)
    col1.button('Add function', on_click=increase_rows)
    col2.button('Delete function', on_click=decrease_rows)
    st.write('---')

    for i in range(st.session_state['rows']):
        display_input_row(i)

with st.form(key='my_form'):
    col1, col2= st.columns(2)
    x_left = col1.number_input('x min',value = -5.0,  key='x_min')
    x_right = col2.number_input('x max', value =5.0, key='x_max')
    submit_button = st.form_submit_button(label='Plot', on_click=form_callback)


with st.container():
    
    components.html(st.session_state.fig_html, height=600)
