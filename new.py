from pymongo import MongoClient
import streamlit as st

client = MongoClient('mongodb+srv://carboncalculator2024:zipzcwaQu1UnYTT5@carbonfootprint.febn7uz.mongodb.net/?retryWrites=true&w=majority&appName=carbonfootprint')

db = client['mydatabase']
collection = db['mydata']

name = st.text_input("Name", value=None)
pas = st.text_input("Password", value=None)
submit = st.button("Submit")

if submit:

    document = {'name':name,'City':pas}
    inserted_document = collection.insert_one(document)
    st.success("Successfully Added")
    client.close()

for people in collection.find():
    st.write(people)