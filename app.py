import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":smile:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_49rdyysj.json")
img_contact_form = Image.open("Images/Loan.png")
img_lottie_animation = Image.open("Images/LOS.png")
img_cnn = Image.open("Images/rock.jpg")
img_nlp = Image.open("Images/zomato.png")
img_web = Image.open("Images/web.png")
img_car = Image.open("Images/car.png")
img_topic = Image.open("Images/topic.png")
img_mech = Image.open('Images/mech.jpg')
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Subradip Poddar :smile:")
    st.title("An aspiring Data Science Professional From India")
    st.write(
        "I am passionate about finding ways to use data to be more efficient and effective in business settings."
    )
    st.write("[LinkendIn >](https://www.linkedin.com/in/subradip-poddar/)")
    #insta_icon = "https://commons.wikimedia.org/wiki/File:Linkedin-png-linkedin-icon-1600.png"
    #insta_link = "https://www.linkedin.com/in/subradip-poddar/"
    # st.markdown(
    # f"""<a href={insta_link}><img src={insta_icon} alt="drawing" width="100"/></a>""", unsafe_allow_html=True)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("A Brief about myself")
        st.write("##")
        st.write(
            """
            - I'm currently pursuing my post graduation in data science and machine learning from Manipal Academy Of Higher Education 
              and have a keen interest in EDA,Data Vizualisation,Statistical analysis and Machine learning algorithms, 
              topics on which I'm currently working on to bring professional competency. 
            
            - I also have knowledge on Natural Language Processing, Deep Learning Algorithms and Image Classification using CNN 
              architecture and Image augmentation techniques.
            
            - I hold a Bachelor's degree in Mechanical Engineering from Visvesvaraya Technological University with a first class with distinction.
            
            - My goal is to turn data into information, information into insights and drive the business' forward 
              by identifying key business problems and providing robust solutions.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader(
            "HOSPITALIZATION DURATION PREDICTION USING MACHINE LEARNING")
        st.write(
            """
            - Covid-19 (recent) The pandemic has called attention to one 
              of the most neglected areas of concern: healthcare management. While data science 
              may be used in a variety of ways in healthcare management, patient length of stay(LOS)
              is one crucial statistic to monitor and anticipate if one wishes to increase the 
              efficiency of a hospital's healthcare management.
            - Prior understanding of LOS can also help with practicalities such as planning space and bed allotment.
              The goal is to properly anticipate the length of stay for each patient 
              on a case-by-case basis so that hospitals may allocate resources more efficiently and effectively.
            """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Predicting_hospital_stay_in_days.git)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Loan Default Prediction using Machine Learning")
        st.write(
            """
             ● I assessed the data  available and performed some exploratory and descriptive analytics to identify interesting and useful patterns, trends, and insights
             Predictive Analysis
             
             ● Built appropriate predictive model/s on the data.
             
             ● Compared various predictive models with appropriate regularization and/or hyper-parameter tuning. 
             
             ● Evaluated the performance of the model. 
             
             ● Identified the right metric to evaluate the performance of the model. 
             
             ● Identified issues and concerns on the given data and suggest the best technique/s to overcome the issues.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Loan-Default-Prediction.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cnn)
    with text_column:
        st.subheader("Classification-of-Scissors-Rock-Paper-Images using CNN")
        st.write(
            """
             ● I had Dataset with Lots of pictures of rock,paper and scissor images I used ImageDataGenerator to segment
               them into training,test and validation sets.
             
             ● I first designed a CNN without any image augmentation techniques used in ImageDataGenerator and used evaluation
               techniques to judge it's performance.  
             
             ● I then used image augmentation techniques and then again used CNN to classify the images hwich showed a 
               marked improvement in accuracy.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Classification-of-Scissors-Rock-Paper-Images.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_nlp)
    with text_column:
        st.subheader(
            "Predict Rating from the Resturant Reviews using NLP and ML algorithms")
        st.write(
            """
             ● Users on the platform can also post reviews of restaurants and provide a rating accompanying the review. 
               The content in the reviews should ideally reflect the rating provided by the customer.
               
             ● In many cases, there is a mismatch, owing to multiple reasons, where the rating does not match the customer review. 
               The reviews and rating match is very important as it builds customer trust 
               on the platform and helps the user get an accurate picture of the restaurant.
             
             ● I needed to enable the identification and cleanup of such cases to ensure the ratings reflect the reviews 
               and that the reviews seem trustworthy to the customer also used NLP techniques in conjunction 
               with machine learning models to predict the rating from the review text.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Help-Zomato-Predict-Rating-from-the-Review.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_web)
    with text_column:
        st.subheader("Various Webscrapping Projects")
        st.write(
            """
             ● Used Beautiful soup and selenium to extract relevant data from static,dynamic websites.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/FlipkartDataScrape.git)")
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/SharkTankInvestor.git)")
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Interview-Quotes.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_car)
    with text_column:
        st.subheader("Car Price and Selling Prediction")
        st.write(
            """
             ● To predict the selling price of second-hand models using Linear Regression Models 
               and also using the same dataset to use to predict whether the model will be 
               sold or not using logistic regression. 

             ● The Model performance is improved using lasso and ridge regression techniques.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Linear-Regression-for-Car-Price-Prediction.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_topic)
    with text_column:
        st.subheader("Topic Analysis of Review Data")
        st.write(
            """
             ● I had data of a leading mobile brand anf tried to understand the voice of the customer by analyzing the
             reviews of their product on Amazon and the topics that customers are talking about. I
             performed topic modeling on specific parts of speech and finally interpreted the emerging topics

             ● Steps:
             
             - Discover the topics in the reviews and present it to business in a consumable format. 
             
            - Employ techniques in syntactic processing and topic modelling.
             
            - Perform specific cleanup, POS tagging, and restricting to relevant POS tags, then, perform topic
             modeling using LDA. 
             
            - Finally, give business-friendly names to the topics and make a table for business.
             """
        )
        st.markdown(
            "[GitHub Link](https://github.com/subradip-poddar/Topic-Modelling.git)")

with st.container():
    st.write("---")
    st.header("Under Graduate Project-Mechanical")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_mech)
    with text_column:
        st.subheader(
            "Electromagnetic and Thermal Analysis of 3-phase induction motor used in an electric vehicle")
        st.write(
            """
             ● This project deals with the study of electromagnetic and thermal analysis of squirrel cage 3-
             phase induction motor used in an electric vehicle, the above said analysis is done by
             changing the material of the rotor winding of the motor with different materials like
             Aluminum, Copper, Nickel, Cobalt and Iron. 
             
             ● Using FEM, the input and output torque,Electrical and mechanical powers and 
             computed using electromagnetic analysis whereas heat flux and temperature distribution is computed from thermal analysis.
             
             ● The results so obtained are used to carry out a comparative study of effectiveness of
             various materials in the rotor winding's and in providing suitable electromagnetic and
             thermal characteristics for each material.
             """
        )
        st.markdown(
            "[Link](https://drive.google.com/file/d/1wvMhkX9uRi6E3qk8CwSGHU9DXXovTyLj/view)")


# Get in touch

with st.container():
    st.write("---")
    st.header("Let's catch up!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/1839e5ad11d1414ad1a34d394361b191" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
