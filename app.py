import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


st.set_page_config(
    page_title="GlowUp Buddy ✨",
    page_icon="✨",
)


GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

chat_model = ChatGroq(
    model="llama3-8b-8192",
    api_key=GROQ_API_KEY
)


def generate_routine(category, user_input):
    prompt = f"""
    ### User Selection:
    - **Category**: {category}
    {user_input}
    Based on the user's selected category ({category}) and their input, 
    provide a detailed weekly routine without any introductory text. 
    Start directly with the personalized routine, including the products to be used in the morning and night, and their respective days. 
    Do not include any phrases like 'I see you've selected...' or 'Here's your routine...'.


    Example output would be like below
    ### Weekly Routine:

    **Morning Routine (Daily):**
    - **Cleanser**: Use a gentle face wash.
    - **Glycolic Acid 7% Toner**: Apply to gently exfoliate and brighten the skin.
    - **Salicylic Acid 2% with Niacinamide 5% Serum**: Helps with pores, oil control, and pimples.
    - **Vitamin C Serum**: For brightening and protecting skin from sun damage (optional: alternate with Kojic Acid some days).
    - **Peptide Moisturizer**: Hydrate and strengthen the skin barrier.
    - **Sunscreen**: Always apply sunscreen as the final step.

    **Night Routine:**
    - **Monday:**
        - **Cleanser**: Use a gentle face wash.
        - **Retinol Serum**: Apply to help with anti-aging.
        - **Alpha Arbutin Serum**: Apply to target hyperpigmentation.
    - **Tuesday:**
        - **Cleanser**: Use a gentle face wash.
        - **Kojic Acid Serum**: Apply to help with brightening and dark spots.
        - **Peptide Moisturizer**: Hydrate and strengthen the skin barrier.
    - **Wednesday:**
        - **Cleanser**: Use a gentle face wash.
        - **30% AHA/BHA Peeling Solution**: Apply for 10 minutes to exfoliate.
        - **Peptide Moisturizer**: Hydrate and strengthen the skin barrier.
    - **Thursday:**
        - **Cleanser**: Use a gentle face wash.
        - **Retinol Serum**: Apply to help with anti-aging.
        - **Alpha Arbutin Serum**: Apply to target hyperpigmentation.
    - **Friday:**
        - **Cleanser**: Use a gentle face wash.
        - **Kojic Acid Serum**: Apply to help with brightening and dark spots.
        - **Peptide Moisturizer**: Hydrate and strengthen the skin barrier.
    - **Saturday:**
        - **Cleanser**: Use a gentle face wash.
        - **30% AHA/BHA Peeling Solution**: Apply for 10 minutes to exfoliate.
        - **Peptide Moisturizer**: Hydrate and strengthen the skin barrier.
    - **Sunday:**
        - **Cleanser**: Use a gentle face wash.
        - **Face Mask**: Hyaluronic Acid, Aloe Vera, Vitamin C, Papaya, Pineapple, Clay Masks, Green Tea, Collagen, Peptide, Niacinamide, Kojic Acid, Salicylic Acid (any one for 15 to 20 mins).
        - **Peptide Moisturizer**: Apply as a gentle moisturizer (rest day).
    """

    system = "You are a helpful assistant."
    human = prompt
    prompt = ChatPromptTemplate.from_messages(
        [("system", system), ("human", human)])

    chain = prompt | chat_model
    response = chain.invoke(
        {"category": category, "user_input": user_input})

    # Print the completion returned by the LLM.
    print(response.content)
    return response.content


# App Title
st.header("Glow Up: Your Personal Care Buddy ✨", divider="gray")

# Sidebar for selecting care type
care_type = st.sidebar.selectbox(
    "Choose your care type:",
    ["Skin Care", "Body Care", "Hair Care"]
)

# Dynamic sections based on selected care type
if care_type == "Skin Care":
    st.header("🧴 Let's Customize Your Skin Care")

    # Dropdowns for Skin Care
    skin_texture = st.selectbox("What is your skin texture?", [
                                "Oily", "Dry", "Combination"])
    skin_type = st.selectbox("What is your skin type?", [
                             "Normal", "Sensitive"])
    skin_concerns = st.multiselect(
        "Which of these describe your concern?",
        ["Acne", "Open Pores", "Pigmentation",
            "Dark Circles", "Acne Marks & Scars", "Aging"]
    )

    if st.button("Generate Skin Care Routine"):
        user_input = f"- **Skin Texture:** {skin_texture}\n- **Skin Type:** {skin_type}\n- **Concerns:** {', '.join(skin_concerns)}"
        routine = generate_routine("Skin Care", user_input)
        st.subheader("Your Skin Care Routine")
        st.write(routine)

elif care_type == "Body Care":
    st.header("🛀 Time to Pamper Your Body")

    body_skin_type = st.selectbox("What is your body skin type?", [
                                  "Normal", "Dry", "Oily"])
    body_concerns = st.multiselect(
        "What is your primary concern?",
        ["Dryness", "Body Acne", "Stretch Marks", "Keratosis Pilaris",
            "Hyperpigmentation", "Rough Skin Texture"]
    )

    if st.button("Generate Body Care Routine"):
        user_input = f"- **Body Skin Type:** {body_skin_type}\n- **Concerns:** {', '.join(body_concerns)}"
        routine = generate_routine("Body Care", user_input)
        st.subheader("Your Body Care Routine")
        st.write(routine)

elif care_type == "Hair Care":
    st.header("💇‍♀️ Healthy Hair Starts Here")

    hair_type = st.selectbox("What is your hair type?", [
                             "Straight", "Wavy", "Curly", "Coily"])
    scalp_type = st.selectbox("What is your scalp type?", [
                              "Normal", "Oily", "Dry", "Sensitive"])
    hair_concerns = st.multiselect(
        "What is your primary concern?",
        ["Hair Fall", "Dandruff", "Dryness", "Frizz",
            "Split Ends", "Oily Scalp", "Scalp Irritation"]
    )

    if st.button("Generate Hair Care Routine"):
        user_input = f"- **Hair Type:** {hair_type}\n- **Scalp Type:** {scalp_type}\n- **Concerns:** {', '.join(hair_concerns)}"
        routine = generate_routine("Hair Care", user_input)
        st.subheader("Your Hair Care Routine")
        st.write(routine)

# Footer
st.markdown("---")
st.text("✨ Glow up every day with simple, effective routine")
