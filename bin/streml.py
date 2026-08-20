import streamlit as st
import random
import pandas as pd
from req import search_g
from req import detail
from predict import predicting 


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
    # TODO: GỌI MODEL CỦA BẠN
    # ========================================================

    # prediction = model.predict(...)
    #
    # return prediction[0]


    # ========================================================
    # MOCK
    # XÓA SAU KHI KẾT NỐI MODEL
    # ========================================================

    return random.choice([
        "hot ass",
        "normal"
    ])


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

            "metacritic": metacritic
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
                    game
                )

            st.session_state.prediction = prediction

            st.rerun()

    else:

        show_prediction(
            st.session_state.prediction
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
