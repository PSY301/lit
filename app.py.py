import streamlit as st
accounts = {}
name = st.text_input("username", "")
password = st.text_input("password", "")
if st.button("sign up"):
    if name not in accounts:
        accounts = accounts | {name: password}
        st.success('Hi')
    else:
        st.write('try again')
elif st.button('sign in'):
    while True:
        try:
            if accounts[name] == password:
                st.success('Hi')
                break
            else:
                st.success("try again")
        except:
            st.write('try again')
