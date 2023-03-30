import streamlit as st
import pyperclip
import os

def main():
    st.markdown(
        f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True
    )
    st.title("Pallet Information")
    st.subheader("Enter the following details:")

    with st.form(key="input_form"):
        pallet_number = st.text_input("Pallet Number:")
        cases_sorted = st.text_input("Number of Cases Sorted:")
        good_cases = st.text_input("Number of Good Cases:")
        bad_cases = st.text_input("Number of Bad Cases:")
        added_to_tag = st.text_input("Tag Number to Add Bad Cases:")
        soiled_hold_tag = st.text_input("Soiled Hold Tag Number:")

        submit_button = st.form_submit_button("Generate Output")

    if submit_button:
        output = f"pallet Number # {pallet_number} - {cases_sorted} cases sorted 100 % - {good_cases} good - {bad_cases} bad added to tag # {added_to_tag} - soiled - hold Tag # {soiled_hold_tag}"
        pyperclip.copy(output)
        st.write("The following text has been copied to your clipboard:")
        st.write(output)

if __name__ == "__main__":
    main()
