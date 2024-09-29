import streamlit as st

# Example user profile and study plan generation logic
def personalize_study_plan(user_profile, subject):
    learning_style = user_profile.get('learning_style', 'visual')
    time_available = user_profile.get('time_available', 2)  # Default to 2 hours
    current_level = user_profile.get('current_level', 'beginner')

    # Simple logic to personalize a study plan
    study_plan = f"Study Plan for {subject}\n"
    study_plan += f"Learning Style: {learning_style}\n"
    study_plan += f"Time Available: {time_available} hours per day\n"
    study_plan += f"Current Level: {current_level}\n"
    study_plan += "Suggested Topics: Basic concepts, followed by examples."

    return study_plan

# Streamlit App Interface
st.title("Personalized Study Plan Generator")

# Get user input for subject
subject = st.text_input("Enter the subject:", "Mathematics")

# Create a user profile dictionary (replace with dynamic inputs if needed)
learning_style = st.selectbox("Select your learning style", ['visual', 'auditory', 'kinesthetic'])
study_hours = st.slider("How many hours can you study per day?", 1, 8, 2)

user_profile = {
    'learning_style': learning_style,
    'time_available': study_hours,
    'current_level': 'beginner'
}

# Generate the study plan
if st.button("Generate Study Plan"):
    study_plan = personalize_study_plan(user_profile, subject)
    st.write(study_plan)
