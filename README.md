<h1>AI Model Deployment using Flask and Render</h1>

<p>This project demonstrates how to deploy an AI model using Flask and Render cloud. The AI model was built, trained and deployed on the cloud, and is accessible via an API.</p><br>

## Prerequisites
- Python 3.6 or later 
- Flask 2.0.1 or later 
- Render account**

## Getting Started
  
1. Clone this repository:<br>
```sh
git clone https://github.com/your-username/your-repo-name.git
```

2. Install the required dependencies:<br>
```sh
pip install -r requirements.txt
```

3. Update the API endpoint URL in the app.js file to match your Render app URL

4. Start the Flask app:
```sh
python app.py
```

5. Navigate to the app URL in your browser.

## API Usage
The API endpoint URL is https://your-app-url.com/predict. You can send a POST request to this URL with the following parameters:

- input: Provide Input to the model for annual health expenses prediction.

The response is a JSON object with the following keys:

- label: The predicted label for the text.
- confidence: The confidence score for the predicted label.


