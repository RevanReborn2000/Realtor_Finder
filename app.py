# app.py

from flask import Flask, render_template
from convex import ConvexClient

# Initialize the Convex client with your project URL
convex = ConvexClient('https://aware-curlew-760.convex.cloud')  # Replace with your actual Convex URL
app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Directly assign the result to data
        data = convex.query('fetchMessages')
        # If data is None or not a list, set it to an empty list
        if not isinstance(data, list):
            data = []
    except Exception as e:
        data = []
        print(f"Error fetching data from Convex: {e}")
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

