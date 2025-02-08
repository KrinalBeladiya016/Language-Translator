from google_trans_new import google_translator
import streamlit as st
from googletrans import Translator
from io import StringIO
translator = google_translator()
translator_2 = Translator()
st.title("Language Translator")

dict={'english':'en','marathi':'mr','gujarati':'gu','punjabi':'pa','swedish':'sv','odia':'or','bengali':'bn','hindi':'hi'}

def changed_to():
    p=st.session_state.To
    # ft = "Translate To.txt"
    # with open(ft, "a", encoding="utf-8") as f:
    #      f.write(p)
    #      f.write("\n")

# @st.cache_data
# def saveData():
#     fo = "history.txt"
#     with open(fo, "a", encoding="utf-8") as f:
#         f.write('{} | {} | {}'.format(Text, to,translate))
#         f.write("\n")


to = st.selectbox(
     'Translate to:',
     ('english','marathi','gujarati','punjabi','swedish','odia','bengali','hindi'),key="To",on_change=changed_to)

for i in dict:
     if(i==to):
          str = dict[i]

Text = st.text_input("Enter a text")
# translate = translator.translate(Text, lang_tgt=str)
# st.write("Result of google_trans_new API ",translate)

translate_2=translator_2.translate(Text,dest=str)
st.write("Result of googletrans API ",translate_2.text)
# saveData()

# @st.cache_data
# def translate_file():
#     st.write(len(uploaded_file.getvalue()))
    
#     else: 
#         st.write('not uploaded')            



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(len(uploaded_file.getvalue()))
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    for string in stringio:
        st.write(string)
        # translate = translator.translate(string, lang_tgt=str)
        translate_2 = translator_2.translate(string, dest=str)
        string=string.strip()
        # st.write(translate)
        with open("translated_file.txt","w",encoding="utf-8") as f:
            f.write('{} | {}'.format(string, translate_2.text))
            f.write("\n")
            
else:
    st.write(uploaded_file)    

if uploaded_file is not None:
    st.write("GOOGLE_TRANS_NEW | original | GOOGLETRANS")
    with open("translated_file.txt", "r", encoding='utf-8') as file1:
        for x in file1:
            st.write(x)
    file11=open('translated_file.txt','r', encoding='utf-8')
    
    st.download_button('Download CSV', file11,file_name='Translated_file.txt')

    file1.close()        
