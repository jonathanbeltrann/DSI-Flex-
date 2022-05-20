import streamlit as st
import pickle

st.title("Which Author do you write like?")
st.text("Type in a sentence and find out!")

page = st.sidebar.selectbox('Select a page', ('About', 'Make a Prediction'))

if page == 'About':
    st.write('Here is my model')
    st.write('Thanks for visiting, view the code at github.com/john')

if page == 'Make a Prediction':
    st.write('Edgar Allen Poe and Jane Austin: both authors. Which do YOU write like?')

    with open('models/author_pipe.pkl', 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)

        user_text = st.text_input("Please enter some text: ", value = 'quoth the raven, nevermore')

        predicted_author = pipe.predict([user_text])[0]

        st.write(f'You write like {predicted_author}')

        st.balloons()
