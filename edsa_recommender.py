"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
from urllib import response
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import base64
from pathlib import Path

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

st.session_state.model = 'SVD'

# styling
app_style = """
<style>

</style>

"""

st.markdown(app_style, unsafe_allow_html=True)

# Custom CSS to change background color
custom_css = """
<style>
    body {
        background-color: #f0f0f0;  /* Change this to the color you want */
    }
</style>
"""

# Display the custom CSS using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

# convert image to text readable
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='border-radius: 50%; width: 100%'>".format(
      img_to_bytes(img_path)
    )
    return img_html

# set app background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
        <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
        </style>
    """,
    unsafe_allow_html=True
    )



# App declaration
def main():
    page_options = ["Recommender System","Project Overview", "About Us", "Data Analytics", "Model Explanation", "App Feedback"]
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Project Overview":
        st.title("Project Overview")
        st.write("We will examine a thorough introduction and overview of the objectives, features, and the overall approach that will be adopted throughout the development and implementation stages of the WatchWiz app.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
        st.image('resources/imgs/Logo.png')
        st.header('Problem Statement')
        st. write('''In the ever-expanding digital landscape of the entertainment industry, the relevance of recommender systems has become pivotal for ensuring individuals receive tailored content recommendations. Future Forge Software, a visionary company in the entertainment domain, aspires to develop a cutting-edge movie recommender system leveraging advanced analytics and predictive modeling. The challenge at hand involves constructing an algorithm, rooted in content or collaborative filtering, capable of accurately predicting user movie ratings for titles they have not yet viewed, based on their historical preferences.''')
          
        st.header('Solution')
        st.write('''WatchWiz: Your Ultimate Movie Recommender App!''')
        st.write('''The primary objective is to develop a functional recommender system that excels in predicting user preferences for unseen movies. The system should leverage either content-based filtering or collaborative filtering approach to achieve accurate predictions. By analyzing user historical data, including viewing habits, ratings, and interactions, the recommender system should provide valuable insights into individual preferences, ultimately enhancing user satisfaction and engagement.''')

        with st.expander("**Business Value**"):
            st.write('**Enhanced User Engagement and Retention:**')
            st.write('''The app's recommender system, rooted in predictive analytics, is designed to enhance user engagement by providing personalized and relevant content suggestions. This, in turn, contributes to higher user retention rates. For a potential buyer, WatchWiz represents a tool to build and sustain a loyal user base, fostering long-term relationships and maximizing the lifetime value of customers.''')
            st.divider()
            st.write('**Competitive Edge in Content Recommendation:**')
            st.write('''WatchWiz's recommender system, whether based on content or collaborative filtering, provides a competitive edge in the crowded entertainment industry. The buyer gains a sophisticated tool that can outperform competitors in delivering accurate and personalized recommendations. This competitive advantage positions the buyer as an industry leader in content curation and user experience.''')
            st.divider()
            st.write('**Strategic Integration with Existing Platforms:**')
            st.write('''For companies with existing digital platforms, WatchWiz offers seamless integration possibilities. The app's advanced predictive analytics technology can complement and enhance existing services. This strategic integration allows the buyer to fortify their digital ecosystem, providing users with an extended and enriched experience, thereby increasing overall user satisfaction and loyalty.''')
            st.divider()
            st.write('**Brand Enhancement and Positive User Perception:**')
            st.write('''The accuracy of WatchWiz's recommender system contributes to a positive user experience, enhancing the buyer's brand perception. By offering users content that aligns closely with their preferences, the buyer can establish the app as a reliable and user-centric platform. This positive association contributes to brand equity and fosters a favorable perception in the market.''')
            st.divider()
            st.write('**Data-Driven Innovation:**')
            st.write('''As the app collects and analyzes vast amounts of user data over time, it becomes a valuable source of insights into evolving preferences, trends, and behaviors. This data-driven approach allows you to continually enhance and innovate the recommendation algorithm. By staying ahead of user preferences and industry trends, the app becomes a dynamic tool for adapting to changing market demands and maintaining relevance in the long run.''')

        tab1, tab2 = st.tabs(["Content-Based Filtering", "Colaborative-Based Filtering"])

        with tab1:
            st.header("Content-Based Filtering")
            st.write('''WatchWiz employs content-based filtering by analyzing user-generated tags, genres, and preferences along with movie attributes. This approach involves weighting features, calculating scores, and generating personalized recommendations based on comprehensive user and content profiles. The integration of user-generated tags ensures a more nuanced and engaging recommendation process, enhancing the app's ability to provide tailored content suggestions.''')
            st.image('resources/imgs/Content.png',use_column_width=True)
            with st.expander("**Advantages/Disadvantages**"):
                st.write('''**Advantages:**''')
                st.write('''1. Personalization: Content-based filtering excels at providing personalized recommendations based on an individual user's preferences. By analyzing the attributes of items a user has interacted with or liked, the system can recommend similar items that align with the user's unique tastes and interests.''')
                st.write('''2. Transparency: Watchwiz recommendations are based on the characteristics of items, this makes it easier to explain to users why certain items are recommended to them thereby enhancing the transparency and trust of the app.''')
                st.write('''3. Stability:Recommendations on Watchwiz remains stable overtime as they are based on inherent item characteristics rather than changing user behavior or external factors.''')
                st.write('''4. Reduced Dependency on User History: Content-based filtering is less reliant on extensive user history or collaborative data. This makes it particularly useful for new users or in scenarios where limited historical data is available. The system can start making relevant recommendations based on the intrinsic features of items.''')
                st.divider()
                st.write('''**Disadvantages:**''')
                st.write('''1. Limited Diversity in Recommendations: One limitation of content-based filtering is that it tends to recommend items that are similar to those a user has already interacted with. This can result in a lack of diversity in recommendations, potentially leading to a "filter bubble" where users are not exposed to a broad range of content.''')
                st.write('''2. Difficulty in Handling Novelty and Serendipity: Content-based filtering struggles with recommending entirely new or novel items that a user may enjoy. Since the recommendations are based on past interactions and content features, the system may find it challenging to introduce users to content outside their established preferences, limiting the potential for serendipitous discovery.''')

        with tab2:
            st.header("Colaborative-Based Filtering")
            st.write('''WatchWiz utilizes collaborative filtering, incorporating both user-based and item-based approaches. By analyzing user behavior and preferences, the app recommends content based on similarities with other users or items that share characteristics with those the user has enjoyed. This dual collaborative filtering strategy enhances the accuracy and diversity of personalized recommendations, providing users with a dynamic and engaging content discovery experience.''')
            st.image('resources/imgs/Colab.png',use_column_width=True)
            with st.expander("**Advantages/Disadvantages**"):
                st.write('''**Advantages:**''')
                st.write('''1. Personalized Recommendations: Collaborative filtering enables WatchWiz to provide highly personalized recommendations by analyzing user behavior and preferences. Users receive suggestions based on the preferences of others with similar tastes, enhancing the likelihood of content alignment.''')
                st.write('''2. Adaptability to User Behavior Changes: TWatchWiz's collaborative filtering models can adapt to changes in user preferences over time. As users engage with new content or their tastes evolve, the system continually learns from these interactions, ensuring that recommendations stay relevant and up-to-date.''')
                st.divider()
                st.write('''**Disadvantages:**''')
                st.write('''1. Cold Start Problem: One challenge is the "cold start" problem, especially for new users or items. If there is limited historical data available, the system may struggle to provide accurate recommendations until a user has established a sufficient interaction history."''')
                st.write('''2. Lack of Diversity in Recommendations: Collaborative filtering tends to recommend items based on user similarities, potentially leading to a lack of diversity in suggestions. Users may be confined to a specific set of preferences, and there's a risk of missing out on content outside their established tastes.''')        

          

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "About Us":
        st.markdown("<div style='background-color: rgba(246, 246, 246, 1); padding: 20px; margin: 0px 0px 25px 0px; border-radius: 10px; text-align:justify'><p>At Future Forge Software, we stand at the forefront of technological evolution, dedicated to shaping the future of software solutions with a specific focus on the entertainment market. As a trailblazing force in the digital landscape, we specialize in harnessing the power of advanced analytics and predictive modeling within the dynamic realm of entertainment.<br><br> Our commitment revolves around developing cutting-edge software that empowers businesses in the entertainment industry to foresee opportunities, mitigate risks, and achieve unprecedented success. With a keen focus on the unique challenges and opportunities within the entertainment market, we tailor our solutions to meet the ever-evolving needs of this dynamic sector.<br><br>As we aspire to seamlessly integrate predictive analytics into every facet of decision-making in the entertainment industry, our vision is to be the driving force behind a world where foresight transforms content curation, user experiences, and industry standards. Join us on this journey of innovation and discovery as we navigate the digital landscape with a commitment to excellence, innovation, and the transformative potential of predictive analytics. Welcome to Future Forge Software, where the future of entertainment is not just a destination; it's a creation. </div>", unsafe_allow_html=True)
        
        st.markdown("<div style='background-color: transparent; margin: 40px 0 20px 0'><h2 style='text-align:center'>Meet Our Team</h2></div>", unsafe_allow_html=True)
        col_team_1, col_team_2, col_team_3= st.columns(3)
        with col_team_1:
            st.markdown(img_to_html('resources/imgs/Christelle.jpg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Christelle Coetzee</b><br>Team Lead - Data Scientist</p></div>", unsafe_allow_html=True)
        with col_team_2:
            st.markdown(img_to_html('resources/imgs/Amanda.png'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Amanda Sibanda</b><br>Project Manager - Data Analyst</p></div>", unsafe_allow_html=True)
        with col_team_3:
            st.markdown(img_to_html('resources/imgs/Oluwakemi.jpeg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Oluwakemi</b><br>Data Analyst</p></div>", unsafe_allow_html=True)
            
        col_team_4, col_team_5, col_team_6, = st.columns(3)
        with col_team_4:
            st.markdown(img_to_html('resources/imgs/Shedrack.jpeg'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Shedrack Efienokwu</b><br>App Designer</p></div>", unsafe_allow_html=True)
        with col_team_5:
            st.markdown(img_to_html('resources/imgs/Victoria.png'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Victoria Chukwuno Chinenye</b><br>App Programmer</p></div>", unsafe_allow_html=True)
        with col_team_6:
            st.markdown(img_to_html('resources/imgs/Janet.png'), unsafe_allow_html=True)
            st.markdown("<div style='background-color: transparent; margin-top: 10px'><p style='text-align:center'><b>Janet</b><br>App Designer</p></div>", unsafe_allow_html=True)
        

    if page_selection == "Data Analytics":
        st.title("Data Analytics")
        st.write("Delve into the intricacies of our data analytics prowess. In this section, we unravel the power of comprehensive data analysis, extracting valuable insights that drive decision-making and shape the future of WatchWiz.")

        with st.expander("**Top 20 Most Relevant Genome Tags - Toy Story (1995)**"):
            st.image('resources/imgs/Top 20 most relevant genome tags Toy Story.png',use_column_width=True)
            st.write('''Upon scrutinizing the results, it appears that the relevance meter is accurate in its assessment. Tags like 'toys,' 'Pixar animation,' and 'kids and family' are fitting when discussing Toy Story.''')
            
        with st.expander("**Top 20 Most Occurring User Tags for Toy Story**"):
            st.image('resources/imgs/Top 20 Most Occurring User Tags for Toy Story.png',use_column_width=True)
            st.write('''Upon analyzing the results, it becomes evident that the top three tags, namely 'animation,' 'Pixar,' and 'Disney,' provide meaningful insights into the nature of the movie 'Toy Story (1995)'.''')

        with st.expander("**Distribution of Relevance Scores**"):
            st.image('resources/imgs/Distribution of Relevance Scores.png',use_column_width=True)
            st.write('''The distribution of relevance scores exhibits a pronounced rightward skewness, indicating a substantial imbalance between tags that are deemed relevant and those that are not. This observation holds significance for our model as it underscores the prevalence of tags with low relevance scores, suggesting that a considerable portion of user-assigned tags might not strongly contribute to characterizing the movies. Recognizing and understanding this skewness is crucial for refining our model's training and predictive capabilities.

The prominence of a right-skewed distribution implies that a majority of tags may have lower relevance values, potentially posing a challenge in accurately capturing meaningful associations between tags and movies. This understanding prompts us to explore strategies to address the skewed distribution, such as setting appropriate thresholds for relevance scores, focusing on the most relevant tags, or considering alternative weighting schemes during model development.

In the context of recommendation systems, acknowledging the skewness in relevance scores can guide us in designing models that prioritize the most pertinent tags, ensuring that the recommendations are driven by tags that genuinely contribute to characterizing a movie. Additionally, it prompts us to explore ways to handle less relevant tags effectively, either by filtering them out or assigning them reduced influence in the recommendation process.

Ultimately, a nuanced consideration of the relevance score distribution enables us to fine-tune our model, leading to more accurate and personalized movie recommendations by emphasizing tags that hold greater significance in capturing user preferences and characteristics of the movies.''')

        with st.expander("**Genre Distribution in the Dataset**"):
            st.image('resources/imgs/Genre Distribution in the Dataset.png',use_column_width=True)
            st.write('''Upon scrutinizing the genre data, it becomes evident that the predominant genre is drama, closely followed by comedy, with both significantly surpassing others in frequency. Conversely, film-noir and IMAX emerge as the least common movie genres.

Understanding the prevalence of genres in the dataset is crucial for model development. This information can aid in creating a more informed and balanced model, ensuring it is trained on a representative distribution of genres. By acknowledging the popularity or scarcity of certain genres, the model can better capture the diverse landscape of movies and enhance its ability to make accurate predictions or recommendations.''')

        with st.expander("**Average Rating per Genre**"):
            st.image('resources/imgs/Average Rating per Genre.png',use_column_width=True)
            st.write('''It's intriguing to observe that despite being less common, Film-noir and Imax films tend to receive higher ratings, with Film-noir being the highest rated among them. This insight raises the question of whether incorporating the genre information, particularly for less prevalent genres like Film-noir and Imax, could potentially enhance the predictive power and accuracy of our recommendation model. Exploring the impact of genre diversity on ratings may provide valuable insights into user preferences and contribute to the refinement of our recommendation algorithms.''')

        with st.expander("**Release Year Distribution**"):
            st.image('resources/imgs/Release Year Distribution.png',use_column_width=True)
            st.write('''It is evident that a substantial majority of movies in the dataset were released during the period from 2000 to 2020. This observation could be attributed to various factors such as the surge in film production during this timeframe, evolving audience preferences, or increased accessibility to film production resources. Understanding the distribution of movie releases is crucial for our model as it allows us to adapt recommendations based on the temporal dynamics of the dataset.

The significance of this insight may vary between collaborative-based and content-based models. For collaborative-based models, which rely on user behavior patterns and preferences, the temporal distribution of movies could impact the relevance of recommendations based on popular trends over time. On the other hand, content-based models, which focus on the features of movies, might be less influenced by temporal dynamics unless specific temporal features are considered in the model. Adjusting the model based on the observed temporal trends can enhance its accuracy and relevance in providing recommendations tailored to user preferences over different periods.''')

        with st.expander("**Average Rating per Release Year**"):
            st.image('resources/imgs/Average Rating per Release Year.png',use_column_width=True)
            st.write('''The observation that movies released before 1920 tend to have lower average ratings, while those after 1920 exhibit higher ratings with a slight dip around 1980, suggests a potential correlation between film quality and historical context. This finding is essential for a recommender system as it highlights the importance of adapting to evolving filmmaking techniques, shifting audience preferences, data biases, cultural influences, and user demographics. By considering these factors, the recommender system can provide more accurate and personalized movie recommendations that align with users' diverse preferences across different cinematic eras.''')
                
        with st.expander("**Distribution of Ratings in the Dataset**"):
            st.image('resources/imgs/Distribution of Ratings in the Dataset.png',use_column_width=True)
            st.write('''The distribution is skewed to the left, indicating higher overall ratings. The most frequently occurring rating in the dataset is 4, closely followed by a rating of 3. This pattern indicates a trend where users are less inclined to assign extreme values like 0.5 or 1.5, suggesting a general tendency towards moderate ratings. Understanding this distribution is crucial for our model, as it helps to interpret user preferences and discern the typical rating patterns in the dataset.''')

        with st.expander("**Top 25 Most Popular Movies**"):
            st.image('resources/imgs/Top 25 Most Popular Movies.png',use_column_width=True)
            st.write('''It's evident that **"The Shawshank Redemption"** holds the top position as the most popular movie in our dataset, closely followed by **"Forrest Gump."** Upon analyzing the top 25 movies, a notable pattern emerges, revealing that many of them are classic films from the 1990s. Given their high number of ratings and consequent widespread viewership, it would be prudent to consider recommending some of these classics to new users on the platform, especially when little to no data on their preferences is available.''')

        with st.expander("**Top Ten Most Active Users**"):
            st.image('resources/imgs/Top Ten Most Active Users.png',use_column_width=True)
            st.write('''Evidently, user 72315 stands out as the most prolific rater, contributing approximately 8000 more ratings than the next active user. This significant discrepancy in rating activity has notable implications for our model. Considering the substantial dominance of user 72315 in the rating activity, it may be necessary to exclude this user from the equation to ensure a more balanced and representative rating system.''')

        with st.expander("**Actor Frequency in Movie Dataset**"):
            st.image('resources/imgs/Actor Frequency in Movie Dataset.png',use_column_width=True)
            st.write('''We see that _Samuel L. Jackson_ is by far the most appearing actor within our dataset, having starred in 83 movies present within our dataset. Among the most featured actors, we also find that most of them appears between 50 and 60 times within the dataset. Also something worth noting is that among the top 30 most occuring actors within our date, only 2 are female, namely __Julianne Moore__ and __Susan Sarandon__.''')

        with st.expander("**Top 25 Rated Actors**"):
            st.image('resources/imgs/Top 25 Rated Actors.png',use_column_width=True)
            st.write('''Notably, when examining the top 25 rated actors, it's evident that there are not many widely recognized household names. This underscores the extensive diversity of movies within the database. This information is crucial for our model, emphasizing the need to account for a broad spectrum of actors, genres, and lesser-known but highly rated performers in order to provide more comprehensive and inclusive movie recommendations to users with diverse preferences.''')

    if page_selection == "Model Explanation":
        st.title('SVC++')
        st.write('''Singular Value Decomposition (SVD++) is like a magical movie recommendation system. Imagine a giant spreadsheet with everyone's movie preferences. SVD++ breaks this down into three smaller sheets: one for people's tastes, one for movie characteristics, and one for individual preferences. Using this recipe, it predicts what movies someone might like based on similar tastes, movie traits, and personal preferences. It's a clever way of suggesting new movies even before you've seen them, like having a movie wizard tailor recommendations just for you!''')

    if page_selection == "App Feedback":
        st.title("App Feedback")
        st.write("We appreciate your valuable feedback on our app! Your insights and suggestions are crucial in helping us improve and provide you with an exceptional user experience. Please take a few moments to share your thoughts by completing this feedback form. Your input will assist us in understanding what aspects of the app are working well and where we can make enhancements or address any issues you may have encountered.")
        
        with st.form("feedback_form"):
            c_feedback = st.container()

            with c_feedback:
                col_feedback_1, col_feedback_2 = st.columns(2)
                with col_feedback_1:
                    feedback_name = st.text_input(
                        "Name",
                        placeholder='Enter',
                    )
                with col_feedback_2:
                    feedback_email = st.text_input(
                        "Email",
                        placeholder='Enter',
                    )
                col_feedback_3, col_feedback_4 = st.columns(2)
                with col_feedback_3:
                    feedback_type = st.selectbox(
                    'Category',
                    ('Defect', 'Bug', 'Feature'))
                with col_feedback_4:
                    feedback_subject = st.text_input(
                        "Subject",
                        placeholder='Enter',
                    )
                col_feedback_5, col_feedback_6 = st.columns(2)
                with col_feedback_5:
                    feedback_description = st.text_area('Description', '''''', height=400)
                with col_feedback_6:
                    tab_low, tab_medium, tab_high = st.tabs(["Low", "Medium", "High"])
                    with tab_low:
                        feedback_priority = 0
                    with tab_medium:
                        feedback_priority = 1
                    with tab_high:
                        feedback_priority = 2

                    feedback_satisfaction = st.radio(
                    "Satisfaction",
                    ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'))

                    st.write('Additional Features')
                    feedback_additional_1 = st.checkbox('UI/UX')
                    feedback_additional_2 = st.checkbox('Performance')
                    feedback_additional_3 = st.checkbox('Functionality')
                    feedback_additional_4 = st.checkbox('Other')
            submit_feedback = st.form_submit_button("Submit Feedback")

            
            st.title("Echo bot")
            st.write("Need some help?")
            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("what's up?"):
                with st.chat_message("user"):
                    st.markdown(prompt)

                st.session_state.messages.append({"role": "user", "content": prompt})
                response = f"Echo: {prompt}"
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                




print('Done')

if __name__ == '__main__':
    main()
