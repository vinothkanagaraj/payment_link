from flask import Flask, redirect, render_template_string

app = Flask(__name__)

# --- CONFIGURATION ---
UPI_ID = "kpvino12345-1@okaxis"
NAME = "Vinoth"
AMOUNT = "99.00"

# Centralized URL generator to avoid typos
def get_upi_url():
    return f"upi://pay?pa={UPI_ID}&pn={NAME}&am={AMOUNT}&cu=INR"

# 1. The "Bridge" Page (Best for WhatsApp)
@app.route('/pay')
def pay_endpoint():
    upi_url = get_upi_url()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redirecting to UPI...</title>
            <script>
                // Auto-trigger
                window.onload = function() {
                    window.location.href = "{{ upi }}";
                };
            </script>
        </head>
        <body style="text-align:center;font-family:sans-serif;padding-top:50px;background:#f4f4f4;">
            <div style="background:white;padding:30px;display:inline-block;border-radius:15px;box-shadow:0 5px 15px rgba(0,0,0,0.1);">
                <h3>Opening UPI App...</h3>
                <p>Paying: <strong>{{ name }}</strong></p>
                <p>Amount: <strong>₹{{ amount }}</strong></p>
                <br>
                <a href="{{ upi }}" style="padding:15px 25px;background:#28a745;color:white;text-decoration:none;border-radius:8px;font-weight:bold;display:block;">
                    OPEN GPAY / PHONEPE / PAYTM
                </a>
            </div>
        </body>
        </html>
    ''', upi=upi_url, name=NAME, amount=AMOUNT)

# 2. The Direct Redirect (Fastest, but sometimes blocked by WhatsApp)
@app.route('/upi')
def direct_pay():
    return redirect(get_upi_url())

# 3. Health Check
@app.route("/")
def test():
    return "Server is Live!"

# This is for local testing; Vercel ignores this block
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
