from flask import Flask, jsonify, render_template
import pymysql

app = Flask(__name__)

# Configure database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aditya'
app.config['MYSQL_DB'] = 'wildlife_tracking'

def get_db_connection():
    conn = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor #Return results as dictionaries
    )
    return conn

@app.route('/api/tracking')
def get_tracking_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """SELECT a.name, t.latitude, t.longitude, t.timestamp 
               FROM Animals a 
               JOIN Tracking_Data t ON a.animal_id = t.animal_id 
               WHERE t.timestamp >= NOW() - INTERVAL 1 HOUR;"""
    
    cursor.execute(query)
    data = cursor.fetchall()

    print("Raw SQL Output:", data)

    cursor.close()
    conn.close()

    return jsonify(data) 



# Render Webpage with Map
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT a.name, t.latitude, t.longitude, t.timestamp FROM Animals a JOIN Tracking_Data t ON a.animal_id = t.animal_id WHERE t.timestamp >= NOW() - INTERVAL 1 HOUR;")
    tracking_data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', tracking_data=tracking_data)


if __name__ == "__main__":
    print("Flask app is starting now...")
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=8000)
