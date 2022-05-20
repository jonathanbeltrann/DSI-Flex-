import streamlit as st
import pickle

st.title('Which author do you write like?')

page = st.sidebar.selectbox(
    'Select a page:',
    ('About', 'Make a prediction')
)
if page == 'About':
    st.write('here is my model')
    st.write('get in touch with me at:')

if page == 'Make a prediction':
    st.write('''Edgar Allen Poe and Jane Austen: both authors. Which one do YOU write like?''')

    with open('models/author_pipe.pkl', mode='rb') as pickle_in:
        pipe = pickle.load(pickle_in)

    user_text = st.text_input('Please input some text:',
        value='quoth the raven...nevermore')

    predicted_author = pipe.predict([user_text])[0]

    st.write(f'You write like: {predicted_author}')