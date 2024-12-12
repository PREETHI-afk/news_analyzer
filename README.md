Fake News Analyzer API and Web Interface

This project is a Fake News Analyzer that provides a simple API and a web-based interface to determine whether a given text is classified as "real" or "fake."
Features

    REST API:
        Endpoint: /predict
        Method: POST
        Input: JSON object containing the text to analyze (e.g., {"text": "Some news text"}).
        Output: JSON response with the classification result (real or fake).

    Web Interface:
        A user-friendly web page to input news text and analyze its authenticity.
        Results are displayed on the same page.

How to Run
Prerequisites:

    Python 3.x installed.
    Required Python libraries: Flask, scikit-learn, and pickle.

Setup Instructions:

    Clone the Project:
        Download or clone the project to your local system.

    Install Dependencies:
        Run the following command to install the necessary libraries:

    pip install flask scikit-learn

Run the Application:

    In the project directory, execute:

        python app.py

        The application will start on http://127.0.0.1:5001.

    Access the Web Interface:
        Open a browser and navigate to http://127.0.0.1:5001.

File Structure

    app.py: The main Flask application that serves the API and web interface.
    model.pkl & vectorizer.pkl: Pre-trained Naive Bayes model and TfidfVectorizer used for text classification.
    index.html: The web page for analyzing news text.

Example Usage
API:

Send a POST request to the /predict endpoint with a JSON payload:

{
  "text": "Breaking: Scientists discover a new cure for cancer!"
}

Response:

{
  "success": true,
  "prediction": "real"
}

Web Interface:

    Open the browser at http://127.0.0.1:5001.
    Enter text in the input box and click Analyze.
    The result will be displayed below the button.

Notes

    This is a development server. Avoid using it in production environments.
    For production, consider using a WSGI server like gunicorn.
    Ensure the saved model (model.pkl) and vectorizer (vectorizer.pkl) exist in the project directory.



THE STRUCTURE SHOULD BE AS BELOW

    project/
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
└── templates/
    └── index.html
