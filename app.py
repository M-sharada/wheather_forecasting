import json
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

received_data = {}  # Initialize an empty dictionary to store received data


@app.route('/', methods=['GET', 'POST'])
def get_data():
    global received_data  # Use global keyword to access the global variable
    if request.method == 'POST':
        if request.is_json:
            received_data = request.json  # Update global variable with received data
            print("Received data '/' :", received_data)
            return jsonify({'data': received_data}), 200
        else:
            print("Invalid JSON data in request.")
            return jsonify({'error': 'Invalid JSON data in request.'}), 400
    else:
        return render_template("sample.html")


@app.route('/getimage', methods=['GET'])
def index():
    global received_data  # Use global keyword to access the global variable
    date2=received_data.get('date2')
    hour=received_data.get('hour')
    state_name = received_data.get('state_name', '') 
    state = state_name.split()[0] 
    
    image_filename = f"{received_data.get('date2')}_{received_data.get('hour')}.{state}.png" 
    image_url = url_for('static', filename=f'images/{image_filename}')

    print("Received data '/getimage' :", image_url)
    return render_template('getImages.html', image_url=image_url,date2=date2,hour=hour,state=state) 


if __name__ == '__main__':
    app.run(debug=True)
