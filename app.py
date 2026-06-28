import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

st.header(r"Sequence: $\quad x_n = \left(1 + \frac{b}{n}\right)^{na}$")
with st.container(border=True,width=650):
    st.subheader(r"$\quad x_n \rightarrow e^{ab} \quad$ i.e. $\quad \lim_{n \to \infty} x_n = e^{ab}$")

st.subheader("Visualization for 100 values of n")
a = st.slider("Enter value of a", min_value=0.0001, max_value=50.0, value=1.0)
b = st.slider("Enter value of b", min_value=0.0001, max_value=50.0, value=1.0)

X = [n for n in range(1,101)]
Y = []
for x in X:
    y = (1 + b/x) **(x*a)
    Y.append(y)

X_r = np.arange(1,101,0.001)
Y_r = []
for x in X_r:
    y = (1 + b/x) **(x*a)
    Y_r.append(y)

fig = plt.figure(figsize=(16,9),dpi=800)
plt.scatter(X,Y,c='red',s=30,label="sequence")
plt.plot(X_r,Y_r,color="green",label="real function")
plt.title(r"$x_n = \left(1 + \frac{b}{n}\right)^{na}$")
plt.axhline(y=np.exp(a*b),color="black",label="y=e")
plt.legend()
st.pyplot(fig,use_container_width=False)

# streamlit run "G:\python manim\sine_n\app.py"