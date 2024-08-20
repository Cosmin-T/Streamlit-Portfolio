
Portfolio App
=============

This code defines a `Stream` class that uses Streamlit to create a simple web application. It includes a welcome page, info pages for two apps (InstaBlast and DataDash), and a "Buy Me A Coffee" page.

The code uses various Streamlit components to create a basic user interface and fetches data from external APIs using the `requests` library.

Features
--------

### Info

* Displays a welcome message with a lottie animation
* Provides information about two applications: InstaBlast and DataDash
* Each application has a button to visit the corresponding website
* Includes a progress bar to indicate the loading status
* Displays a success or error message based on the website loading status

### Buy Me A Coffee

* Displays a lottie animation of a coffee cup

Getting Started
---------------

1. Install the required packages by running `pip install -r requirements.txt`
2. Run the app by executing `python main.py`
3. Open a web browser and navigate to `http://localhost:8501`

Components
----------

### Navigation.py

* Defines a `Stream` class that encapsulates the Streamlit app
* Includes methods for loading lottie animations, displaying information, and handling button clicks
* Uses the `streamlit_option_menu` and `streamlit_lottie` libraries to create a navigation menu and display lottie animations

### Main.py

* Imports the `Stream` class from `navigation.py`
* Creates an instance of the `Stream` class and calls its `welcome` and `container` methods to display the app

Libraries Used
--------------

* Streamlit
* Streamlit Option Menu
* Streamlit Lottie
* Requests
* Webbrowser
* Threading
* Time

License
-------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
