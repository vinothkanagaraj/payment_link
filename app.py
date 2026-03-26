from flask import Flask, redirect

app = Flask(__name__)

# --- CONFIGURATION ---
# Your hidden UPI details
UPI_ID = "kpvino12345-1@okaxis"
NAME = "Vinoth"
AMOUNT = "99.00"

@app.route('/')
def direct_pay():
    # Construct the deep link
    upi_url = f"upi://pay?pa={UPI_ID}&pn={NAME}&am={AMOUNT}&cu=INR"
    
    # Return a 302 Found redirect
    # This is a 'Header Redirect' - the browser never stays on your domain
    return redirect(upi_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)