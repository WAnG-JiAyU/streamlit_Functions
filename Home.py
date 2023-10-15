import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome👋")

st.write("""
This is a little application to draw simple functions and simple vector field.
""")


st.sidebar.success("Select a demo above.")
# X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
# U = np.cos(X)
# V = np.sin(Y)
# fig1, ax1 = plt.subplots()
# ax1.set_title('Arrows scale with plot width, not view')
# Q = ax1.quiver(X, Y, U, V, units='width')
# qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',coordinates='figure')
# fig_html = mpld3.fig_to_html(fig1)
# components.html(fig_html, height=600)


