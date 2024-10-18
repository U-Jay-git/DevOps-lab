from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        phone = request.form['phone']
        college = request.form['college']
        
        # Process the data as needed (e.g., store it, print it, etc.)
        print("Registration done successfully!")
        print(f"Name: {name}, Email: {email}, Event: {event}, Phone: {phone}, College: {college}")

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return "Registration done successfully!"

if __name__ == '__main__':
    app.run(debug=True)
