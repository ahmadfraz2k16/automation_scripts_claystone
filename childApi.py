import re
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/api/register', methods=['POST'])


def register():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

# simple validations
    if (email is None or email.strip() == ""):
        return jsonify({"error": "Email cannot be empty"}), 400
    if not (re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        return jsonify({"error": "Invalid email address"}), 400
    if (password is None or password.strip() == ""):
        return jsonify({"error": "Password cannot be empty"}), 400
    if (len(password) < 8):
        return jsonify({"error": "Password should be at least 8 characters long"}), 400
    if (password != confirm_password):
        return jsonify({"error": "Password and confirm password don't match"}), 400

    return jsonify({"message": "User registered successfully"},
                   {"email": email},
                   {"password": password}), 201

if __name__ == '__main__':
    app.run(debug=True)
