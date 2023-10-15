import streamlit as st
import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, sqrt, log
import pandas as pd
import matplotlib.pyplot as plt

import mpld3
import streamlit.components.v1 as components

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")

st.markdown(
    """
    # Plot 2D functions $z=f(x,y)$
    ## Here you can enter expressions of functions, valid expressions are :

    - Usual expressions : +, -, *, /
    - Power law : **
    - Trigonometric functions : cos(), sin(), tan(), arccos(), arcsin(), arctan()
    - Exponential & logarithmic functions : exp(), log()
    - Square function : sqrt()
    
    ---
"""
)
place_holder1 = st.empty()
place_holder2 = st.empty()

with place_holder1.form(key='my_form'):
	col1, col2= st.columns(2)
	x_min = col1.number_input('x min', value =-10.0, key='x_min')
	x_max = col2.number_input('x max',value =10.0,  key='x_max')
	y_min = col1.number_input('y min',value =-10.0,  key='y_min')
	y_max = col2.number_input('y max', value =10.0, key='y_max')
	
	with st.container():
		col1, col2= st.columns([1, 10])
		col1.subheader("")
		col1.write("f(x,y) = ")
		col2.text_input('Function : enter an expression with x and y :', 'x**2 + y**2 - 2', key='Function')
	submit_button = st.form_submit_button(label='Plot')

x_vec = np.linspace(st.session_state.x_min, st.session_state.x_max, 100)
y_vec = np.linspace(st.session_state.y_min, st.session_state.y_max, 100)
x, y = np.meshgrid(x_vec, y_vec)
try :
	exec("z="+st.session_state['Function'])
except:
    st.write('Function is not valid')
else : 
    ax.plot_surface(x, y, locals()['z'], edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)
    ax.contour(x, y, locals()['z'], zdir='z', offset=np.min(locals()['z']), cmap='coolwarm')
    ax.contour(x, y, locals()['z'], zdir='x', offset=st.session_state.x_min, cmap='coolwarm')
    ax.contour(x, y, locals()['z'], zdir='y', offset=st.session_state.y_max, cmap='coolwarm')
ax.set_box_aspect(aspect=None, zoom=0.8)

with place_holder2.container():
	col1, col2= st.columns([3, 1])
	col2.write('You can change the view angles here : ')
	elev_angle = col2.slider("Elev angle", -180, 180, 30, 10)
	azim_angle = col2.slider("Azim angle", -180, 180, -60, 10)
	roll_angle = col2.slider("Roll angle",-180, 180, 0, 10)
	ax.view_init(elev_angle, azim_angle, roll_angle)
	col1.pyplot(fig)











