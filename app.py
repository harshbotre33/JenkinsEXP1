from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# In-memory storage for demonstration (resets on restart)
registrations = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        ticket_type = request.form.get('ticket_type')

        # Basic validation
        if not name or not email:
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('register'))

        # Store registration
        registration = {
            'name': name,
            'email': email,
            'ticket_type': ticket_type
        }
        registrations.append(registration)

        flash('Registration successful!', 'success')
        return redirect(url_for('success', name=name))

    return render_template('register.html')

@app.route('/success')
def success():
    name = request.args.get('name', 'Attendee')
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)