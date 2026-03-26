from flask import Flask, redirect, render_template_string

app = Flask(__name__)

# 3. Health Check
@app.route("/test")
def test():
    return "Server is Live!"

# This is for local testing; Vercel ignores this block
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
