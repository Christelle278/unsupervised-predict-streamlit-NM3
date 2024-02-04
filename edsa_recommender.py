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
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():
    
    st.sidebar.image("resources/imgs/logo.jpg")
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home page","Recommender System","Solution Overview", "Analysis","Company Overview", "Feedback", 'Feedbacks']

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)

# Rest of your Streamlit code
        
    if page_selection == "Company Overview":
        #Header contents
        st.write('# About Future Forge')
        st.image('resources/imgs/logor.jpg', width=70)
        st.markdown(''' Welcome to Future Forge, where innovation meets foresight. 
We are a cutting-edge software company dedicated to crafting prediction 
software that empowers businesses to navigate the future with confidence. 
In an era where data is king, our team of seasoned developers and data 
scientists is committed to creating advanced solutions that transcend 
conventional expectations.
''')
        st.write('# Our Vision')
        st.markdown(''' Aspire to be the driving force behind a world where predictive 
analytics seamlessly integrates into every facet of decision-making. We envision our 
software empowering organizations globally, propelling them towards sustained growth, 
and transforming industries through the foresight of accurate predictions.
''')
        st.write('# Our Mission')
        st.markdown(''' To harness the power of advanced analytics and predictive modeling, 
we are committed to developing cutting-edge software solutions that enable businesses 
to foresee opportunities, mitigate risks, and achieve unprecedented success in an 
ever-evolving digital landscape
''')
        st.write('# Why Future Forge')
        st.markdown(''' **Innovation:** We thrive on pushing the boundaries of what's possible, 
constantly exploring new frontiers in predictive technology.

**Reliability:** Our software solutions are built on robust frameworks,
ensuring reliability and accuracy in every prediction.

**Customization:** Recognizing the unique needs of each business, 
we tailor our solutions to fit seamlessly into your workflow, providing personalized 
insights.

**Collaboration:** We believe in working hand-in-hand with our clients, 
fostering a collaborative approach that ensures our solutions align perfectly with 
your objectives ''')
        st.write('# Meet the team')
        st.write("## Application Programmer")

# Write-up in the left column
        st.write('### Chukwuno Victoria')
        col1, col2 = st.columns([2, 1])
        col2.markdown(''' Chukwuno Victoria, our talented Application Programmer, embodies the spirit of innovation and determination. Hailing from a background enriched with a degree in computer science, Chukwuno is a visionary who navigates the intricate world of coding with finesse.

Her journey into the realm of software development began with a passion for solving complex problems. Chukwuno's insatiable curiosity led her to explore various programming languages and frameworks, honing her skills and deepening her understanding of the ever-evolving tech landscape.

Chukwuno's commitment to excellence is not only reflected in her coding prowess but also in her ability to seamlessly translate ideas into efficient and user-friendly applications. With a keen eye for detail, she ensures that each line of code contributes to the overall success of our software solutions.

Beyond her technical acumen, Chukwuno brings a collaborative and innovative spirit to the Future Forge team. She thrives on challenges, constantly seeking new opportunities to push the boundaries of what's possible in the digital realm. As an integral part of our company, Chukwuno plays a pivotal role in shaping the future of predictive technology.
''')
        col1.image('resources/imgs/p.jpeg', use_column_width=True)
        
        st.write("## Application Designer")
        st.write('### Efienokwu Shedrack')
        col1, col2 = st.columns([2, 1])
        col2.markdown('''Our App Designer, is a creative force behind Future Forge. Armed with a keen eye for design aesthetics and a passion for user-centric experiences, Shedrack elevates our software solutions to new heights. With a background in graphic design and a commitment to staying on the cutting edge of design trends, he brings a fresh and innovative approach to every project. Shedrack's dedication to creating visually compelling and intuitive interfaces plays a key role in shaping the Future Forge user experience. His ability to seamlessly blend form and function ensures that our applications not only meet but exceed user expectations. In the realm of software design, Shedrack Efienokwu is a driving force, contributing to Future Forge's mission of transforming industries through predictive technology.''')
        col1.image('resources/imgs/O.jpeg', use_column_width=True)
        
        st.write("## Data Analyst")
        st.write('### Oluwakemi')
        col1, col2 = st.columns([2, 1])
        col2.markdown('''Oluwakemi specializes in Exploratory Data Analysis (EDA), employing advanced statistical techniques to uncover hidden patterns, identify anomalies, and validate hypotheses. With a meticulous eye for detail, she ensures that our predictive models are built on a foundation of robust and accurate data. Oluwakemi's passion for data, coupled with her analytical prowess, makes her an invaluable asset to the Future Forge team. Join us in leveraging Oluwakemi's expertise to unlock the full potential of your data and drive informed decisions for a future of success.''')
        col1.image('resources/imgs/Z.jpeg', use_column_width=True)
        
        st.write("## Data Science")
        st.write('### Christelle Coetzee')
        col1, col2 = st.columns([2, 1])
        col2.markdown('''As a seasoned Data Scientist, Christelle combines technical expertise with creative problem-solving, crafting innovative solutions that propel our predictive capabilities to new heights. Actively engaging with cross-disciplinary teams to integrate Data Science seamlessly into our software solutions. Beyond algorithms and models, Christelle is dedicated to delivering strategic decision support. By translating complex data into actionable intelligence, she empowers businesses to make informed choices and navigate the future with confidence. Her ability to bridge the gap between technical intricacies and practical application enhances the overall impact of our predictive technologies. Christelle Coetzee, with her passion for innovation and unwavering commitment to excellence, exemplifies the spirit of Future Forge's Data Science division. ''')
        col1.image('resources/imgs/z.jpeg', use_column_width=True)

        st.write("## Project Manager")
        st.write('### Amanda Sibanda')
        col1, col2 = st.columns([2, 1])
        col2.markdown('''Meet Amanda Sibanda, the orchestrator of project excellence at Future Forge. As our dedicated Project Manager, Amanda plays a pivotal role in ensuring that every project unfolds seamlessly, meeting and exceeding client expectations. In the dynamic landscape of software development, Amanda excels at adapting to change. Her agile mindset allows her to navigate shifting priorities, evolving client needs, and emerging technologies, ensuring that projects remain resilient in the face of challenges. With a keen understanding of client needs, Amanda ensures that projects align with business goals. Her client-centric approach involves active communication, transparency, and a commitment to delivering solutions that resonate with the unique requirements of each project.
Amanda Sibanda personifies Future Forge's commitment to project management excellence. Join us on a journey where projects unfold seamlessly, guided by Amanda's expertise and a passion for delivering exceptional results.''')
        col1.image('resources/imgs/c.jpeg', use_column_width=True)
    
    if page_selection == "Home page":
        st.write('# We are the Future')
        st.image('resources/imgs/logor.jpg', use_column_width=True)
        import json

        def load_knowledge_base(file_path):
            with open(file_path, 'r') as file:
                knowledge_base = json.load(file)
            return knowledge_base

        def save_knowledge_base(file_path, knowledge_base):
            with open(file_path, 'w') as file:
                json.dump(knowledge_base, file, indent=2)

        def chat_bot(user_input, knowledge_base):
            for entry in knowledge_base["questions"]:
                if user_input.lower() in entry["question"].lower():
                    return entry["answer"]
            return "I don't know the answer. Can you teach me?"

        if __name__ == "__main__":
            json_file_path = "knowledge_base.json"
            knowledge_base = load_knowledge_base(json_file_path)

            while True:
                user_input = input("You: ")
                if user_input.lower() == "exit":
                    break

                response = chat_bot(user_input, knowledge_base)
                print("Bot:", response)

                if response == "I don't know the answer. Can you teach me?":
                    new_answer = input("You: ")
                    new_question = input("Enter a question for the answer: ")
                    knowledge_base["questions"].append({"question": new_question, "answer": new_answer})
                    save_knowledge_base(json_file_path, knowledge_base)
                    print("Thank you for teaching me!")


        
    if page_selection == "Analysis":
        st.markdown("# Exploratory Data Analysis")
        st.markdown('''Exploratory Data Analysis (EDA) is a fundamental and systematic 
process that entails conducting initial investigations on data. The primary objectives 
are to uncover discernible patterns, detect anomalies, rigorously test hypotheses, and 
validate assumptions through the utilization of summary statistics and graphical representations. 
This analytical approach plays a crucial role in the comprehensive understanding and interpretation 
of datasets, providing a solid foundation for subsequent data-driven decision-making..''')
            
        eda_select = st.selectbox('Choose a visualization to examine ',('Relivance Score','Genres Rating','Release Year', 'Ratings', 'User Activity', 'Top Actors', 'Popular Movies', 'Genres Distribution', 'Movie/Time', 'Toy Story User Tag', 'Toy Story Genome Tag'))
        if eda_select == "Relivance Score":
            st.image('resources/imgs/B.JPG',use_column_width=True)
            st.write('''The distribution of relevance scores exhibits a pronounced rightward skewness, indicating a substantial imbalance between tags that are deemed relevant and those that are not. This observation holds significance for our model as it underscores the prevalence of tags with low relevance scores, suggesting that a considerable portion of user-assigned tags might not strongly contribute to characterizing the movies. Recognizing and understanding this skewness is crucial for refining our model's training and predictive capabilities.

The prominence of a right-skewed distribution implies that a majority of tags may have lower relevance values, potentially posing a challenge in accurately capturing meaningful associations between tags and movies. This understanding prompts us to explore strategies to address the skewed distribution, such as setting appropriate thresholds for relevance scores, focusing on the most relevant tags, or considering alternative weighting schemes during model development.

In the context of recommendation systems, acknowledging the skewness in relevance scores can guide us in designing models that prioritize the most pertinent tags, ensuring that the recommendations are driven by tags that genuinely contribute to characterizing a movie. Additionally, it prompts us to explore ways to handle less relevant tags effectively, either by filtering them out or assigning them reduced influence in the recommendation process.

Ultimately, a nuanced consideration of the relevance score distribution enables us to fine-tune our model, leading to more accurate and personalized movie recommendations by emphasizing tags that hold greater significance in capturing user preferences and characteristics of the movies.''')
        if eda_select == "Genres Rating":
            st.image('resources/imgs/G.JPG',use_column_width=True)
            st.write('''It's intriguing to observe that despite being less common, Film-noir and Imax films tend to receive higher ratings, with Film-noir being the highest rated among them. This insight raises the question of whether incorporating the genre information, particularly for less prevalent genres like Film-noir and Imax, could potentially enhance the predictive power and accuracy of our recommendation model. Exploring the impact of genre diversity on ratings may provide valuable insights into user preferences and contribute to the refinement of our recommendation algorithms.''')
        if eda_select == "Release Year":
            st.image('resources/imgs/I.JPG',use_column_width=True)
            st.write('''The observation that movies released before 1920 tend to have lower average ratings, while those after 1920 exhibit higher ratings with a slight dip around 1980, suggests a potential correlation between film quality and historical context. This finding is essential for a recommender system as it highlights the importance of adapting to evolving filmmaking techniques, shifting audience preferences, data biases, cultural influences, and user demographics. By considering these factors, the recommender system can provide more accurate and personalized movie recommendations that align with users' diverse preferences across different cinematic eras.''')
        if eda_select == "Ratings":
            st.image('resources/imgs/H.JPG',use_column_width=True)
            st.write('''It is evident that a substantial majority of movies in the dataset were released during the period from 2000 to 2020. This observation could be attributed to various factors such as the surge in film production during this timeframe, evolving audience preferences, or increased accessibility to film production resources. Understanding the distribution of movie releases is crucial for our model as it allows us to adapt recommendations based on the temporal dynamics of the dataset.

The significance of this insight may vary between collaborative-based and content-based models. For collaborative-based models, which rely on user behavior patterns and preferences, the temporal distribution of movies could impact the relevance of recommendations based on popular trends over time. On the other hand, content-based models, which focus on the features of movies, might be less influenced by temporal dynamics unless specific temporal features are considered in the model. Adjusting the model based on the observed temporal trends can enhance its accuracy and relevance in providing recommendations tailored to user preferences over different periods.''')
        if eda_select == "User Activity":
            st.image('resources/imgs/F.JPG',use_column_width=True)
            st.write('')
        if eda_select == "Top Actors":
            st.image('resources/imgs/G.JPG',use_column_width=True)
            st.write('')
        if eda_select == "Popular Movies":
            st.image('resources/imgs/E.JPG',use_column_width=True)
            st.write('')
        if eda_select == "Genres Distribution":
            st.image('resources/imgs/V.jpg',use_column_width=True)
            st.write('''Upon scrutinizing the genre data, it becomes evident that the predominant genre is drama, closely followed by comedy, with both significantly surpassing others in frequency. Conversely, film-noir and IMAX emerge as the least common movie genres.

Understanding the prevalence of genres in the dataset is crucial for model development. This information can aid in creating a more informed and balanced model, ensuring it is trained on a representative distribution of genres. By acknowledging the popularity or scarcity of certain genres, the model can better capture the diverse landscape of movies and enhance its ability to make accurate predictions or recommendations.''')
        if eda_select == "Movie/Time":
            st.image('resources/imgs/J.JPG',use_column_width=True)
            st.write('')
        if eda_select == 'Toy Story User Tag':
            st.image('resources/imgs/T.jpeg',use_column_width=True)
            st.write('''Upon analyzing the results, it becomes evident that the top three tags, namely 'animation,' 'Pixar,' and 'Disney,' provide meaningful insights into the nature of the movie 'Toy Story (1995).

In conclusion, it can be inferred that the frequency of a user_tag correlates with its relevance to the movie. Tags appearing more frequently tend to offer more meaningful and representative information about the movie, while less commonly used tags may not contribute significantly to the movie's characterization.''')
        if eda_select == "Toy Story Genome Tag":
            st.image('resources/imgs/k.jpeg',use_column_width=True)
            st.write('''Some of the least mentioned user_tags such as 'DVD-Video,' 'story,' and 'good time' contribute less to our understanding of the movie.
To sum up, it can be deduced that the occurrence of a user tag is linked to its significance to the movie. Tags with higher frequencies generally provide more meaningful and indicative information about the film, whereas tags used less frequently may have a lesser impact on the movie's portrayal.
''')
    
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
    if page_selection == "Solution Overview":
        st.title("Problem Statement")
        st.markdown("In the ever-expanding digital landscape of the entertainment industry, the relevance of recommender systems has become pivotal for ensuring individuals receive tailored content recommendations. Future Forge Software, a visionary company in the entertainment domain, aspires to develop a cutting-edge movie recommender system leveraging advanced analytics and predictive modeling. The challenge at hand involves constructing an algorithm, rooted in content or collaborative filtering, capable of accurately predicting user movie ratings for titles they have not yet viewed, based on their historical preferences.")

        st.title(" Solution ")
        st.write("### WatchWiz: Your Ultimate Movie Recommender App!")
        col1, col2 = st.columns([2, 1])
        col2.markdown(" The primary objective is to develop a functional recommender system that excels in predicting user preferences for unseen movies. The system should leverage either content-based filtering or collaborative filtering approach to achieve accurate predictions. By analyzing user historical data, including viewing habits, ratings, and interactions, the recommender system should provide valuable insights into individual preferences, ultimately enhancing user satisfaction and engagement.")
        col1.image('resources/imgs/S.jpeg', use_column_width=True)
        
        st.title("Business Value")
        st.write(" ### Enhanced User Engagement and Retention:")
        st.markdown(" The app's recommender system, rooted in predictive analytics, is designed to enhance user engagement by providing personalized and relevant content suggestions. This, in turn, contributes to higher user retention rates. For a potential buyer, WatchWiz represents a tool to build and sustain a loyal user base, fostering long-term relationships and maximizing the lifetime value of customers.")

        st.write(" ### Competitive Edge in Content Recommendation:")
        st.markdown(" WatchWiz's recommender system, whether based on content or collaborative filtering, provides a competitive edge in the crowded entertainment industry. The buyer gains a sophisticated tool that can outperform competitors in delivering accurate and personalized recommendations. This competitive advantage positions the buyer as an industry leader in content curation and user experience.")
        
        st.write(" ### Strategic Integration with Existing Platforms:")    
        st.markdown(" For companies with existing digital platforms, WatchWiz offers seamless integration possibilities. The app's advanced predictive analytics technology can complement and enhance existing services. This strategic integration allows the buyer to fortify their digital ecosystem, providing users with an extended and enriched experience, thereby increasing overall user satisfaction and loyalty.")
    
        st.write(" ### Brand Enhancement and Positive User Perception:")
        st.markdown(" The accuracy of WatchWiz's recommender system contributes to a positive user experience, enhancing the buyer's brand perception. By offering users content that aligns closely with their preferences, the buyer can establish the app as a reliable and user-centric platform. This positive association contributes to brand equity and fosters a favorable perception in the market.")

        st.write( " ### Data-Driven Innovation:")
        st.markdown(" As the app collects and analyzes vast amounts of user data over time, it becomes a valuable source of insights into evolving preferences, trends, and behaviors. This data-driven approach allows you to continually enhance and innovate the recommendation algorithm. By staying ahead of user preferences and industry trends, the app becomes a dynamic tool for adapting to changing market demands and maintaining relevance in the long run.")
    
        st.title( "Content-Based Filtering")
        col1, col2 = st.columns([2, 1])
        col2.markdown(" WatchWiz employs content-based filtering by analyzing user-generated tags, genres, and preferences along with movie attributes. This approach involves weighting features, calculating scores, and generating personalized recommendations based on comprehensive user and content profiles. The integration of user-generated tags ensures a more nuanced and engaging recommendation process, enhancing the app's ability to provide tailored content suggestions.")
        col1.image('resources/imgs/M.jpeg', use_column_width=True)

        st.title(" Collaborative-Based Filtering")
        col1, col2 = st.columns([2, 1])
        col2.markdown(" WatchWiz utilizes collaborative filtering, incorporating both user-based and item-based approaches. By analyzing user behavior and preferences, the app recommends content based on similarities with other users or items that share characteristics with those the user has enjoyed. This dual collaborative filtering strategy enhances the accuracy and diversity of personalized recommendations, providing users with a dynamic and engaging content discovery experience.")
        col1.image('resources/imgs/P.jpeg', use_column_width=True)
    # You may want to add more sections here for aspects such as an EDA,
    
    if page_selection == "Feedback":
        st.title("App Feedback")
        st.write(" Your feedback is invaluable to us! Please take a moment to share your thoughts on our app. Your insights and suggestions play a vital role in our continuous effort to enhance your user experience. The completion of this feedback form will provide us with valuable information on the app's strengths, areas for improvement, and any issues you may have encountered. Thank you for helping us create a better experience for you!")
        
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
            

    if page_selection == "Feedbacks":
        st.write("# App Feedback Form")

    # User Information Section
        st.write("## User Information")
        name = st.text_input("Your Full Name:")
        email = st.text_input("Your Email Address:")
        phone_number = st.text_input("Your Phone Number:")

    # Feedback Section
        st.write("## Feedback")
        overall_experience = st.selectbox(
        "How would you rate your overall experience with the app?",
        ["Excellent", "Good", "Average", "Poor"]
    )

        specific_feedback = st.text_area("Share specific feedback or suggestions:")

    # Bug Report Section
        st.write("## Bug Report (if any)")
        bug_description = st.text_area("Describe the issue or bug you encountered:")

    # Submit Button
        if st.button("Submit Feedback"):
        # You can add code here to save the feedback to a database or file
            st.success("Feedback submitted successfully! Thank you for your input.")


# Run the feedback form function

    # or to provide your business pitch.


if __name__ == '__main__':
    main()
