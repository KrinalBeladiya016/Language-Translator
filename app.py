from googletrans import Translator
from languages import *
import streamlit as st
from io import StringIO
from gtts import gTTS 

st.set_page_config(page_title='Simply! Translate', page_icon='translator-icon.png', initial_sidebar_state='expanded')


translator_2 = Translator()

st.title('Language Translator')

source_text=st.text_input('Enter text to translate',help="input text")
target_languages=st.selectbox('Select your target language',options=languages, index=29)
translate=st.button('Translate')
     

if translate or source_text:
    translator=Translator()
    out=translator.translate(source_text,dest=target_languages)
    st.write("Translated Text : ")
    st.write(out.text)

    myobj = gTTS(text=out.text, lang='en', slow=False) 
    
    myobj.save("welcome.mp3") 
    audio_file = open('welcome.mp3','rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio')

def changed_to():
    p=st.session_state.To

str_help='Upload Only .txt file'

uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False,help=str_help)
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    for string in stringio:
        # translate = translator.translate(string, lang_tgt=str)
        translate_2 = translator_2.translate(string, dest=target_languages)
        string=string.strip()
        # st.write(translate)
        with open("translated_file.txt","w",encoding="utf-8") as f:
            f.writelines(string)
            # f.write('{} | {}'.format(string, translate_2.text))
            f.write("\n")
  

if uploaded_file is not None:
    # st.write("GOOGLE_TRANS_NEW | original | GOOGLETRANS")
    # with open("translated_file.txt", "r", encoding='utf-8') as file1:
    #     for x in file1:
    #         st.write(x)
    file12=open('translated_file.txt','r',encoding='utf-8')
    
    st.write("Translated File : ")
    # st.write(file12)
    for x in file12:
        st.write(x)
    file12.close()

    file11=open('translated_file.txt','r', encoding='utf-8')
    
    st.download_button(' Download ', file11,file_name='Translated_file.txt')

    file11.close()        
