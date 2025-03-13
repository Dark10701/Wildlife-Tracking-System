from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="wildlife_tracking"
)
cursor = db.cursor(dictionary=True)

# API to Fetch Real-Time Tracking Data
@app.route('/api/tracking')
def get_tracking_data():
    query = """
    SELECT a.name, t.latitude, t.longitude, t.timestamp
    FROM Animals a
    JOIN Tracking_Data t ON a.animal_id = t.animal_id
    WHERE t.timestamp >= NOW() - INTERVAL 1 HOUR;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify(data)

# Render Webpage with Map
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
