import streamlit as st
import pandas as pd


from links import *

add_selectbox = st.sidebar.selectbox(
    "Sergei Budygin 231-1 PyProject",
    ("Comments", "Grade", "It's actually fake")
)

with st.sidebar:
    add_radio = st.radio(
        "Do you like my project?",
        ("It's awesome", "It's nonsense")
    )
# intro
st.text(open(intro).read())
# DataCleanup
data_old = pd.read_csv(data_old)
st.text(open(DataCleanup).read())
button_clicked = st.button("Before:")
if button_clicked:
    st.write(data_old.head(15))
data = pd.read_csv(data)
if st.button("After:"):
    st.write(data.head(25))
# overview

st.text(open(gr1_overview).read())
st.image(paintings[1], use_column_width=True)
st.image(paintings[2], use_column_width=True)
st.text(open(gr4).read())


import matplotlib as plt
data = pd.read_csv('new1.csv')
fig, ax = plt.pyplot.subplots()
ax = data.loc[data.brand == 'Suzuki', 'year'].plot(kind='hist', alpha=0.4, label='Suzuki')
data.loc[data.brand == 'Kia', 'year'].plot(kind='hist', alpha=0.2, ax=ax, label='Kia')
data.loc[data.brand == 'Skoda', 'year'].plot(kind='hist', alpha=0.4, ax=ax, label='Skoda')
ax.yaxis.set_label_text('Quantity')
ax.set_title('The quantity of Suzuki, Skoda, and Kia on the market.')
plt.pyplot.legend()
st.pyplot(fig)


st.text(open(gr56).read())
st.image(paintings[5], use_column_width=True)
st.image(paintings[6], use_column_width=True)
st.text(open(gr7).read())
st.image(paintings[7], use_column_width=True)
st.text(open(gr8).read())
st.image(paintings[8], use_column_width=True)
st.text(open(gr9).read())
st.image(paintings[9], use_column_width=True)
st.text(open(gr10).read())
st.image(paintings[10], use_column_width=True)
st.button("Click if you're tired")
