import streamlit as st
from datetime import date

st.set_page_config(page_title="Mood Tracker", page_icon="😊")

# Sidebar Navigation
page = st.sidebar.radio("Menu", ["About", "Profile", "Track Mood"])

# ABOUT PAGE
if page == "About":

    st.title("Simple Mood Tracker")

    st.header("About This App")

    st.write("This app helps girls track their daily mood.")

    st.subheader("Use Case")
    st.write("Users can record how they feel every day.")

    st.subheader("Target Users")
    st.write("Girls who want to monitor their emotions.")

    st.subheader("Inputs")
    st.write("Name, age, date, mood, energy level, sleep hours, activities.")

    st.subheader("Outputs")
    st.write("Mood summary and simple feedback.")

    st.info("This is a simple Streamlit UI demonstration.")

# PROFILE PAGE
elif page == "Profile":

    st.title("User Information")

    name = st.text_input("Your Name")

    age = st.number_input("Age", 10, 50)

    today_date = st.date_input("Select Date", date.today())

    save = st.button("Save Profile")

    if save:
        st.success("Profile saved!")

# MOOD TRACKER PAGE
elif page == "Track Mood":

    st.title("🌸 Daily Mood Tracker 🌸")

    mood = st.selectbox(
        "How do you feel today?",
        ["Happy 😊", "Okay 🙂", "Neutral 😐", "Sad 😢"]
    )

    energy = st.slider("Energy Level", 0, 10)

    sleep = st.slider("Sleep Hours", 0, 12)

    stress = st.radio("Stress Level", ["Low", "Medium", "High"])

    activities = st.multiselect(
        "What did you do today?",
        ["Study", "Watch movie", "Exercise", "Talk with friends"]
    )

    note = st.text_area("Write your feelings")

    color = st.color_picker("Pick your favorite color")

    smile = st.checkbox("I smiled today")

    relax = st.checkbox("I relaxed today")

    submit = st.button("Save Mood")

    if submit:

        st.success("Mood saved!")

        st.subheader("Mood Summary")

        st.write("Mood:", mood)
        st.write("Energy:", energy)
        st.write("Sleep:", sleep)
        st.write("Stress:", stress)
        st.write("Activities:", activities)

        if mood == "Happy 😊":
            st.balloons()
            st.success("Great! Keep smiling!")

        elif mood == "Sad 😢":
            st.warning("Take some rest and talk to a friend.")

        else:
            st.info("Hope you have a good day!")