from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get("message")
        if not message:
            return render_template("index.html", error="Error: message field is empty")
        if len(message) > 1200:
            return render_template("index.html", error="Error: message is too long")
        message_unicode = []
        for letter in message:
            message_unicode.append(ord(letter))
        message_binary = ""
        for num in message_unicode:
            message_binary += format(num, '08b') + " "
        message_bulbs = message_binary.replace("1", "🟡").replace("0", "⚫")
        return render_template("index.html", message=message_bulbs)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/decode", methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        message_binary = request.form.get("message").replace("🟡", "1").replace("⚫", "0")
        message_binary_arr = message_binary.split(" ")
        message_unicode_arr = []
        if not message_binary:
            return render_template("binary_converter.html", error="Error: message field is empty")
        if len(message_binary) > 25000:
            return render_template("binary_converter.html", error="Error: message too long")
        try:
            for binary in message_binary_arr:
                message_unicode_arr.append(int(binary, 2))
        except ValueError:
            return render_template("binary_converter.html", error="Error: invalid characters in message field")
        message_letter_arr = []
        for unicode in message_unicode_arr:
            message_letter_arr.append(chr(unicode))
        message_letter_arr = ''.join(message_letter_arr)
        return render_template("binary_converter.html", message=message_letter_arr)
    return render_template("binary_converter.html")

if __name__ == '__main__':
    app.run(debug=True)

