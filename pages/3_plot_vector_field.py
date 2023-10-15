import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin, tan, arccos, arcsin, arctan, exp, sqrt, log


fig = plt.figure(figsize=(10, 10), layout="constrained")
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect('equal')
st.markdown(
    r"""
    # Plot 2D vector field $\vec{V}(x, y) = [u(x,y), v(x,y)]$
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
		st.latex(r'''\vec{V}(x, y) = [u(x,y), v(x,y)]''')
		col1, col2= st.columns([1, 10])
		col1.latex(" u(x,y) = ")
		col2.text_input('Function : enter an expression with x and y :', '-y/sqrt(x**2+y**2)', key='Function_u')
		col1.latex(" v(x,y) = ")
		col2.text_input('Function : enter an expression with x and y :', 'x/sqrt(x**2+y**2)', key='Function_v')
	submit_button = st.form_submit_button(label='Plot')

x_vec = np.linspace(x_min, x_max, 100)
y_vec = np.linspace(y_min, y_max, 100)
x, y = np.meshgrid(x_vec, y_vec)
try :
	exec("u="+st.session_state['Function_u'])
	exec("v="+st.session_state['Function_v'])
	M = np.hypot(locals()['u'], locals()['v'])
except:
    st.write('One of the functions is not valid')


with place_holder2.container():
	quiver_density = st.slider("Quiver density", 1, 30, 10)
	xy_slice = slice(0, 100, 100//quiver_density)
	ax.quiver(x[xy_slice,xy_slice], y[xy_slice,xy_slice], locals()['u'][xy_slice,xy_slice], locals()['v'][xy_slice,xy_slice], angles='xy', scale_units='xy')
	st.pyplot(fig)


