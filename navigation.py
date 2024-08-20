import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import webbrowser
import threading
import time
import os


class Stream:
    def __init__(self, st):
        self.st = st
        self.st_lottie = st_lottie

    def load_lottie(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching lottie data: {e}")

    def welcome(self):
        self.st.markdown("##")
        col1, col2 = self.st.columns(2)
        with col1:
            for _ in range(1):
                self.st.markdown("##")
            self.st.title("May theIndent be With You!!!")
        with col2:
            lottie_coder = self.load_lottie("https://lottie.host/5f341e13-e3bc-4e8f-a9de-7b07749c5f0c/YL7OP4IECI.json")
            st_lottie(lottie_coder)
        self.st.write('---')

    def application_logic(self, url, success, fail, prefix=""):
        """
        This function handles the application logic for the Streamlit app.

        Args:
        url (str): The URL to visit.
        success (str): The success message to display.
        fail (str): The error message to display.
        prefix (str): The prefix for the URL (default is an empty string).
        """

        # Create a placeholder for the progress bar and messages
        placeholder = st.empty()
        progress_bar = st.empty()

        # Initialize the visited state
        if 'visited' not in st.session_state:
            st.session_state.visited = False

        # Create the button code
        button_code = f"""
            <style>
            .custom-button {{
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                background-color: #262730;
                border: none;
                border-radius: 5px;
                text-align: center;
                text-decoration: none;
                width: 100%;
                transition: background-color 0.3s ease;
            }}
            .custom-button:hover {{
                background-color: #6a2336;
                color: white;
            }}
            </style>
            <a href="{url}" target="_blank" class="custom-button" onclick="visitLink()">Visit</a>
            <script>
            function visitLink() {{
                window.parent.visitLinkCallback();
            }}
            </script>
        """

        # Display the button
        self.st.markdown(button_code, unsafe_allow_html=True)

        # Define a callback function to handle the button click
        def visit_link_callback():
            st.session_state.visited = True

        # Add the callback function to the Streamlit app
        self.st.js("window.visitLinkCallback = () => {window.parent.visitLinkCallback();};")

        # Check if the button has been clicked
        if st.session_state.visited:
            # Display the progress bar
            progress_bar.progress_bar(0)

            # Simulate some work
            for i in range(100):
                time.sleep(0.001)
                progress_bar.progress_bar(i + 1)

            # Try to visit the URL
            try:
                response = requests.head(url)
                if response.status_code == 200:
                    # Display a success message
                    placeholder.success(success)
                    progress_bar.empty()
                    time.sleep(3)
                    placeholder.empty()
                    st.session_state.visited = False
                else:
                    # Display an error message
                    placeholder.error(fail)
                    progress_bar.empty()
                    time.sleep(3)
                    placeholder.empty()
                    st.session_state.visited = False
            except requests.exceptions.RequestException as e:
                # Display an error message
                placeholder.error(f"Error opening link: {e}")
                progress_bar.empty()
                st.session_state.visited = False

    def information(self, selected):
        if selected == 'Info':
            col1, col2 = self.st.columns(2)
            with col1:
                for _ in range(1):
                    self.st.markdown("###")
                self.st.subheader('Warning! Boring stuff down bellow!')
            with col2:
                lottie_coder = self.load_lottie("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
                self.st_lottie(lottie_coder)

            self.st.write('---')

            self.st.subheader('InstaBlast')
            self.st.markdown('###### Blast your message to the masses, without losing your mind!')
            self.application_logic('https://www.instagram.com', 'InstaBlast Loaded', 'Failed to Load InstaBlast', prefix='1')
            with self.st.expander('The Boring Stuff', expanded=False):
                self.st.info(
                    """
                    Are you tired of manually sending messages to all your followers?
                    Do you want to increase your outreach without increasing your stress levels?
                    Look no further than InstaBlast!
                    This app offers three primary functionalities to help you conquer the world of Instagram:
                    """
                    )
                self.st.info(
                    """
                    * Lead Fetching: Extract valuable connections from specific usernames, because who doesn't love a good treasure hunt?

                    * Mass Messaging to all Followers: Send a single message to all your followers, because who doesn't love a good broadcast?

                    * Mass Messaging to all Leads: Send targeted messages to users who are interested in your content, because who doesn't love a good lead?

                    """
                )
                self.st.info(
                    """
                    Example Use Cases:

                    * Send a promotional message to all your followers about your new product launch.

                    * Send a personalized message to all your leads about your new service offering.

                    * Extract leads from a specific hashtag or username to grow your business.

                    """
                )
            self.st.write('---')
            self.st.subheader('DataDash')
            self.st.markdown('###### Dash to insights, without getting lost in data!')
            self.application_logic('https://www.datadash.com', 'DataDash Loaded', 'Failed to Load DataDash', prefix='2')
            with self.st.expander('The Boring Stuff', expanded=False):
                self.st.info(
                    """
                    Are you tired of sifting through spreadsheets and databases to find meaningful insights?
                    Do you want to visualize your data without losing your mind?
                    Look no further than DataDash! This Power BI tool allows you to:
                    """
                )
                self.st.info(
                    """
                    * Connect to databases: Link your database to our tool and start visualizing your data in minutes.

                    * Upload Excel files: Upload your Excel files and start analyzing your data in seconds.
                    """
                )
                self.st.info(
                    """
                    Example Use Cases:

                    * Connect to your sales database to track sales performance and identify trends.

                    * Upload your customer data to create personalized marketing campaigns.

                    * Visualize your website traffic to optimize your online presence.
                    """
                )

    def buy_me_coffee(self, selected):
        if selected == 'Buy Me A Coffee':
            self.st.write('---')
            for _ in range(1):
                self.st.markdown("##")
            url = "https://revolut.me/cosminhbs7"
            col1, col2 = self.st.columns(2)
            with col1:
                self.st.markdown('###### If you enjoy my work, please consider buying me a coffee!')
            with col2:
                button_code = f"""
                    <style>
                    .custom-button {{
                        display: inline-block;
                        padding: 10px 20px;
                        font-size: 16px;
                        font-weight: bold;
                        color: white;
                        background-color: #262730;
                        border: none;
                        border-radius: 5px;
                        text-align: center;
                        text-decoration: none;
                        width: 100%;
                        transition: background-color 0.3s ease;
                    }}
                    .custom-button:hover {{
                        background-color: #6a2336;
                        color: white;
                    }}
                    </style>
                    <a href="{url}" target="_blank" class="custom-button">Buy Me A Coffee</a>
                    """
                self.st.markdown(button_code, unsafe_allow_html=True)
            self.st.write('---')
            self.st_lottie(self.load_lottie("https://lottie.host/6da5d610-becb-4650-a196-c45330ba89d8/yFOvC9Qw3t.json"))


    def container(self):
        self.st.markdown("##")
        with self.st.container():
            selected = option_menu(
                menu_title=None,
                options=['Info', 'Buy Me A Coffee'],
                icons=['read_me', 'coffee'],
                default_index=0,
                orientation="horizontal",
            )

        self.information(selected)
        self.buy_me_coffee(selected)