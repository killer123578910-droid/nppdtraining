import streamlit as st
import plotly.express as px
import shap
import matplotlib.pyplot as plt
import pandas as pd
from req import (search_g,detail)
from predict import (predicting,get_input,get_model) 


feature_names = [
    "devs_encoded",
    "console_encoded",
    "genre_encoded",
    "critic_tier",
    "critic_power"
]


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Game Predictor",
    page_icon="🎮",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "search"

if "search_results" not in st.session_state:
    st.session_state.search_results = []

if "selected_game" not in st.session_state:
    st.session_state.selected_game = None

if "prediction" not in st.session_state:
    st.session_state.prediction = None


# ============================================================
# SEARCH FUNCTION
# ============================================================

def search_similar_games(game_name):


    results = search_g(game_name)
    return results




# ============================================================
# MODEL FUNCTION
# ============================================================

def predict_game(game_data):
    """
    TODO:
    Kết nối model Machine Learning của bạn.

    Model của bạn chỉ trả về:

        "hot ass"

    hoặc:

        "normal"

    Ví dụ:

        prediction = model.predict([
            [
                game_data["developer"],
                game_data["genre"],
                game_data["platform"],
                game_data["metacritic"]
            ]
        ])

        return prediction[0]
    """
    # ========================================================
    devs,cons,gen,crit=game_data["developer"],game_data["platform"],game_data["genre"],(game_data["critics"]/10)
    df_input=get_input(devs,cons,gen,crit)
    return predicting(df_input)
    #


# ============================================================
# RESET
# ============================================================

def reset_search():

    st.session_state.page = "search"

    st.session_state.search_results = []

    st.session_state.selected_game = None

    st.session_state.prediction = None


# ============================================================
# PREDICTION DISPLAY
# ============================================================

def show_prediction(prediction):

    st.divider()

    st.header("🤖 Model Prediction")

    prediction = str(prediction).lower().strip()


    # ========================================================
    # HOT ASS
    # ========================================================

    if prediction == "hot ass":

        st.error(
            "🔥 HOT ASS"
        )

        st.subheader(
            "🔥 THIS GAME IS HOT ASS 🔥"
        )

        st.write(
            "The model thinks this game belongs "
            "to the **HOT ASS** class."
        )

        # Meme native Streamlit
        col1, col2, col3 = st.columns(3)

        with col1:

            st.write("🔥🔥🔥")

        with col2:

            st.write(
                "## 💀"
            )

            st.caption(
                "Model after seeing the game:"
            )

        with col3:

            st.write("🔥🔥🔥")


        st.warning(
            "💀 Bro... the model did NOT cook."
        )


    # ========================================================
    # NORMAL
    # ========================================================

    elif prediction == "normal":

        st.success(
            "😐 NORMAL"
        )

        st.subheader(
            "😐 Nothing crazy... just NORMAL."
        )

        st.write(
            "The model thinks this game belongs "
            "to the **NORMAL** class."
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write("😐")

        with col2:

            st.write(
                "## 🗿"
            )

            st.caption(
                "Model reaction:"
            )

        with col3:

            st.write("😐")


        st.info(
            "🗿 The model has spoken. It's normal."
        )


    # ========================================================
    # UNKNOWN RESULT
    # ========================================================

    else:

        st.warning(
            f"Unknown model output: {prediction}"
        )

# ============================================================
# GLOBAL FEATURE IMPORTANCE
# ============================================================

def show_global_importance(model, feature_names):

    df_imp = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    df_imp = df_imp.sort_values(
        by="Importance",
        ascending=True
    )

    fig = px.bar(
        df_imp,
        x="Importance",
        y="Feature",
        orientation="h",
        title="📈 Global Feature Importance",
        color="Importance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
# ============================================================
# LOCAL SHAP EXPLANATION
# ============================================================

def show_shap_explanation(model, input_df):

    try:

        explainer = shap.TreeExplainer(model)

        shap_explanation = explainer(input_df)

        # Nếu binary classification
        if len(shap_explanation.shape) == 3:

            shap_explanation = shap_explanation[..., 1]

        # Vẽ waterfall
        fig = plt.figure()

        shap.plots.waterfall(
            shap_explanation[0],
            show=False
        )

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)
        
        st.subheader("📋 What do these features mean?")

        feature_info = {
            "devs_encoded":
                "Encoded representation of the game developer.",

            "console_encoded":
                "Encoded representation of the platform / console.",

            "genre_encoded":
                "Encoded representation of the game's genre.",

            "critic_tier":
                "A categorized representation of the critic score.",

            "critic_power":
                "A numerical representation derived from the critic score."
        }

        for feature in input_df.columns:

            with st.expander(
                f"🔹 {feature}"
            ):

                st.write(
                    feature_info.get(
                        feature,
                        "Feature used by the model."
                    )
                )

                st.write(
                    f"Input value: `{input_df.iloc[0][feature]}`"
                )

    except Exception as e:

        st.error(
            "❌ Cannot generate SHAP explanation."
        )

        st.exception(e)
    
# ============================================================
# MODEL EXPLANATION
# ============================================================

def show_model_explanation(
    model,
    input_df,
    feature_names
):

    st.divider()

    st.header("🧠 Why did the model make this prediction?")

    # ========================================================
    # MODEL INFORMATION
    # ========================================================

    st.subheader("🤖 Model Information")

    model_name = type(model).__name__

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Model",
            model_name
        )

    with col2:
        st.metric(
            "Number of features",
            len(feature_names)
        )

    st.caption(
        "The explanation below shows how each input feature "
        "contributed to this specific prediction."
    )


    # ========================================================
    # BASIC SHAP EXPLANATION
    # ========================================================

    with st.expander(
        "📖 How to read the SHAP graph?"
    ):

        st.markdown(
            """
### 🔹 What is `f(x)`?

`f(x)` is the **model's output for the current game**.

In other words:

> **f(x) = what the model predicts for this particular game.**

For your classifier, this corresponds to the model's prediction
for the current input.

---

### 🔹 What is `E[f(x)]`?

`E[f(x)]` is the **expected / average model output** over the
background data used by SHAP.

You can think of it as:

> **"What would the model normally predict before seeing this
> particular game?"**

The SHAP explanation starts from `E[f(x)]` and then shows how
each feature moves the prediction toward or away from `f(x)`.

---

### 🔹 What do the red and blue values mean?

🔴 **Red / positive contribution**

The feature pushes the prediction **toward the explained class**.

🔵 **Blue / negative contribution**

The feature pushes the prediction **away from the explained class**.

The longer the bar, the stronger the contribution.

---

### 🔹 How should I interpret a feature?

For example:

**Critic Power → +0.35**

means that this feature contributed positively to the
prediction.

While:

**Console → -0.18**

means that the feature pushed the prediction in the opposite
direction.

This does **not** mean that the feature is inherently
"good" or "bad".

It only describes its effect for this particular prediction.
"""
        )


    # ========================================================
    # TABS
    # ========================================================

    tab1, tab2 = st.tabs([
        "🔍 Local Explanation",
        "📈 Global Feature Importance"
    ])


    # ========================================================
    # LOCAL SHAP
    # ========================================================

    with tab1:

        st.subheader(
            "🔍 Why this game received this prediction"
        )

        st.write(
            "This graph explains the contribution of each feature "
            "for the current game."
        )

        show_shap_explanation(
            model,
            input_df
        )


        st.info(
            "💡 The SHAP graph explains one game at a time. "
            "It tells you which features pushed the model's "
            "decision in each direction."
        )


    # ========================================================
    # GLOBAL IMPORTANCE
    # ========================================================

    with tab2:

        st.subheader(
            "📈 Which features matter most to the model?"
        )

        st.write(
            "Global feature importance summarizes how important "
            "each feature is across the model as a whole."
        )

        show_global_importance(
            model,
            feature_names
        )

        st.info(
            "💡 Global importance tells you which features the "
            "model relies on most overall. It does not explain "
            "the prediction of one specific game."
        )
# ============================================================
# MANUAL INPUT FORM
# ============================================================

def manual_input_page():

    st.title("📝 Enter Game Information")

    st.subheader(
        "Manually enter the game statistics"
    )

    st.info(
        "💡 You can use this option directly from "
        "the start if you already know the game's stats."
    )

    st.divider()


    with st.form("manual_game_form"):

        st.header("🎮 Game Statistics")

        col1, col2 = st.columns(2)

        with col1:

            developer = st.text_input(
                "🏢 Developer",
                placeholder="Example: Rockstar Games"
            )

            genre = st.text_input(
                "🎭 Genre",
                placeholder="Example: Action"
            )

        with col2:

            platform = st.text_input(
                "🎮 Platform",
                placeholder="Example: PC"
            )

            metacritic = st.slider(
                "⭐ Metacritic",
                min_value=1,
                max_value=100,
                value=75
            )

        st.divider()

        submitted = st.form_submit_button(
            "🤖 Predict Game",
            use_container_width=True
        )


    if submitted:

        if not developer.strip():

            st.error(
                "Please enter the developer."
            )

            return

        if not genre.strip():

            st.error(
                "Please enter the genre."
            )

            return

        if not platform.strip():

            st.error(
                "Please enter the platform."
            )

            return


        game_data = {

            "name": "Manual Input",

            "developer": developer,

            "genre": genre,

            "platform": platform,

            "critics": metacritic
        }


        with st.spinner(
            "🤖 Running model..."
        ):

            prediction = predict_game(
                game_data
            )


        st.session_state.selected_game = game_data

        st.session_state.prediction = prediction

        st.session_state.page = "prediction"

        st.rerun()


    st.divider()


    if st.button(
        "← Back to search",
        use_container_width=True
    ):

        reset_search()

        st.rerun()

def manual_prediction_page():
    game_data=st.session_state.selected_game

    st.title("🤖 Prediction Result")

    st.subheader("Your game prediction")

    st.divider()

    show_prediction(
        st.session_state.prediction
    )

    st.divider()
        # ========================================================
    # MODEL EXPLANATION
    # ========================================================

    if st.session_state.prediction is not None:

        devs,cons,gen,crit=game_data["developer"],game_data["platform"],game_data["genre"],(game_data["critics"]/10)

        input_df = get_input(
            devs,cons,gen,crit
        )

        show_model_explanation(
            get_model(),
            input_df,
            feature_names
        )

    

    if st.button(
        "🔄 Search another game",
        use_container_width=True
    ):

        reset_search()

        st.rerun()
# ============================================================
# SEARCH PAGE
# ============================================================

def search_page():
    

    st.title("🎮 Game Predictor")

    st.subheader(
        "Find a game or enter its statistics manually"
    )

    st.write(
        "Choose how you want to use the prediction system."
    )

    st.divider()


    # ========================================================
    # TWO OPTIONS
    # ========================================================

    search_col, manual_col = st.columns(
        2,
        gap="large"
    )


    # ========================================================
    # OPTION 1 — SEARCH
    # ========================================================

    with search_col:

        st.header("🔎 Search for a game")

        st.write(
            "Enter a game name and find the "
            "10 closest matches."
        )

        st.write(
            "🎮 → 🔎 → 📋 → 🤖"
        )

        game_name = st.text_input(
            "Game name",
            placeholder="Example: Grand Theft Auto",
            key="search_game"
        )

        search_button = st.button(
            "🔎 Search Game",
            use_container_width=True
        )


        if search_button:

            if not game_name.strip():

                st.warning(
                    "Please enter a game name."
                )

            else:

                with st.spinner(
                    "🔍 Searching..."
                ):

                    results = search_similar_games(
                        game_name.strip()
                    )

                st.session_state.search_results = results

                if results:

                    st.session_state.page = "results"

                else:

                    st.session_state.page = "input"

                st.rerun()


    # ========================================================
    # OPTION 2 — MANUAL
    # ========================================================

    with manual_col:

        st.header("📝 Enter stats manually")

        st.write(
            "Already know the game's information?"
        )

        st.write(
            "🏢 → 🎭 → 🎮 → ⭐ → 🤖"
        )

        st.write(
            "Skip the search and enter the "
            "game statistics directly."
        )

        st.write("")

        if st.button(
            "📝 Enter Game Stats",
            use_container_width=True
        ):

            st.session_state.page = "input"

            st.rerun()


    st.divider()


    # ========================================================
    # INFO
    # ========================================================

    st.header("🧠 How it works")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            "**1️⃣ Search**\n\n"
            "Search for a game and the system "
            "finds similar games."
        )

    with col2:

        st.info(
            "**2️⃣ Select / Enter**\n\n"
            "Choose an existing game or "
            "manually enter its statistics."
        )

    with col3:

        st.info(
            "**3️⃣ Predict**\n\n"
            "The trained model classifies "
            "the game as HOT ASS or NORMAL."
        )


# ============================================================
# RESULTS PAGE
# ============================================================

def results_page():

    st.title("🔎 Search Results")

    results = st.session_state.search_results

    st.write(
        f"Found **{len(results)}** closest matches."
    )

    st.divider()


    # ========================================================
    # 10 GAME CARDS
    # ========================================================

    for row in range(5):

        col1, col2 = st.columns(2)

        indexes = [
            row * 2,
            row * 2 + 1
        ]


        for col, index in zip(
            [col1, col2],
            indexes
        ):

            if index >= len(results):

                continue


            game = results[index]


            with col:

                with st.expander(
                    f"🎮 {game['name']}"
                ):

                    st.image(
                        game["image"],
                    )


                    info1, info2 = st.columns(2)

                    with info1:

                        st.write(
                            f"🎭 **Genre:** "
                            f"{game['genre']}"
                        )



                    with info2:

                        st.write(
                            f"🎮 **Platform:** "
                            f"{game['platform']}"
                        )


                    if st.button(
                        "🎮 Select this game",
                        key=f"select_{game['id']}",
                        use_container_width=True
                    ):

                        st.session_state.selected_game = game["id"]

                        st.session_state.prediction = None

                        st.session_state.page = "details"

                        st.rerun()


    st.divider()


    if st.button(
        "🔄 Search another game",
        use_container_width=True
    ):

        reset_search()

        st.rerun()


# ============================================================
# DETAILS PAGE
# ============================================================

def details_page():

    game = st.session_state.selected_game
    
    de=detail(game)
    st.title("🎮 Game Details")

    st.header(
        de["name"]
    )

    st.divider()


    # ========================================================
    # IMAGE + DESCRIPTION
    # ========================================================

    image_col, info_col = st.columns(
        [1, 2],
        gap="large"
    )


    with image_col:

        st.image(
            de["image"],
        )


    with info_col:

        st.subheader(
            "📖 Description"
        )

        st.write(
            de["description"]
        )

        st.divider()

        st.subheader(
            "📊 Game Statistics"
        )

        col1, col2 = st.columns(2)

        with col1:


            st.metric(
                "🏢 Developer",
                de["developer"]
            )


        with col2:

            st.metric(
                "⭐ Metacritic",
                f"{de['critics']}/100"
            )

            st.metric(
                "🎮 Platform",
                de["platform"]
            )
            st.metric(
                "🎮 Release_date:",
                de["release"]
            )




    st.divider()


    # ========================================================
    # GENRE
    # ========================================================

    st.subheader("🎭 Genre")

    st.info(
        de["genre"]
    )


    # ========================================================
    # PREDICTION
    # ========================================================

    if st.session_state.prediction is None:

        st.header("🤖 Model Prediction")

        st.write(
            "Run the trained model to classify this game."
        )

        if st.button(
            "🤖 Predict",
            use_container_width=True
        ):

            with st.spinner(
                "🤖 Model is thinking..."
            ):

                prediction = predict_game(
                de
                )

            st.session_state.prediction = prediction

            st.rerun()

    else:

        show_prediction(
            st.session_state.prediction
        )
        
      # ========================================================
    # MODEL EXPLANATION
    # ========================================================

    if st.session_state.prediction is not None:

        devs,cons,gen,crit=de["developer"],de["platform"],de["genre"],(de["critics"]/10)

        input_df = get_input(
            devs,cons,gen,crit
        )

        show_model_explanation(
            get_model(),
            input_df,
            feature_names
        )


    st.divider()


    if st.button(
        "🔄 Search another game",
        use_container_width=True
    ):

        reset_search()

        st.rerun()


# ============================================================
# ROUTER
# ============================================================

if st.session_state.page == "search":

    search_page()

elif st.session_state.page == "results":

    results_page()

elif st.session_state.page == "details":

    details_page()

elif st.session_state.page == "input":

    manual_input_page()
elif st.session_state.page == "prediction":
    manual_prediction_page()
