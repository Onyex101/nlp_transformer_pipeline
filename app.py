import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Select an Option",
    [
        "Classify Text",
        "Question Answering",
        "Text Generator",
        "Named Entity Recognition",
        "Text Summarization",
        "Translation"
    ]
)

if option == "Classify Text":
    text = st.text_area(label="Enter text")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == "Question Answering":
    q_a = pipeline("question-answering")
    context = st.text_area(label="Enter Context")
    question = st.text_area(label="Enter Question")
    if context and question:
        answer = q_a({"question":question,"context":context})
        st.write(answer)
elif option == "Text Generator":
    text = st.text_area(label="Enter text")
    if text:
        text_gen = pipeline("text-generation")
        answer = text_gen(text,max_new_tokens=200)
        st.write(answer)
elif option == "Named Entity Recognition":
    text = st.text_area("Enter Text")
    if text:
        ner = pipeline("ner")
        answer = ner(text)
        st.write(answer)
elif option == "Text Summarization":
    summarizer = pipeline("summarization")
    text = st.text_area("Paste Article")
    if text:
        summary = summarizer(text, max_length=400,min_length=30)
        st.write(summary)
elif option == "Translation":
    translator = pipeline("translation_en_to_fr")
    text = st.text_area("Enter Text")
    if text:
        translation = translator(text)
        st.write(translation)