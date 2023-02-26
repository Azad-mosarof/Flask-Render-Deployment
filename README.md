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
The API endpoint URL is https://flask-render-app-glku.onrender.com/predict. You can send a POST request to this URL with the following parameters:

- input: Provide Input to the model for annual health expense prediction.

- The response is a JSON object with the following keys:

- jsonData: The predicted annual health care expense.

## Deployment
- Sign up for a Render account.

- Create a new Render app and link it to your GitHub repository.

- Configure the app by specifying the following:

- Build command: 
```sh
pip install -r requirements.txt
python app.py
```
Start command: 
```sh
python app.py
```
- Deploy the app and wait for it to build and start.

- Access the app URL to confirm that it's working.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
