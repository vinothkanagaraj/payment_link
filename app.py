from flask import Flask, redirect, render_template_string

app = Flask(__name__)

# --- CONFIGURATION ---
# Your hidden UPI details
UPI_ID = "kpvino12345-1@okaxis"
NAME = "Vinoth"
AMOUNT = "99.00"

UPI_URL = "upi://pay?pa=kpvino12345-1@okaxis&pn=Vinoth&am=99.00&cu=INR"

@app.route('/pay') # This creates the http://domain.com/pay endpoint
def pay_endpoint():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redirecting...</title>
            <script>
                // Try to open UPI app immediately
                window.location.href = "{{ upi }}";
            </script>
        </head>
        <body style="text-align:center;font-family:sans-serif;padding-top:50px;">
            <h3>Opening UPI App...</h3>
            <p>If it doesn't open, click below:</p>
            <a href="{{ upi }}" style="padding:15px 25px;background:#28a745;color:white;text-decoration:none;border-radius:5px;font-weight:bold;">
                OPEN GPAY / PHONEPE
            </a>
        </body>
        </html>
    ''', upi=UPI_URL)

@app.route('/')
def direct_pay():
    # Construct the deep link
    upi_url = f"upi://pay?pa={UPI_ID}&pn={NAME}&am={AMOUNT}&cu=INR"
    
    # Return a 302 Found redirect
    # This is a 'Header Redirect' - the browser never stays on your domain
    return redirect(upi_url)
@app.route("/test")
def test():
    return "Hello, World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
