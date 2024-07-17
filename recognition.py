import speech_recognition as sr
from PIL import Image
import string
import streamlit as st
import os
import time

# Function to handle text detection
def text_detection():
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
               'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy']
    
    arr = list(string.ascii_lowercase)

    text_input = st.text_input("Enter the text command:")
    if text_input:
        a = text_input.lower()
        st.write("You entered: " + a)

        for c in string.punctuation:
            a = a.replace(c, "")
        
        if a in ['goodbye', 'good bye', 'bye']:
            st.write("Oops! Time to say goodbye")
            return
        
        if a in isl_gif:
            gif_path = f'/home/tejaswini/Downloads/ISL_Gifs/{a}.gif'
            if os.path.exists(gif_path):
                st.image(gif_path)
            else:
                st.write("GIF not found!")
        else:
            image_list = []
            for char in a:
                if char in arr:
                    img_path = f'/home/tejaswini/Downloads/letters/{char}.jpg'
                    if os.path.exists(img_path):
                        image_list.append(img_path)
                    else:
                        st.write(f"Image for '{char}' not found!")
                else:
                    continue
            
            if image_list:
                if 'index' not in st.session_state:
                    st.session_state.index = 0

                if st.session_state.index < len(image_list):
                    img_path = image_list[st.session_state.index]
                    st.image(img_path)
                    st.session_state.index += 1
                    time.sleep(1)  # Delay for 1 second before showing the next image
                    st.experimental_rerun()
                else:
                    st.session_state.index = 0  # Reset the index for the next input

# Function to handle voice detection
def voice_detection():
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
               'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy']

    arr = list(string.ascii_lowercase)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Listening... Please speak.")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            st.write("You said: " + command)

            for c in string.punctuation:
                command = command.replace(c, "")
            
            if command in ['goodbye', 'good bye', 'bye']:
                st.write("Oops! Time to say goodbye")
                return
            
            if command in isl_gif:
                gif_path = f'/home/tejaswini/Downloads/ISL_Gifs/{command}.gif'
                if os.path.exists(gif_path):
                    st.image(gif_path)
                else:
                    st.write("GIF not found!")
            else:
                image_list = []
                for char in command:
                    if char in arr:
                        img_path = f'/home/tejaswini/Downloads/letters/{char}.jpg'
                        if os.path.exists(img_path):
                            image_list.append(img_path)
                        else:
                            st.write(f"Image for '{char}' not found!")
                    else:
                        continue
                
                if image_list:
                    if 'index' not in st.session_state:
                        st.session_state.index = 0

                    if st.session_state.index < len(image_list):
                        img_path = image_list[st.session_state.index]
                        st.image(img_path)
                        st.session_state.index += 1
                        time.sleep(1)  # Delay for 1 second before showing the next image
                        st.experimental_rerun()
                    else:
                        st.session_state.index = 0  # Reset the index for the next input
        except sr.UnknownValueError:
            st.write("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            st.write("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main Streamlit App
st.title("Indian Sign Language(ISL)")

# Sidebar with options
option = st.sidebar.selectbox(
    "Choose an option",
    ("Home", "Text Detection", "Voice Detection", "About")
)

if option == "Home":
    st.write("The Indian Sign Language(ISL) is an application designed to facilitate communication for the deaf community. It translates live speech or audio recordings into text and displays corresponding Indian Sign Language images or GIFs.")
    st.image("/home/tejaswini/Downloads/sign.jpeg", use_column_width=True)
elif option == "Text Detection":
    text_detection()
elif option == "Voice Detection":
    voice_detection()
elif option == "About":
    st.write("This application is designed to assist individuals with hearing impairments by translating text and voice commands into sign language. Developed using Python and Streamlit.")
    st.write("This aims to bridge communication gaps between hearing and deaf individuals by utilizing natural language processing and machine learning algorithms.")
    st.title("Working Process:")
    st.write("	1.Language Translation: Converts spoken or recorded audio into text using speech recognition.")
    st.write("	2.Text Processing: Uses natural language processing (NLP) to process the text and determine the relevant Indian Sign Language (ISL) translations.")
    st.write("	3.Sign Display: Shows corresponding ISL images or GIFs for the translated text.")
    st.write("	4.Accessibility: Aims to assist in communication for deaf and hard-of-hearing individuals.")
    st.write("	5.Machine Learning: Incorporates machine learning algorithms for improved translation accuracy.")
